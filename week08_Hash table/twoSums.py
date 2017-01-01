import random
import math
import sys

class ListNode(object):
    '''
    lineked list node
    '''
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class HashTable(object):
    '''
    a simple separate chaining hash table
    '''
    def __init__(self, cap=100, p=109345121):
        self._array = [None]*cap
        self._n = 0
        self._prime = p
        self._scale = 1+random.randrange(p-1)
        self._shift = random.randrange(p)
    
    def __len__(self):
        return self._n
        
    def _hashFunction(self, k):
        return (hash(k)*self._scale+self._shift) % self._prime % len(self._array)
    
    def insert(self, k):
        hashKey = self._hashFunction(k)
        lNode = ListNode(k, self._array[hashKey])
        self._array[hashKey] = lNode
        self._n += 1
        # resize array when number of elements store in hash table is greater than 2*array_length
        if self._n > 2*len(self._array):
            self._resize()
        return
    
    def delete(self, k):
        hashKey = self._hashFunction(k)
        head = self._array[hashKey]
        if head is None:
            raise KeyError(str(k)+' is not in the hash table!')
        if head.next is None:
            if head.data == k:
                self._array[hashKey] = None
                return
            else:
                raise KeyError(str(k)+' is not in the hash table!')
        before = head
        curr = head.next
        while curr is not None:
            if curr.data == k:
                before.next = curr.next
                return
            else:
                before = curr
                curr = curr.next
        raise KeyError(str(k)+' is not in the hash table!')
              
    def __contains__(self, k):
        hashKey = self._hashFunction(k)
        curr = self._array[hashKey]
        while curr is not None:
            if curr.data == k:
                return True
            curr = curr.next
        return False
    
    def _resize(self):
        cur_length = len(self._array)
        old = self._array
        self._array = [None]*2*cur_length
        self._n = 0
        for pt in old:
            while pt is not None:
                self.insert(pt.data)
                pt = pt.next
        return
        
def readData():
    f = open('twosum.txt')
    lst = []
    for line in f.readlines():
        line = line.strip()
        lst.append(int(line))
    return lst
    
def main():
    '''
    Given a number x, and a list of numbers, find if there are two distinct numbers a,b in 
    the list so that a+b = x.
    A hash table H is built to store the list of numbers. 
    For each element a in the list, look up x-a in H.
    '''
    x = 0
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    lst = readData()
    ht = HashTable()
    for n in lst:
        ht.insert(n)
    for a in lst:
        b = x - a
        if (b != a) and (b in ht):
            print("There are two distinct numbers a,b in the list so that a+b = %d" % x)
            break
    print("Can't find two distinct numbers in the list whose sum is %d." % x)
    return

if __name__ == "__main__":
    main()

