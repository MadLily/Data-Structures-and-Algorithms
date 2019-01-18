# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def split_1q8(eq8):
    eq8 = re.split("([+-/*])", eq8)
    data = [int(x) for x in eq8 if x not in ['+','-','/','*']]
    ops = [x for x in eq8 if x in ['+','-','/','*']]
    return data, ops

def get_maximum_value(dataset):
    data, ops = split_1q8(dataset)
    n = len(data)
    m = np.zeros((n,n))
    M = np.zeros((n,n))
    for i in range( n ):
        m[i,i] = data[i]
        M[i,i] = data[i]
    for s in range(1,n):
        for ii in range(n-s):
            j = s + ii
            m[ii,j], M[ii,j] = min_n_max(ii,j,m,M,ops)
    #write your code here
    return int(M[0,n-1])

def min_n_max(i,j,m,M,ops):
    min_Res =  10**8
    max_Res = - 10**8
    for k in range(i,j): # j-1 or j?
        a =  evalt(M[i,k],M[k+1,j], ops[k])
        b =  evalt(M[i,k],m[k+1,j], ops[k])
        c =  evalt(m[i,k],M[k+1,j], ops[k])
        d =  evalt(m[i,k],m[k+1,j], ops[k])
        min_Res = min(min_Res,a,b,c,d)
        max_Res = max(max_Res,a,b,c,d)
    return (min_Res,max_Res)



if __name__ == "__main__":
    import re
    import numpy as np
    print(get_maximum_value(input()))
