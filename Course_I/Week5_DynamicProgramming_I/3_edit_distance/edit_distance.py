# Uses python3
def edit_distance(s, t):
    l_s = len(s) + 1
    l_t = len(t) + 1
    mat = np.matrix(np.zeros((l_s,l_t)))
    mat[0] = np.arange(l_t)
    mat = mat.T
    mat[0] = np.arange(l_s)
    mat = mat.T
    for i in range(1,l_s):
        for j in range(1,l_t):
            insertion = mat[i,j-1] + 1
            deletion = mat[i-1,j] + 1
            match = mat[i-1,j-1]
            mismatch = mat[i-1,j-1] +1
            if s[i-1] == t[j-1]:
                mat[i,j] = min(insertion,deletion,match)
            else:
                mat[i,j] = min(insertion,deletion,mismatch)
    return int(mat[l_s-1,l_t-1])


if __name__ == "__main__":
    import numpy as np
    print(edit_distance(input(), input()))
