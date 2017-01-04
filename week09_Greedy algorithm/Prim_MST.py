class Heap(object):
    def __init__(self, type="min"):
        assert type in {"min", "max"}, "type could only be min or max"
        self._data = [(None,None)]
        self._size = 0
        self._type = type
    
    def __len__(self):
        return self._size
        
    def insert(self, key, value=None):
        self._data.append((key, value))
        self._size += 1
        self._heapifyUp(self._size)
    
    def getTop(self):
        if self._size == 0:
            print("Empty heap")
            return None
        else:
            return self._data[1][0]
        
    def extractTop(self):
        if self._size == 0:
            print("Empty heap")
            return None
        else:
            top = self._data[1]
            self._data[1] = self._data[self._size]
            self._data.pop()
            self._size -= 1
            self._heapifyDown(1)
            return top
    
    def _isHeap(self, parentIdx, idx):
        if self._type == "min":
            return self._data[parentIdx][0] <= self._data[idx][0]
        else:
            return self._data[parentIdx][0] >= self._data[idx][0]
        
    def _heapifyUp(self, i):
        if i == 1:
            return
        else:
            parentIdx = i//2
            if self._isHeap(parentIdx, i):
                return
            else:
                temp = self._data[i]
                self._data[i] = self._data[parentIdx]
                self._data[parentIdx] = temp
                self._heapifyUp(parentIdx)
            
    
    def _heapifyDown(self, i):
        leftChildIdx = i*2
        rightChildIdx = i*2 + 1
        if self._size < leftChildIdx:
            return
        elif self._size == leftChildIdx:
            exchangeChildIdx = leftChildIdx
        else:
            leftChildKey = self._data[leftChildIdx][0]
            rightChildKey = self._data[rightChildIdx][0]
            if self._type == "min":
                exchangeChildIdx = leftChildIdx if leftChildKey < rightChildKey else rightChildIdx
            else:
                exchangeChildIdx = leftChildIdx if leftChildKey > rightChildKey else rightChildIdx
        if self._isHeap(i, exchangeChildIdx):
            return
        else:
            temp = self._data[i]
            self._data[i] = self._data[exchangeChildIdx]
            self._data[exchangeChildIdx] = temp
            self._heapifyDown(exchangeChildIdx)

def readGraph(file):
    '''
    Function to read a graph from a text file and return the corresponding
    adjacency list and edge cost list
    '''
    f = open(file, 'r')
    graph_size = f.readline().strip().split()
    nV = int(graph_size[0])
    nE = int(graph_size[1])
    Vlist = [[] for x in range(nV)]
    Elist = [[] for x in range(nE)]
    Ecost = [0]*nE
    for i in range(nE):
        edge = [int(x) for x in f.readline().strip().split()]
        Elist[i] = [edge[0]-1, edge[1]-1]
        Ecost[i] = edge[2]
        Vlist[edge[0]-1].append(i)
        Vlist[edge[1]-1].append(i)
    return (Vlist, Elist, Ecost)

def main():
    '''
    This function implements Prim's minimum spanning tree algorithm.
    Edge cost can be positive or negative.
    A heap is used to find the edge with minimum cost among the edges that 
    connect explored and unexplored vertices at each iteration.
    '''
    Vlist, Elist, Ecost = readGraph('edges.txt')
    Vset1 = {0}
    Vset2 = set(range(1,500))
    cutEdgeCost = Heap()
    for e in Vlist[0]:
        cutEdgeCost.insert(Ecost[e], e)
    MST = []
    MST_cost = 0
    while len(Vset2)>0:
        while True:
            cost, minEdge = cutEdgeCost.extractTop()
            endV = Elist[minEdge]
            if (endV[0] in Vset2)^(endV[1] in Vset2):
                break
        mergeV = endV[0] if endV[0] in Vset2 else endV[1]
        Vset1.add(mergeV)
        Vset2.remove(mergeV)
        MST.append(minEdge)
        MST_cost += cost
        for adjE in Vlist[mergeV]:
            endV = Elist[adjE]
            if (endV[0] in Vset2)^(endV[1] in Vset2):
                cutEdgeCost.insert(Ecost[adjE], adjE)
    print("The total length of the minimum spanning tree is %d" % MST_cost)

if __name__ == "__main__":
    main()

