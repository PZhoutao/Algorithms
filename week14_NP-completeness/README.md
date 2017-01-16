## Traveling Salesman Problem
Given a list of cities and the distances between each pair of cities, 
what is the shortest possible route that visits each city exactly once 
and returns to the origin city?
<br>
It's an NP-hard problem. I devised an algorithm where greedy algorithm 
is used first to obtain a path which is not necessarily the best solution. 
Then, path-grow method and early stopping criterion are used to get the final answer.
<br>
This is not an efficient algorithm. Just write it for fun.
