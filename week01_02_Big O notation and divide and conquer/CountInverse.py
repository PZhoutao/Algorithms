def CountInv(lst):
    '''
    Function to count how many inversions are there in a list of numbers
    '''
    if len(lst) == 1:
        return lst,0
    else:
        mid = len(lst) // 2
        leftSort, leftInv = CountInv(lst[:mid])
        rightSort, rightInv = CountInv(lst[mid:])
        ret = []
        inv = leftInv + rightInv
        i = j = 0
        for k in range(len(lst)):
            if leftSort[i] <= rightSort[j]:
                ret.append(leftSort[i])
                i += 1
                if i == len(leftSort):
                    ret = ret + rightSort[j:]
                    break
            else:
                ret.append(rightSort[j])
                j += 1
                inv += len(leftSort) - i
                if j == len(rightSort):
                    ret = ret + leftSort[i:]
                    break
        return ret, inv


import sys

if __name__ == "__main__":
    lst = []
    for line in sys.stdin:
        lst.append(eval(line.strip()))
    Sorted,inv = CountInv(lst)
    print("Number of inversions in list:", inv)
