import random

def readData(file):
    f = open(file,'r')
    n_job = eval(f.readline())
    jobs = []
    for i in range(n_job):
        line = f.readline()
        line = line.strip().split()
        jobs.append((eval(line[0])/eval(line[1]), int(line[0]), int(line[1])))
    return jobs

def quickSort(lst):
    '''
    Quick sort a list of tuples, with each tuple's first element as sort key
    '''
    lst_cp = lst[:]
    quickSort_help(lst_cp, 0, len(lst)-1)
    return lst_cp

def quickSort_help(lst, l, r):
    if r-l <= 0:
        return
    else:
        idx = partition(lst, l, r)
        quickSort_help(lst, l, idx-1)
        quickSort_help(lst, idx+1, r)
    return

def partition(lst, l, r):
    pivot = random.randint(l, r)
    temp = lst[r]
    lst[r] = lst[pivot]
    lst[pivot] = temp
    pt = l
    for i in range(l,r):
        if lst[i][0]>lst[r][0]:
            temp = lst[i]
            lst[i] = lst[pt]
            lst[pt] = temp
            pt += 1
    temp = lst[r]
    lst[r] = lst[pt]
    lst[pt] = temp
    return pt

def main():
    jobs = readData('jobs.txt')
    jobs_sorted = quickSort(jobs)
    cost = 0
    finish_time = 0
    for job in jobs_sorted:
        finish_time += job[2]
        cost += finish_time*job[1]
    print("The weighted sum of completion times is %d" % cost)

if __name__ == '__main__':
    main()

