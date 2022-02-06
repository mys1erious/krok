import numpy as np
import random

array1 = np.array([random.randint(10, 100) for i in range(10)])
array2 = np.array([random.randint(10, 100) for i in range(10)])
array3 = np.zeros(0)


for i in range(len(array1)):
    array3 = np.append(array3, (array1[i] * array2[i]))

print(array1)
print(array2)
print(array3)