import numpy as np
import random

array = np.array([random.randint(-10, 20) for i in range(10)])
product = 1

for i in array:
    if i < 0:
        product = product * i

print(array)
print(product)