class Heap:
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



def findMedian(lst):
    # function to track the median of a stream of numbers
    # Input: a list of numbers
    # Output: a list of medians where the kth element is the median of the first k numbers in the input list
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    maxHeap = Heap("max")
    minHeap = Heap("min")
    maxHeap.insert(min(lst[:2]))
    minHeap.insert(max(lst[:2]))
    medians = [min(lst[:2])]*2
    for n in lst[2:]:
        if n < maxHeap.getTop():
            maxHeap.insert(n)
        else:
            minHeap.insert(n)
        if (len(maxHeap)-len(minHeap)) == 2:
            temp = maxHeap.extractTop()
            minHeap.insert(temp[0])
            medians.append(maxHeap.getTop())
        elif (len(maxHeap)-len(minHeap)) == 1:
            medians.append(maxHeap.getTop())
        elif len(maxHeap) == len(minHeap):
            medians.append(maxHeap.getTop()/2+minHeap.getTop()/2)
        elif (len(minHeap)-len(maxHeap)) == 1:
            medians.append(minHeap.getTop())
        elif (len(minHeap)-len(maxHeap)) == 2:
            temp = minHeap.extractTop()
            maxHeap.insert(temp[0])
            medians.append(minHeap.getTop())
    return medians

def main():
    f = open("Median.txt",'r')
    lst = []
    for line in f.readlines():
        n = int(line.strip())
        lst.append(n)
    medians = findMedian(lst)
    print("The sum of all medians is %d" % sum(medians))

if __name__ == '__main__':
    main()

