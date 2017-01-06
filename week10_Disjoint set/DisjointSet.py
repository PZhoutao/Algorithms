# Implementing the disjoint set data structure
class DisjointSet(object):
    def __init__(self, n):
        '''
        Each node in the up-tree is represented by a list[a, b], 
        where a is its parent node index (-1 means root), 
              b is the rank of the up-tree rooted at this node
        '''
        self._upTree = [[-1, 0] for i in range(n)]
        self._nSet = n
    
    def __len__(self):
        return self._nSet
    
    def find(self, i):
        '''
        Function find with path compression
        '''
        if self._upTree[i][0] == -1:
            return i
        else:
            root = self.find(self._upTree[i][0])
            self._upTree[i][0] = root
            return root
    
    def union(self, i, j):
        '''
        set with smaller rank will be merged into set with bigger rank
        '''
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            # print("%d and %d are in the same set." % (i,j))
            return
        if self._upTree[root_i][1] > self._upTree[root_j][1]:
            self._upTree[root_j][0] = root_i
        elif self._upTree[root_i][1] < self._upTree[root_j][1]:
            self._upTree[root_i][0] = root_j
        else:
            self._upTree[root_i][0] = root_j
            self._upTree[root_j][1] += 1
        self._nSet -= 1
        return
    
    def printPath(self, i):
        path = self.getPath(i)
        print("->".join([str(x) for x in path]))
    
    def getPath(self, i):
        path = [i]
        if self._upTree[i][0] != -1:
            parent_path = self.getPath(self._upTree[i][0])
            path = path + parent_path
        return path

