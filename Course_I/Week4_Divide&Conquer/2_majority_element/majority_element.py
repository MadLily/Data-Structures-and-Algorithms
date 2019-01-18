# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    count = dict()
    for x in a:
        if x not in count.keys():
            count[x] = 0
        count[x] += 1
    res = max(count, key = count.get)
    if count[res] >= len(a)//2+1:
        return max(count)
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
