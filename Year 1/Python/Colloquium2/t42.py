import numpy as np
import random
import math

array = np.array([random.randint(0, 10) for i in range(50)])

count = 0
indexI = 0
for i in array:
    if i*i < indexI < math.factorial(i):
        count += 1
    indexI += 1

print(count)