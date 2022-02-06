import numpy as np
import random

def linear_search(array, elem):
    # Returns position of given elem

    i = 0
    while i < len(array) and array[i] != elem:
        i+=1
    if i == len(array):
        print('Element isnt in array')
    else:
        return i
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

ans = linear_search(arr, n)
print("Index:", ans)