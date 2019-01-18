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


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))

