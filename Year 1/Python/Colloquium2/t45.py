import numpy as np

roofR = int(input('Roof R in m: '))
array = np.zeros(0)

while roofR > 0:
    roofR = int(roofR/5)
    array = np.append(array, roofR)
print(array)