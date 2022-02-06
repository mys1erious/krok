import numpy as np
import random

array = np.array([random.randint(15, 90) for i in range(12)])
dry = np.zeros(0)
year = 0

for i in array:
    year+=i
    if i <30:
        dry = np.append(dry, i)

mean = array.mean()
minDry = min(dry)
print("Annual precipitation: ", year)
print("Average a month: ", mean)
print("Dry months: ", dry)
print("Driest month: ", minDry)