import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(30)])
summ = 0

for i in array:
    if i % 5 == 0 and i % 8 == 0:
        summ += i

print(array)
print("Sum of array elems which are divided by 5 and 8: ", summ)

