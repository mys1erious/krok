import numpy as np
import random

minTempNov = np.array([random.randint(-15, 10) for i in range(10)])
count = 0

print(minTempNov)

for i in minTempNov:
    if i < -10:
        count+=1

print("Number of times when temp dropped less then 10deg:", count)