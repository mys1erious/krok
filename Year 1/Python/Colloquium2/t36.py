import numpy as np

def linear_array_creator(size):

    arr = np.zeros(size)

    for i in range(size):
        elem = int(input(f"Enter elem {i + 1}/{size}: "))
        arr[i] = elem
    return arr

arrSize = 10
array = linear_array_creator(arrSize)

summ = 0

for i in array:
    if i > 0:
        summ+=i

print(summ)