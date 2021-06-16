import numpy as np
import random

array = np.array([random.randint(0, 20) for i in range(20)])
print(array)

indOfMax = np.argmax(array)

array = np.insert(array, indOfMax+1, indOfMax)
print(array)