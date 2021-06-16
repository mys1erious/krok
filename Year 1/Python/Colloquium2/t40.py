import numpy as np
import random

array = np.array([random.randint(-10, 10) for i in range(10)])
summ = 0

for i in array:
    if i == 0:
        break
    elif i % 2 == 0:
        summ += i

print(array)
print(summ)