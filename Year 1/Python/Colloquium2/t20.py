import numpy as np
import random

array = np.array([random.randint(50, 100) for i in range(20)])
summ = 0
n = int(input("Enter num: "))

for i in array:
    if i > n:
        summ += i

print(array)
print("Sum of array elems higher than entered num: ", summ)

