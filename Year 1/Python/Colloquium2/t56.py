import numpy as np
import random

arr = np.random.randint(0, 10, 10)
r = False
arrDup = np.zeros(0)

i = 0
while i in range(len(arr)-1):
    arrDup = np.append(arrDup, arr[i])
    for j in range(2):
        if arr[i] == arr[i+j+1]:
            arrDup = np.append(arrDup, arr[i])
        else:
            i += j+1
            break
    if len(arrDup) == 3:
        r = True
        break
    else:
        arrDup = np.zeros(0)

print(arr)
print(r)