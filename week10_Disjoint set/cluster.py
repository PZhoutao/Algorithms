from DisjointSet import DisjointSet

def readGraph():
    '''
    The file contains edge costs for a complete graph.
    It has the following format:
    [number_of_nodes]
    [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
    [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
    ......
    '''
    f = open('clustering1.txt')
    n = int(f.readline())
    Elist = []
    for line in f.readlines():
        e = [int(x) for x in line.strip().split()]
        e[0] -= 1
        e[1] -= 1
        Elist.append(e)
    return (Elist, n)

def cluster(Elist, nV, k):
    '''
    Function for single-linkage hierarchical clustering, which is based on 
    Kruskal's minimum spanning tree algorithm.
    Input:
        Elist: Edge list for a complete graph(contains end verticies and edge cost)
        nV   : total number of vertices
        k    : number of clusters
    Output:
        The shortest distance between two verticies that belong to different clusters.
    '''
    assert nV >= k, "Number of clusters can't be greater than number of nodes!"
    Elist.sort(key=lambda x : x[2])
    dset = DisjointSet(nV)
    i = 0
    while len(dset) > k:
        e = Elist[i]
        i += 1
        if dset.find(e[0]) != dset.find(e[1]):
            dset.union(e[0], e[1])
    while dset.find(Elist[i][0]) == dset.find(Elist[i][1]):
        i += 1
    return Elist[i][2]

def main():
    Elist, nV = readGraph()
    d = cluster(Elist, nV, 4)
    print("The shortest distance is %d after clustering with k=4." % d)

if __name__=="__main__":
    main()

