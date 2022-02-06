import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(10)])

i = 0
minArr = min(array)
check = False
summ = 0

while i in range(len(array)-1):
    if array[i] != minArr and check == False:
        i+=1
    else:
        check = True
        summ+=array[i+1]
        i+=1


print(summ)
print(summ)