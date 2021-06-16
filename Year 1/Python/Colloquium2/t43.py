import numpy as np
import random

array = np.array([random.randint(0, 200) for i in range(10)])
a = int(input('a: '))
b = int(input('b" '))
w = False

for i in array:
    if i % a == 0 and i % b != 0:
        w = True
        break

print(array)
print(w)