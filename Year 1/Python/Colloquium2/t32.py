import numpy as np
import random

array = np.array([random.randint(-10, 10) for i in range(10)])
t = False

for i in array:
    if i < 0 and i % 2 == 0:
        t = True
        break

print(array)
print(t)