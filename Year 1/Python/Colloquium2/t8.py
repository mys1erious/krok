import numpy as np
import random

A = np.array([random.randint(-15, 30) for i in range(15)])

maxElem = max(A)
index = np.where(A == maxElem)

print(A)
print(maxElem)
print(index)
