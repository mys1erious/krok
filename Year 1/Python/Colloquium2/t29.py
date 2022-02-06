import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(10)])
count = 0
a = int(input("Enter a: "))

for i in array:
    if i == a:
        break
    elif i % 2 == 0:
        count += 1

print(array)
print(count)