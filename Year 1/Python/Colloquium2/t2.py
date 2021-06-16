import numpy as np
import math

X = np.zeros(5)
sqrt = []
square = []

for i in range(5):
    elem = int(input(f"Enter elem {i+1}/5: "))
    X[i] = elem
    sqrt.append(f'{math.sqrt(elem):.{3}}')
    square.append(elem**2)

print("Array: ", X)
print("Sqrt of array: ", sqrt)
print("Square of array: ", square)