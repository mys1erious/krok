import numpy as np
import random

array = np.array([i for i in range(20)])
product = 1

for i in array:
    if i != 0:
        product = product * i

print(array)
print(product)