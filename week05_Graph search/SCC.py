from sys import stdin
import copy

print("Reading graph from file")
V = {}
E = {}
Vrev = {}
Erev = {}
ne = 0
for line in stdin:
    row = [eval(x) for x in line.split()]
    if (row[0] != row[1]):
        rowrev = list(row)
        rowrev.reverse()
        E[ne] = row
        Erev[ne] = rowrev
        if row[0] in V.keys():
            V[row[0]].append(ne)
        else:
            V[row[0]] = [ne]
        if row[1] in Vrev.keys():
            Vrev[row[1]].append(ne)
        else:
            Vrev[row[1]] = [ne]
        ne += 1
print("Graph input done")

print("Topological sort on reversed graph")
max_node = max(max(V.keys()), max(Vrev.keys()))
seq = list()
visited = [0]*max_node
stack = list()
for i in range(1, max_node+1):
    if visited[i-1] == 0:
        visited[i-1] = 1
        if i not in Vrev.keys():
            seq.append(i)
        else:
            stack.append((i, Vrev[i]))
            while len(stack) > 0:
                if len(stack[-1][1]) == 0:
                    v,e = stack.pop(-1)
                    seq.append(v)
                else:
                    edge = stack[-1][1].pop()
                    adj_v = Erev[edge][1]
                    if visited[adj_v-1] == 0:
                        visited[adj_v-1] = 1
                        if adj_v in Vrev.keys():
                            stack.append((adj_v, Vrev[adj_v]))
                        else:
                            seq.append(adj_v)

print("DFS on original graph")
seq.reverse()
visited = [0]*max_node
stack = list()
s = None
master = [0]*max_node
for i in seq:
    if visited[i-1] == 0:
        visited[i-1] = 1
        s = i
        master[i-1] = s
        if i in V.keys():
            stack.append((i, V[i]))
            while len(stack) > 0:
                if len(stack[-1][1]) == 0:
                    stack.pop(-1)
                else:
                    edge = stack[-1][1].pop()
                    adj_v = E[edge][1]
                    if visited[adj_v-1] == 0:
                        visited[adj_v-1] = 1
                        master[adj_v-1] = s
                        if adj_v in V.keys():
                            stack.append((adj_v, V[adj_v]))

count = {}
for i in master:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

count_lst = list(count.values())
count_lst.sort(reverse=True)
print("The sizes of the 5 largest SCCs are:")
print(count_lst[:5])

