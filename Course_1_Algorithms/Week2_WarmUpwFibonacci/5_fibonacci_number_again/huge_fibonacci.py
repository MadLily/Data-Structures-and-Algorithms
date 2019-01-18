
# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    l = [0, 1]
    while (previous, current) != (m-1, 1):
        previous, current = current, (previous + current) % m
        l.append(current)
    
    return (l[n % len(l)])

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
