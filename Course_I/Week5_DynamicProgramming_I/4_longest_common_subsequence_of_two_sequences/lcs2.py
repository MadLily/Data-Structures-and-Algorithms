#Uses python3

import sys


def lcs2(s, t):
    l_s = len(s) + 1
    l_t = len(t) + 1
    mat = np.matrix(np.zeros((l_s,l_t)))
    for i in range(1,l_s):
        for j in range(1,l_t):
            insertion = mat[i,j-1]
            deletion = mat[i-1,j]
            match = mat[i-1,j-1] + 1
            mismatch = mat[i-1,j-1]
            if s[i-1] == t[j-1]:
                mat[i,j] = max(insertion,deletion,match)
            else:
                mat[i,j] = max(insertion,deletion,mismatch)
    return int(mat[l_s-1,l_t-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    
    import numpy as np
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))


