import numpy as np
import random

arr1 = np.array([random.randint(0, 20) for i in range(10)])
arr2 = np.zeros(0)

for i in arr1:
    if i % 2 == 0:
        arr2 = np.append(arr2, i)

arr2Max = max(arr2)

count = 0
for i in arr2:
    if arr2Max == i:
        count+=1

print(arr2)
if count > 1:
    print("Duplicates of max exist")
else:
    print("Duplicates of max dont exist")