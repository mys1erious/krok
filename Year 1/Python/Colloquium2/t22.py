import numpy as np
import random

array = np.array([random.randint(5, 500) for i in range(10)])
product = 1

for i in array:
    if i % 3 == 0 and i % 9 == 0:
        product = product * i

print(array)
print("Product of array elems which are multiples of 3 and 9: ", product)

