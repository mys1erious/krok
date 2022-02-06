import numpy as np
import random

array = np.array([random.randint(1, 100) for i in range(15)])
minNum = min(array)

print(array)
print(minNum)