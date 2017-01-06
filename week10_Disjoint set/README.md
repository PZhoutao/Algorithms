## Disjoint Set

### Clustering problem1
File "clustering1.txt" contains the edge weights for a complete graph with 500 
nodes. This program uses Kruskal's minimum spanning tree algorithm to perform 
single-linkage hierarchical clustering on these nodes.

Disjoint set is used to keep track of the partition of clusters.

### Clustering problem2
File "clustering_big.txt" contains the node information of a much bigger graph 
(200000 nodes complete graph). Each node is represented by 24 bits, and the 
distance between each pair of nodes is defined as the number of different 
bits between the two nodes.

The question is: what is the largest value of k such that there is a k-clustering with
spacing at least 3? The number of edges is so big that Kruskal's MST algorithm 
is not applicable.

Solution: 
```
Remove duplicated nodes
create a Disjoint Set S for distinct_nodes
for each node i in distinct_nodes:
    generate all bit strings that differ from i by at most 2 bits by bitwise xor
    for each generated bit string j:
        if j in distinct_nodes:
            S.join(i,j)
return (number of sets in S)
```


