# Uses python3
import sys
import numpy as np

def optimal_sequence(n):
    sequence =  [0] * n
    prev = [0] * n
    for i in range(2,n+1):
        mn1,db2,db3 = 10**6, 10**6,10**6
        d3 = i % 3 == 0
        d2 = i % 2 == 0
        mn1 = sequence[i-2] + 1
        if not (d2 or d3):
            sequence[i-1] = mn1
        else:
            if d2:
                db2 = sequence[i//2-1] + 1
            if d3:
                db3 = sequence[i//3-1] + 1
            sequence[i-1] = min([mn1,db2,db3])
    seq = [n]
    while n>1:
        if (n%3!=0 and n%2 !=0) and sequence[n-2] < sequence[n-1]:
            seq.append(n-1)
            n-=1
        elif n%3 == 0 and sequence[n//3-1] < sequence[n-1]:
            seq.append(n//3)
            n = n//3
        elif n%2 == 0 and sequence[n//2-1] < sequence[n-1]:
            seq.append(n//2)
            n = n//2
        else:
            seq.append(n-1)
            n-=1

    return seq[::-1]




input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
