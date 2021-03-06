# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    kkk = 0
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            if kkk!=0:
                a[i], a[j], a[j+kkk] = a[j+kkk], a[i], a[j]
            else:
                a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            kkk+=1
            a[i],a[j+kkk] = a[j+kkk],a[i]
    a[l], a[j] = a[j], a[l]
    return j,kkk


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m,kk = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m+kk + 1, r);



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
