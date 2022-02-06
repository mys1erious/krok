import numpy as np
import random

A = np.array([random.uniform(-10, 10) for i in range(8)])
count = 0

for i in A:
    if i < 0:
        count+=1

print(A)
print("Amount of negative nums: ", count)