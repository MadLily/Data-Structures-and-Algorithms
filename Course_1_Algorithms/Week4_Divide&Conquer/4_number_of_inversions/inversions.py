# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a,b,left, right, ave)
    return number_of_inversions

def merge(a,b,left, right, ave):
    arr1 = a[left:ave].copy()
    arr2 = a[ave:right].copy()
    i = 0
    j = 0
    k = left
    inv = 0
    while i < len(arr1) and j <len(arr2):
        if arr1[i] <= arr2[j]:
            a[k] = arr1[i]
            i +=1
        else:
            a[k] = arr2[j]
            j +=1
            inv += len(arr1) - i
        k += 1
    while i < len(arr1):
        a[k] = arr1[i]
        i+=1
        k+=1
    while j <len(arr2):
        a[k] = arr2[j]
        j+=1
        k+=1
    return inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))





