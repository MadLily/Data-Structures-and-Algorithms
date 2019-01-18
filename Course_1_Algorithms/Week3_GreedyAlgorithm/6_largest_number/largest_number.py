#Uses python3

import sys

def isGreaterOrEqual(a,b):
    return int(str(a) + str(b)) >= int(str(b) + str(a))



def largest_number(Digits):
    res = ""
    while len(Digits) != 0:
        maxDigit = 0
        for dig in Digits:
            if isGreaterOrEqual(dig,maxDigit):
                maxDigit = dig
        res += str(maxDigit)
        Digits.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))







