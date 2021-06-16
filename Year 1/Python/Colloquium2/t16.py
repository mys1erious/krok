import numpy as np
import random

array = np.array([random.randint(1, 50) for i in range(15)])
product = 1

for i in array:
    if i % 7 == 0:
        product = product * i

print(array)
print(product)
