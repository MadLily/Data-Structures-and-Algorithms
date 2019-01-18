# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    def coin():
        yield 10
        yield 5
        yield 1
    gen = coin()
    while m !=0:
        div = next(gen)
        m, temp = m% div, m//div
        n += temp     
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
