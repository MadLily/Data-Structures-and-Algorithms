##Uses python3
#import sys
#import math
#
#def minimum_distance(x, y):
#    x_ind = sorted(range(len(x)), key=lambda k: x[k])
#    y_ind = sorted(range(len(y)), key=lambda k: y[k])
#
#
#def recursive(x,y, x_ind,y_ind,l,r):
#    #write your code here
#    if r <= l + 1
#        return 10 ** 18
#    elif r - l ==2:
#        return math.hypot(x[x_ind[l]]-x[x_ind[r]],y[y_ind[l]] - y[y_ind[r]])
#    else:
#        mid = (r + l)//2
##        min_left = recursive([x[x_cor] for x[x_cor] in x_ind[l:mid]],[y[y_cor] for y_cor in y_ind[l:mid]],x_ind,y_ind,l,mid)
##        min_left = recursive([x[x_cor] for x[x_cor] in x_ind[mid:r]],[y[y_cor] for y[y_cor] in y_ind[mid:r]],x_ind,y_ind,mid,r)
#        min_left = recursive(x,y,x_ind,y_ind,l,mid)
#        min_left = recursive(x,y,x_ind,y_ind,mid,r)
#        d = min(min_left,min_right)
#        mid_x =  x[x_ind[mid-1]]
#        mid_xs = [k for k in x[l:r] if mid_x-d <= k <= mid_x + d]
#        if len(mid_xs) <=1:
#            return d
#        else:
#            mid_ys = [ky for (kx,ky) in zip(x,y) if mid_x-d <= kx <= mid_x + d]
#
#            y_index = sorted(range(len(mid_ys)), key=lambda k: mid_ys[k])
#            d_mid = 10 ** 18
#            for i in range(len(y_index)):
#                d_temp = 10 ** 18
#                for j in range(max(0,i-6),i):
#                    if i==j:
#                        continue
#                    d_temp = min(math.hypot(mid_xs[y_index[i]]-mid_xs[y_index[j]],mid_ys[y_index[i]]-mid_ys[y_index[j]]),d_temp)
#                d_mid =min(d_mid,d_temp)
#            return min(d_mid,min_left,min_right)
#
#
#
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
#    n = data[0]
#    x = data[1::2]
#    y = data[2::2]
#    print("{0:.9f}".format(minimum_distance(x, y)))


#Uses python3
import sys
import math

def minimum_distance(x, y):
    y_ind = sorted(range(len(y)), key=lambda k: y[k])

    xx = [x[i] for i in y_ind]
    yy = [y[i] for i in y_ind]
    
#    x_ind = sorted(range(len(y)), key=lambda k: y[k])
    XX = xx.copy()
    XX.sort()
    return recursive(xx,yy,XX)




def recursive(x,y,XX):
    #write your code here
    if len(x) <=1:
        return 10 ** 18
    elif len(x) ==2:
        return math.hypot(x[0]-x[1],y[0]-y[1])
    else:

        mid_x = XX[len(XX)//2-1]

        left_ind = [i for i in range(len(x)) if x[i] <= mid_x]
        left_x = [x[i] for i in left_ind]
        left_y = [y[i] for i in left_ind]
        
        right_ind = [i for i in range(len(x)) if x[i] > mid_x]
        right_x = [x[i] for i in right_ind]
        right_y = [y[i] for i in right_ind]

        min_left = recursive(left_x,left_y,XX[:len(XX)//2])
        min_right = recursive(right_x,right_y,XX[len(XX)//2:])

        d = min(min_left,min_right)
        mid_xs = [k for k in x if mid_x-d <= k <= mid_x + d]

        if len(mid_xs) <=1:
            return d
        else:
            mid_ys = [ky for (kx,ky) in zip(x,y) if mid_x-d <= kx <= mid_x + d]
            
            d_mid = 10 ** 18
            for i in range(len(mid_ys)):
                d_temp = 10 ** 18
                for j in range(max(0,i-7),i):
                    d_temp = min(math.hypot(mid_xs[i]-mid_xs[j],mid_ys[i]-mid_ys[j]),d_temp)
                d_mid =min(d_mid,d_temp)
            return min(d_mid,min_left,min_right)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

