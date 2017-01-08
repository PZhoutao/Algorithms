# Dynamic Programming
# Knapsack problem
# Given weights and values of n items, put these items in a knapsack 
# of capacity W to get the maximum total value in the knapsack. 
# python 3.5

import sys
sys.setrecursionlimit(10000)

def readData():
    f = open('knapsack_big.txt')
    line = [eval(x) for x in f.readline().strip().split()]
    W,n = line[0], line[1]
    items = []
    for i in range(n):
        items.append([eval(x) for x in f.readline().strip().split()])
    return W,items
    
def fillKnapsack(items, i, w, tempResults):
    if w <= 0:
        return 0,[]
    if i < 0:
        return 0,[]
    if (i, w) in tempResults:
        return tempResults[(i,w)]
    else:
        sub1 = fillKnapsack(items, i-1, w, tempResults)
        sub2 = fillKnapsack(items, i-1, w-items[i][1], tempResults)
        if w-items[i][1] < 0:
            tempResults[(i, w)] = sub1
        else:
            if sub1[0] > sub2[0]+items[i][0]:
                tempResults[(i, w)] = sub1
            else:
                tempResults[(i, w)] = (sub2[0]+items[i][0], sub2[1]+[i])
    return tempResults[(i, w)]

def main():
    W,items = readData()
    tempResults = {}
    total_val, path = fillKnapsack(items, len(items)-1, W, tempResults)
    print("Maximum value is %d" % total_val)

if __name__ == "__main__":
    main()


