#Uses python3

import sys

def lcs3(d, e, f):
    l_s = len(d) + 1
    l_t = len(e) + 1
    l_f = len(f) + 1
    mat = np.zeros((l_s,l_t, l_f))
    for i in range(1,l_s):
        for j in range(1,l_t):
            for k in range(1,l_f):
                if d[i-1] == e[j-1] == f[k-1]:
                    mat[i,j,k] = mat[i-1,j-1,k-1] + 1
                else:
                    mat[i,j,k] = max(mat[i-1,j,k],mat[i,j-1,k],mat[i,j,k-1])
    return int(mat[l_s-1,l_t-1,l_f-1])


if __name__ == '__main__':
    import numpy as np
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
