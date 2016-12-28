## Implimentation of Dijkstra's shortest path algorithm
## python 3.5

def readData():
    f = open("dijkstraData.txt")
    G = {}
    for line in f.readlines():
        line = line.strip().split()
        V = line[0]
        adjV = line[1:]
        adjV = [x.split(',') for x in adjV]
        adjV = {x[0]:int(x[1]) for x in adjV}
        G[V] = adjV
    return G

def updateDist(dist, V, Vdist, G):
    adjV = G[V]
    for k,d in adjV.items():
        if k in dist:
            dist[k] = min(dist[k], Vdist+d)
    return

def dijkstra(G, start):
    '''
    Return a dictionary with all vertices in graph G as keys and 
    the length of the shortest path from each vertex to the starting 
    vertex as value
    '''
    included = {}
    allV = set(G.keys())
    dist = {x:float('inf') for x in allV}
    dist[start] = 0
    while len(dist) > 0:
        sortedV = sorted(dist.items(), key=lambda x:x[1])
        shortestDistV = sortedV[0][0]
        shortestDist = sortedV[0][1]
        included[shortestDistV] = shortestDist
        del dist[shortestDistV]
        updateDist(dist, shortestDistV, shortestDist, G)
    for k,d in included.items():
        if d == float('inf'):
            included[k] = 1000000
    return included

def main():
    G = readData()
    start = '1'
    shortestDist = dijkstra(G, start)
    target = ['7', '37', '59', '82', '99', '115', '133', '165', '188', '197']
    print("The shortest distances from vertex "+start+" to "+','.join(target)+" are:")
    print("%d, %d, %d, %d, %d, %d, %d, %d, %d, %d" % tuple([shortestDist[x] for x in target]))

if __name__ == "__main__":
    main()

