import numpy as np
import random

array = np.array([random.randint(0, 20) for i in range(20)])
count = 0

for i in range(len(array)):
    if array[i] == i and array[i] % 3 == 0:
        count+=1

print(array)
print(count)