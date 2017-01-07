# Dynamic programming
# Given an array of numbers, find the subset of numbers in which 
# no pair of numbers are adjacent in the original array and the 
# sum is maximized
# python 3.5

def readArray():
    f = open('mwis.txt', 'r')
    n = eval(f.readline())
    arr = []
    for i in range(n):
        arr.append(eval(f.readline()))
    return arr

def getMax(arr):
    maxSumPrev2 = 0
    pathPrev2 = []
    maxSumPrev1 = arr[0]
    pathPrev1 = [0]
    for i in range(1,len(arr)):
        if maxSumPrev2+arr[i] > maxSumPrev1:
            maxSum = maxSumPrev2+arr[i]
            path = pathPrev2[:]
            path.append(i)
        else:
            maxSum = maxSumPrev1
            path = pathPrev1[:]
        maxSumPrev2 = maxSumPrev1
        pathPrev2 = pathPrev1
        maxSumPrev1 = maxSum
        pathPrev1 = path
    return maxSum,path

def main():
    arr = readArray()
    if len(arr) == 0:
        maxSum = 0
    elif len(arr) == 1:
        maxSUm = arr[0]
    else:
        maxSum,path = getMax(arr)
    print("The maximum-weight independent set of the path graph is %d" % maxSum)

if __name__ == "__main__":
    main()

