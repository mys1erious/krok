import numpy as np
import random

arr = np.random.randint(0, 10, 10)
print(arr)

arrDup = np.zeros(0)
arrDupInd = np.zeros(0)
i = 0
while i in range(len(arr)-1):
    arrDup = np.append(arrDup, arr[i])
    for j in range(len(arr)-i-1):
        if arr[i] == arr[i+j+1]:
            arrDup = np.append(arrDup, arr[i])
        else:
            break
    i += j + 1
    arrDupInd = np.append(arrDupInd, len(arrDup))
    arrDup = np.zeros(0)

print(arrDupInd)
print(int(max(arrDupInd)))