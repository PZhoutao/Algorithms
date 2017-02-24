# python 3.5
from sys import stdin
import random
import copy
from collections import defaultdict

def readGraph():
    adjListV = defaultdict(list)
    adjListE = {}
    Eset = set()
    EIdx = 0
    for line in stdin.readlines():
        line_split = [int(x) for x in line.split()]
        V = line_split[0]
        adjVs = line_split[1:]
        for adjV in adjVs:
            edge = (min(V,adjV), max(V,adjV))
            if edge not in Eset:
                adjListV[V].append(EIdx)
                adjListV[adjV].append(EIdx)
                adjListE[EIdx] = edge
                Eset.add(edge)
                EIdx += 1
    return adjListV, adjListE

def minCut(adjListV, adjListE, seed):
    random.seed(seed)
    edges = list(adjListE.keys())
    for i in range(len(adjListV)-2):
        mergeEdge = random.choice(edges)
        V1, V2 = adjListE[mergeEdge]
        V2Edges = adjListV.pop(V2)
        for e in V2Edges:
            if V1 in adjListE[e]:
                adjListV[V1].remove(e)
                adjListE.pop(e)
                edges.remove(e)
            else:
                adjListV[V1].append(e)
                otherV = adjListE[e][0] if adjListE[e][0] != V2 else adjListE[e][1]
                adjListE[e] = (min(V1,otherV), max(V1,otherV))
    return len(edges)

if __name__ == "__main__":
    adjListV, adjListE = readGraph()
    minC = float('inf')
    for i in range(500):
        seed = random.randint(1,10000)
        V_copy = copy.deepcopy(adjListV)
        E_copy = copy.deepcopy(adjListE)
        currMinCut = minCut(V_copy, E_copy, seed)
        minC = min(minC, currMinCut)
    print("The Minimum Cut is: ", minC)
