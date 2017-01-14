# python 3.5
# All-Pairs Shortest Paths
# Johnson's Algorithm
# 1. add a dummy vertex and run Bellman-Ford algorithm,
#    if the graph doesn't contain negative loop, calculate vertex weights 
# 2. reweight each edge so that there is no negative-length edge
# 3. run Dijkstra's Algorithm on each vertex to get all-pairs shortes path
import sys

def readGraph(file):
    f = open(file)
    size = [int(x) for x in f.readline().strip().split()]
    nV = size[0]; nE = size[1]
    Vinlist = [[] for x in range(nV)]
    Voutlist = [[] for x in range(nV)]
    Elist = [[] for x in range(nE)]
    for i in range(nE):
        E = [int(x) for x in f.readline().strip().split()]
        E[0] -= 1
        E[1] -= 1
        Voutlist[E[0]].append(i)
        Vinlist[E[1]].append(i)
        Elist[i] = E
    return Vinlist, Voutlist, Elist

def BellmanFord(Vinlist,Elist,Vstart):
    nV = len(Vinlist)
    sp = [float('inf')]*nV
    sp[Vstart] = 0
    for i in range(1, nV):
        sp_add1 = sp[:]
        for j in range(nV):
            sp_j = sp[j]
            for inE in Vinlist[j]:
                length = sp[Elist[inE][0]]+Elist[inE][2]
                if length < sp_j:
                    sp_j = length
            sp_add1[j] = sp_j
        if sp == sp_add1:
            break
        else:
            sp = sp_add1
    # check if there is negative loop
    noNegLoop = True
    for j in range(nV):
        for inE in Vinlist[j]:
            length = sp[Elist[inE][0]]+Elist[inE][2]
            if length < sp[j]:
                noNegLoop = False
                break
        if not noNegLoop:
            break
    if not noNegLoop:
        print("Negative loop exists!")
        return None
    else:
        return sp

def reweight(Elist, p):
    # for edge e = (u,v), cost(e)=cost(e)+p(u)-p(v)
    for e in Elist:
        e[2] += p[e[0]] - p[e[1]]
    return

def Dijkstra(Voutlist, Elist, Vstart):
    nV = len(Voutlist)
    minDist = [float('inf')]*nV
    set1 = set()
    set2 = set(list(range(nV)))
    adjV_dic = {Vstart:0}
    adjV_lst = sorted(list(adjV_dic.items()), key=lambda x:x[1])
    while len(adjV_lst) > 0:
        v,dist = adjV_lst.pop(0)
        del adjV_dic[v]
        set1 = set1 | {v}
        set2.remove(v)
        minDist[v] = dist
        for e_idx in Voutlist[v]:
            e = Elist[e_idx]
            if e[1] in set2:
                if e[1] in adjV_dic:
                    adjV_dic[e[1]] = min(adjV_dic[e[1]], dist+e[2])
                else:
                    adjV_dic[e[1]] = dist+e[2]
        adjV_lst = sorted(list(adjV_dic.items()), key=lambda x:x[1])
    return minDist

def getOrigDist(APSP, p):
    nV = len(APSP)
    for i in range(nV):
        for j in range(nV):
            APSP[i][j] += p[j]-p[i]
    return

def main():
    argv = sys.argv
    if len(argv) == 1:
        infile = "test.txt"
    else:
        infile = argv[1]
    # read in graph
    Vinlist, Voutlist, Elist = readGraph(infile)
    nV = len(Vinlist)
    nE = len(Elist)
    # add a dummy vertex
    for i in range(nV):
        Elist.append([nV,i,0])
        Vinlist[i].append(nE+i)
    Vinlist.append([])
    Voutlist.append(list(range(nV)))
    # run Bellman-Ford algorithm to get vertex weights
    p = BellmanFord(Vinlist,Elist,nV)
    if p is None:
        return
    # reweight edges so that there is no negative edge
    reweight(Elist, p)
    # remove dummy vertex
    Vinlist.pop()
    for i in range(nV):
        Vinlist[i].pop()
    Voutlist.pop()
    Elist = Elist[:nE]
    # run Dijkstra algorithm on each vertex to get All-Pairs Shortest Paths
    APSP = []
    for i in range(nV):
        if i > 0 and i % 20 == 0:
            print("calculating shortest path from vertex %d to all vertices" % i)
        APSP.append(Dijkstra(Voutlist, Elist, i))
    # restore path length under original edge weights
    getOrigDist(APSP, p)
    # get the shortest path among all shortest paths
    ssp = [min(x) for x in APSP]
    ssp = min(ssp)
    print("The smallest length among the all-pair shortest paths is %d" % ssp)
    return

if __name__ == "__main__":
    main()


