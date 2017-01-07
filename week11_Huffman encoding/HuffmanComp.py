# Huffman compression
# python 3.5
import pickle
import re
import sys

def charCount(filename):
    # Function to count character frequency in a text file
    f = open(filename, 'r')
    charDic = {}
    for line in f.readlines():
        for ch in line:
            if ch in charDic:
                charDic[ch] += 1
            else:
                charDic[ch] = 1
    charDic['end'] = 1
    return charDic

class Queue(object):
    def __init__(self):
        self._array = []
    
    def __len__(self):
        return len(self._array)
        
    def enqueue(self,x):
        self._array.insert(0,x)
        return
    
    def dequeue(self):
        if len(self._array) == 0:
            print("The queue is empty!")
            return
        return self._array.pop()
    
    def peek(self):
        if len(self._array) == 0:
            print("The queue is empty!")
            return
        return self._array[-1]

def createTreeNode(freq,l=None,r=None,ch=None):
    treeNode = {'freq':freq,
                'left':l,
                'right':r,
                'ch':ch,
                'isLeaf':(l is None and r is None)}
    return treeNode

def HuffmanTree(charDic):
    # Function to build Huffman tree for text encoding.
    # Two queues are used to maintain tree nodes sorted by frequency
    sorted_char = sorted(list(charDic.items()), key=lambda x : x[1])
    q1 = Queue() ; q_merge = Queue()
    for tp in sorted_char:
        q1.enqueue(createTreeNode(freq=tp[1], ch=tp[0]))
    while (len(q1)+len(q_merge)) >= 2:
        node1 = getMinFreqNode(q1, q_merge)
        node2 = getMinFreqNode(q1, q_merge)
        node_merge = createTreeNode(freq=node1["freq"]+node2["freq"], l=node1, r=node2)
        q_merge.enqueue(node_merge)
    return q_merge.dequeue()

def getMinFreqNode(q1, q2):
    # Function to get the tree node with the smallest frequency from two queues
    if len(q1) != 0 and len(q2) != 0:
        if q1.peek()["freq"] < q2.peek()["freq"]:
            return q1.dequeue()
        else:
            return q2.dequeue()
    elif len(q1) == 0:
        return q2.dequeue()
    else:
        return q1.dequeue()
        
def encoding(TreeNode):
    # Function to get the code for each character by traversing Huffman tree
    code = {}
    curr_code = ''
    encoding_help(TreeNode, code, curr_code)
    return code

def encoding_help(TreeNode, code, curr_code):
    if TreeNode["isLeaf"]:
        code[TreeNode["ch"]] = curr_code
    else:
        encoding_help(TreeNode["left"], code, curr_code+'0')
        encoding_help(TreeNode["right"], code, curr_code+'1')
    return

def compress(filename, huffTree):
    code = encoding(huffTree)
    f_in = open(filename, 'r')
    text = f_in.read()
    coded_text = ''
    for ch in text:
        coded_text += code[ch]
    coded_text += code['end']
    out_filename = re.sub(r"\.[^\.]*$", ".bin", filename)
    f_out = open(out_filename, 'wb')
    ## write encoded text to a binary file
    while len(coded_text) >= 8:
        byte = int(coded_text[:8],2).to_bytes(1,'little')
        coded_text = coded_text[8:]
        f_out.write(byte)
    if len(coded_text):
        coded_text += '0'*(8-len(coded_text))
        byte = int(coded_text,2).to_bytes(1,'little')
        f_out.write(byte)
    f_out.close()
    ## save huffman tree for decompression
    tree_filename = re.sub(r"\.[^\.]*$", ".tree", filename)
    f_tree = open(tree_filename, 'wb')
    pickle.dump(huffTree, f_tree)
    f_tree.close()
    return

def main():
    assert len(sys.argv)>1, "File name not provided."
    filename = sys.argv[1]
    charDic = charCount(filename)
    huffTree = HuffmanTree(charDic)
    compress(filename, huffTree)
    return

if __name__ == "__main__":
    main()
