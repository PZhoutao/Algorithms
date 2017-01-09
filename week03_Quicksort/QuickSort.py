# python 3.5
def QuickSort(lst):
    # This function will return the total number of comparisons used to sort the list
    return QuickSort_help(lst, 0, len(lst)-1)

def QuickSort_help(lst, l, r):
    # Choose pivot with "median-of-three" method
    if (r-l <=0):
        return 0
    mid = (l+r) // 2
    three = [(lst[l], l), (lst[mid], mid), (lst[r], r)]
    three.sort()
    pivot = three[1][1]
    temp = lst[l]
    lst[l] = lst[pivot]
    lst[pivot] = temp
    i = l+1
    for j in range(l+1, r+1):
        if lst[j] < lst[l]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            i += 1
    temp = lst[l]
    lst[l] = lst[i-1]
    lst[i-1] = temp
    leftChange = QuickSort_help(lst, l, i-2)
    rightChange = QuickSort_help(lst, i, r)
    return leftChange+rightChange+r-l


from sys import stdin

if __name__ == "__main__":
    lst = []
    for line in stdin:
        lst.append(eval(line.strip()))
    comp = QuickSort(lst)
    print("The total number of comparisons is %d" % comp)
