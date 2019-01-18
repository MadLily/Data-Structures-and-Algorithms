# Uses python3
import sys


def get_change(money, coins = [1,3,4]):
    #write your code here
    res = (money+1) * [0]
    res[0] = 0
    for m in range (1,money+1):
        res[m] = 10**18
        for coin in coins:
            if m >= coin:
                num = res[m-coin] +1
                if num<res[m]:
                    res[m] = num
    return res[money]
    




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
