import numpy as np
import random

apartments = np.array([[random.randint(1, 7)]for i in range(30)])
apartments = np.flip(apartments, axis=0)

count = 0
for i in apartments:
    if i > 5:
        count += 1

print(apartments)
print("Number of apartments where live more them 5 ppl: ", count)