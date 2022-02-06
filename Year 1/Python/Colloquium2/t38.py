import numpy as np
import random

northWind = np.array([random.randint(0, 15) for i in range(10)])
southWind = np.array([random.randint(0, 15) for i in range(10)])
eastWind = np.array([random.randint(0, 15) for i in range(10)])
westWind = np.array([random.randint(0, 15) for i in range(10)])

count = 0

for i in southWind:
    if i >=8:
        count+=1

print(southWind)
print(count)