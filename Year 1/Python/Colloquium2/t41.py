import numpy as np
import random

array = np.array([random.randint(0, 20) for i in range(10)])
t = False
a = int(input("a: "))

Max = max(array)
count = 0
i = 0

for i in array:
    if i == Max:
        count += 1

if count == 1 and Max < a:
    t = True

print(array)
print(Max)
print(t)