import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(10)])
product = 1

for i in array:
    if i % 5 == 0:
        product = product * i

print(array)
print("Product of array elems which are multiples of 5: ", product)
