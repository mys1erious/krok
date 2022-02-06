import numpy as np
import random

minDecTemp = np.array([random.randint(-1, 10) for i in range(10)])
meanTemp = np.mean(minDecTemp)
count = 0

for i in minDecTemp:
    if i > meanTemp: count+=1

print(minDecTemp)
print(count)