# Huffman decompression
# python 3.5
import pickle
import re
import sys

def readHuffTree(tree_filename):
    f_tree = open(tree_filename, 'rb')
    huffTree = pickle.load(f_tree)
    return huffTree

def decompress(filename, huffTree):
    f_in = open(filename, 'rb')
    out_filename = re.sub(r'\.[^\.]*$', '_decompress.txt', filename)
    f_out = open(out_filename, 'w')
    ## readin the compressed binary file, and restore it to binary string
    bi_code = f_in.read()
    bi_code_expand = ''
    for byte_num in bi_code:
        byte = bin(byte_num)
        bi_code_expand += '0'*(10-len(byte)) + byte[2:]
    ## use huffTree to decode binary string
    decoded_file = ''
    curr_node = huffTree
    isEnd = False
    i = 0
    while not isEnd:
        bit = bi_code_expand[i]
        i += 1
        if bit == '0':
            curr_node = curr_node['left']
        else:
            curr_node = curr_node['right']
        if curr_node['isLeaf']:
            if curr_node['ch'] == 'end':
                isEnd = True
            else:
                decoded_file += curr_node['ch']
                curr_node = huffTree
    f_out.write(decoded_file)
    f_out.close()
    return
    
def main():
    assert len(sys.argv) > 1, "Name of binary file not provided."
    filename = sys.argv[1]
    tree_filename = re.sub(r'\.[^\.]*$', '.tree', filename)
    huffTree = readHuffTree(tree_filename)
    decompress(filename, huffTree)
    return

if __name__ == "__main__":
    main()


