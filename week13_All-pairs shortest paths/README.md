## All-Pairs Shortest Paths
### Johnson's algorithm
1. Add a dummy vertex and run Bellman-Ford algorithm, if the graph 
doesn't contain negative loop, calculate vertex weights 
2. Reweight each edge so that there is no negative-length edge
3. Run Dijkstra's Algorithm on each vertex to get all-pairs shortes path

Graphs are provided through text file in the following format:
\[number of vertices\] \[number of edges\]
\[head vertex of edge1\] \[tail vertex of edge1\] \[edge1 length\]
\[head vertex of edge2\] \[tail vertex of edge2\] \[edge2 length\]
......

"test.txt" is a small graph, "g1.txt" and "g3.txt" are larger graphs.
"g1.txt" contains negativ loops, "g3.txt" doesn't

Run the code by the following commands:
```
python APSP.py test.txt
python APSP.py g1.txt
python APSP.py g3.txt
```
