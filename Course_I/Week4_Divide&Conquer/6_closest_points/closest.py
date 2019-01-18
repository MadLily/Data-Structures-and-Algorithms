#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    if len(x) <=1:
        return 10 ** 18
    elif len(x) ==2:
        return math.hypot(x[0]-x[1],y[0]-y[1])


    x_index = sorted(range(len(x)), key=lambda k: x[k])
    left_x = [x[i] for i in x_index[:len(x_index)//2]]
    left_y = [y[i] for i in x_index[:len(x_index)//2]]

    right_x = [x[i] for i in x_index[len(x_index)//2:]]
    right_y = [y[i] for i in x_index[len(x_index)//2:]]
    mid_x = left_x[-1]

    min_left = minimum_distance(left_x,left_y)
    min_right = minimum_distance(right_x,right_y)

    d = min(min_left,min_right)
    mid_xs = [k for k in x if mid_x-d <= k <= mid_x + d]
    if len(mid_xs) <=1:
        return d
    else:
        mid_ys = [ky for (kx,ky) in zip(x,y) if mid_x-d <= kx <= mid_x + d]

        y_index = sorted(range(len(mid_ys)), key=lambda k: mid_ys[k])
        d_mid = 10 ** 18
        for i in range(len(y_index)):
            d_temp = 10 ** 18
            j = i+1
            while j in range(i+1,min(i+7,len(y_index))) and abs(mid_ys[y_index[i]]-mid_ys[y_index[j]])<d:
                d_temp = min(math.hypot(mid_xs[y_index[i]]-mid_xs[y_index[j]],mid_ys[y_index[i]]-mid_ys[y_index[j]]),d_temp)
                j +=1
            d_mid =min(d_mid,d_temp)
        return min(d_mid,min_left,min_right)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
