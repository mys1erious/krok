import numpy as np
import random

A = np.array([random.uniform(-20, 10) for i in range(12)])

print(A)

for i in range(len(A)):
    if A[i] < 0:
        A[i] = 0

print(A)