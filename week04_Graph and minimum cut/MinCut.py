# python 3.5
def MinCut(v, m, seed):
    random.seed(seed)
    for i in range(len(v)-2):
        nm = len(m)
        remove = random.choice(list(m.keys()))
        node1 = m[remove][0]
        node2 = m[remove][1]
        for n2edge in v[node2]:
            if node1 in m[n2edge]:
                del m[n2edge]
                v[node1].remove(n2edge)
            else:
                v[node1].append(n2edge)
                if node2 == m[n2edge][0]:
                    m[n2edge] = (node1, m[n2edge][1])
                else:
                    m[n2edge] = (m[n2edge][0], node1)
        del v[node2]
    return(len(m))

from sys import stdin
import random, copy

if __name__ == "__main__":
    v = {}
    m = {}
    nm = 1
    for line in stdin.readlines():
        row = [eval(x) for x in line.split()]
        node = row[0]
        adjs = row[1: ]
        v[node] = []
        for adj in adjs:
            if adj not in v.keys():
                m[nm] = (row[0], adj)
                v[node].append(nm)
                nm += 1
            else:
                for edge in v[adj]:
                    if node in m[edge]:
                        v[node].append(edge)
                        break

    minc = nm
    lst = list(range(10000))
    for i in range(500):
        seed = random.choice(lst)
        v_copy = copy.deepcopy(v)
        m_copy = copy.deepcopy(m)
        currmc = MinCut(v_copy, m_copy, seed)
        if currmc < minc:
            minc = currmc
    print(minc)


