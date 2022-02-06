import numpy as np
import random

temp = np.array([random.randint(-7, 15) for i in range(10)])
precipitation = np.array([random.randint(0, 40) for i in range(10)])

snow = 0
rain = 0

for i in range(len(temp)):
    if precipitation[i] != 0:
        if temp[i] > 0:
            rain += precipitation[i]
        else:
            snow += precipitation[i]

print("Rainfall: ", rain)
print("Snowfall: ", snow)