# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)
    if x < a[0]:
        return 0
    elif x > a[-1]:
        return len(a)
    else:
        while left!=right:
            if x >= a [left + (right-left)//2]:
                left += (right-left+1)//2
            else:
                right -= (right-left+1)//2
        return left


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    for i in range(len(points)):
        pls = binary_search(starts, points[i])
        mns = binary_search(ends, points[i]-1)
        cnt[i] = pls - mns
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
