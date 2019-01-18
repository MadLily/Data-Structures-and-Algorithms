# Uses python3
import sys
import itertools

#def partition3(A):
#    for c in itertools.product(range(3), repeat=len(A)):
#        sums = [None] * 3
#        for i in range(3):
#            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
#
#        if sums[0] == sums[1] and sums[1] == sums[2]:
#            return 1
#
#    return 0
def optimal_weight(W, w):
    # write your code here
    values = np.zeros((len(w)+1,W+1))
    for j in range(len(w)):
        for i in range(1,W + 1):
            values[j+1,i] = values[j,i]
            if w[j] <= i:
                val = values[j,i-w[j]] + w[j]
                if values[j+1,i] < val:
                    values[j+1,i] = val
#    return int(values[len(w),W])
    return values

#
#def partition3(A):
#    W = sum(A)
#    if W%3 != 0:
#        return 0
#    else:
#        W = W // 3
#        res1 = optimal_weight(W, A)
#        res2 = optimal_weight(2*W, A)
#        if res1 == W and res2 == 2*W:
#            return 1
#        else:
#            return 0

def trace(values,W,A):
    use = [0] * len(A)
    for i in range(len(A)):
        if res[



def partition3(A):
    W = sum(A)
    if W%3 != 0:
        return 0
    else:
        W = W // 3
        res1 = optimal_weight(W, A)
        res2 = optimal_weight(2*W, A)
        if res1 == W and res2 == 2*W:
            return 1
        else:
            return 0





if __name__ == '__main__':
    input = sys.stdin.read()
    import numpy as np
    n, *A = list(map(int, input.split()))
    print(partition3(A))

