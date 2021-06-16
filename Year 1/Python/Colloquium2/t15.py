import numpy as np
import random

array = np.array([random.randint(100, 200) for i in range(20)])
summ = 0

for i in array:
    if i % 2 == 0:
        summ+=i

print(array)
print('Sum of even numbers: ', summ)