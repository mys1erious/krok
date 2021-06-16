import numpy as np
import random

arr1 = np.array([random.randint(0, 20) for i in range(10)])
arr2 = np.zeros(0)
print(arr1)


for i in range(len(arr1)):
    if arr1[i] == i+10:
        arr2 = np.append(arr2, arr1[i])

if len(arr2) > 0:
    print('Elements which higher of their index by 10\n', arr2)
else:
    print('No such elements')