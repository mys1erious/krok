import numpy as np
import random

arr = np.zeros(0)
size = 20

for i in range(size):
    elem = int(input(f"Enter elem {i+1}/{size}: "))
    arr = np.append(arr, elem)

uni, count = np.unique(arr, return_counts=True)

print(uni)
print(count)

dup = False
for i in count:
    if i > 1:
        dup = True
        break

if dup:
    print("Duplicates exist")
else:
    print("Duplicates dont exist")