import numpy as np
import random

time = range(8, 21)
temp = random.randint(5, 20)
check = True

for i in time:
    print(f"Temperature at {i} hrs = {'%.2f'%temp}")
    tempChange = random.uniform(3, 0.1)
    temp = temp - tempChange
    if temp < 0 and check:
        print(f"First negative temperature was spotted at {i+1} hrs")
        check = False