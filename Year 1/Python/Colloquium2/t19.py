import numpy as np
import random

array = np.array([random.randint(200, 300) for i in range(20)])
summ = 0

for i in array:
    if i % 2 == 3:
        summ += i

print(array)
print(summ)