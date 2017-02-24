from sys import stdin
import copy, os
from collections import defaultdict, Counter

def readGraph():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(curr_dir+os.path.sep+"SCC.txt")
    adjListV = defaultdict(list)
    for line in f.readlines():
        endV = [int(x) for x in line.split()]
        adjListV[endV[0]].append(endV[1])
    return adjListV

def reverseGraph(G):
    revG = defaultdict(list)
    for V, adjVs in G.items():
        for adjV in adjVs:
            revG[adjV].append(V)
    return revG

def topoSort(G):
    topoOrder = []
    isVisited = defaultdict(bool)
    stack = []
    for V in G.keys():
        if not isVisited[V]:
            stack.append([V, 0])
            isVisited[V] = True
            while len(stack):
                if stack[-1][1] == 1:
                    vertex,_ = stack.pop()
                    topoOrder.append(vertex)
                else:
                    vertex = stack[-1][0]
                    if vertex not in G:
                        stack.pop()
                        topoOrder.append(vertex)
                    else:
                        stack[-1][1] = 1
                        for adjV in G[vertex]:
                            if not isVisited[adjV]:
                                isVisited[adjV] = True
                                stack.append([adjV, 0])
    return reversed(topoOrder)
    
def getSCC(G, topoOrder):
    isVisited = defaultdict(bool)
    VAssign = defaultdict(int)
    stack = []
    for V in topoOrder:
        if not isVisited[V]:
            isVisited[V] = True
            VAssign[V] = V
            stack.append(V)
            while len(stack):
                vertex = stack.pop()
                if vertex not in G:
                    continue
                for adjV in G[vertex]:
                    if not isVisited[adjV]:
                        isVisited[adjV] = True
                        VAssign[adjV] = V
                        stack.append(adjV)
    SCC = Counter(list(VAssign.values()))
    SCC_size = list(SCC.values())
    SCC_size.sort(reverse=True)
    return SCC_size[:5]

if __name__ == "__main__":
    print("Read graph from file")
    print("The graph is very big, be patient~")
    G = readGraph()
    print("Graph input finished")
    revG = reverseGraph(G)
    print("Topological sort on reversed graph")
    topoOrder = topoSort(revG)
    print("DFS on original graph")
    SCC_size = getSCC(G, topoOrder)
    print("The sizes of the 5 largest SCCs are:")
    print(SCC_size)   

