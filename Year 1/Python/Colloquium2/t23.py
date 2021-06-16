import numpy as np
import random

array = np.array([random.randint(150, 300) for i in range(20)])
summ = 0
mean = array.mean()

for i in array:
    if i < mean:
        summ += i

print(array)
print("Sum of array elems less than mean of array: ", summ)

