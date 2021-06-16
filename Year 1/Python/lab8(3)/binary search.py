import numpy as np
import random

def binary_search(array, elem):

    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right)//2
        if array[mid] == elem:
            return mid
        else:
            if array[mid] < elem:
                left = mid+1
            else:
                right = mid-1


def linear_array_creator(size):

    arr = np.zeros(size)

    for i in range(size):
        elem = int(input(f"Enter elem {i + 1}/{size}: "))
        arr[i] = elem
    return arr


arrSize = int(input("Enter size of array: "))
arr = linear_array_creator(arrSize)
arr = sorted(arr)
n = int(input("Enter int which u`r looking for: "))

ans = binary_search(arr, n)
print("Index:", ans)
