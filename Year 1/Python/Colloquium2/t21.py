import numpy as np
import random

array = np.array([random.uniform(50, 100) for i in range(10)])
product = 1
n = int(input("Enter num: "))

for i in array:
    if i < n:
        product = product * i

print(array)
print("Product of array elems less than entered num: ", product)