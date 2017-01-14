### Strongly Connected Components
File "SCC.txt" contains the edges of a directed graph. This program computes 
the number of strongly connected components (SCCs) in a given graph by:
* Run topological sort on reversed graph
* Run DFS on original graph, processing node in decreasing order of finishing 
times in topological sort

Run the program by:
```
# the graph is very large, this might take 2~3 minutes
cat SCC.txt | python SCC.py
```
