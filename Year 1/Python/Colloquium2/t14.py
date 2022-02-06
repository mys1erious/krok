import numpy as np
import random

array = np.zeros(10)

time = 10
g = 9.8
ans = 0

for i in range(time):
    ans = (g * i**2)/2
    print(f'Distance travelled by a freely falling body in {i} secs', ans)