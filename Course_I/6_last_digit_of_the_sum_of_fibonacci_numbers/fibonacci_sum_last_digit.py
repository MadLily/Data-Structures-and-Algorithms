# Uses python3
import sys

#def fibonacci_sum_naive(n):
#    if n <= 1:
#        return n
#
#    previous = 0
#    current  = 1
#    sum      = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#        sum += current
#
#    return sum % 10
#
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    n = int(input)
#    print(fibonacci_sum_naive(n))

def fibonacci_sum(n):
    if n <= 1:
        return n
    l = [0,1]
    prev = 0
    curr = 1
    while (prev, curr)!= (9,0):
        prev, curr = curr, (prev + curr + 1) % 10
        l.append(curr)
    return l[n % len(l)]
#    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))

