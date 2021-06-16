import numpy as np
import random

minWaterTemp = np.array([random.randint(12, 30) for i in range(10)])

threshold = 20
count = 0

for i in minWaterTemp:
    if i > threshold: count += 1


print(minWaterTemp)
print("Normal days to swim in the sea:", count)