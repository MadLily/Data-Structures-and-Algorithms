# Uses python3
import sys


#'''With Repititions'''
#def optimal_weight(W, w):
#    # write your code here
#    values = [0]* (W + 1)
#    for i in range(1,W + 1):
#        for j in range(len(w)):
#            if w[j] <= i:
#                val = values[W - w[j]] + w[j]
#                if values[i] < val:
#                    values[i] = val
#    return values[-1]

'''Without Repititions'''
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
    return int(values[len(w),W])



if __name__ == '__main__':
    input = sys.stdin.read()
    import numpy as np
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

