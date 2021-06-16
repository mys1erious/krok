import numpy as np
import random

T = np.zeros(6)

for i in range(6):
    elem = float(input(f"Enter temp {i+1}/6: "))
    T[i] = elem

maxt = max(T)
mint = min(T)
meant = T.mean()

print("Max temp:", maxt)
print("Min temp:", mint)
print("Mean temp:", meant)