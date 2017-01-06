from DisjointSet import DisjointSet
import re

def readGraph():
    '''
    The file contains 200000 bit string, each represents a vertex in the graph.
    It has the following format:
    [# of nodes] [# of bits for each node]
    [first bit of node 1] ... [last bit of node 1]
    [first bit of node 2] ... [last bit of node 2]
    ......
    The distance between two vertices u and v is defined as the number of 
    different bits between u and v.
    '''
    f = open('clustering_big.txt')
    n, dim = tuple([int(x) for x in f.readline().strip().split()])
    Vlist = []
    for i in range(n):
        V = f.readline().strip()
        V = re.sub(r'\s', '', V)
        Vlist.append(V)
    return Vlist, dim

def cluster(Vlist, dim):
    '''
    Function to cluster a list of nodes so that the single link distance between each
    pair of cluster is at least 3 and the number of clusters is maximized
    Input:
        Vlist: bit string representation of all nodes
        dim  : dimension of each node (length of bit string)
    Output:
        Largest number of clusters such that the spacing between any pair of clusters is at least 3
    '''
    distinct_V = {}
    i = 0
    for V in Vlist:
        intV = int(V,2)
        if intV not in distinct_V:
            distinct_V[intV] = i
            i +=1
    dset = DisjointSet(len(distinct_V))
    ## create a list of bit strings with length <= dim and at most 2 bits are "1"
    permutation_lst = []
    for i in range(dim):
        permutation_lst.append("1"+"0"*i)
    for i in range(dim-1):
        for j in range(i+1, dim):
            permutation_lst.append("1"+"0"*(j-i-1)+"1"+"0"*(23-j))
    permutation_lst = [int(x,2) for x in permutation_lst]
    for V in distinct_V.keys():
        V_permu2 = [V^x for x in permutation_lst]
        for v_permu in V_permu2:
            if v_permu in distinct_V:
                dset.union(distinct_V[V], distinct_V[v_permu])
    return len(dset)

def main():
    Vlist, dim = readGraph()
    k = cluster(Vlist, dim)
    print("There can be at most %d clusters." % k)

if __name__=="__main__":
    main()


