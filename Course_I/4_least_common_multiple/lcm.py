# Uses python3
import sys

#def lcm_naive(a, b):
#    for l in range(1, a*b + 1):
#        if l % a == 0 and l % b == 0:
#            return l
#
#    return a*b
#
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    a, b = map(int, input.split())
#    print(lcm_naive(a, b))


def gcd(a, b):
    mn, mx = min(a,b), max(a,b)
    while mx % mn != 0:
        mn, mx = min(mn, mx % mn),max(mn, mx % mn)
    return mn

def lcm(a, b):
    g = gcd(a ,b)
    res = int(a/g) * b
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
