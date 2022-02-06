import numpy as np

n = 5
array = np.zeros(5)

for i in range(5):
    elem = int(input(f"Enter elem {i+1}/5: "))
    array[i] = elem

arrayStr = str(array)
arrayStr = arrayStr.replace('.', ',', len(array)-1)
mean = array.mean()

print("Array: ", arrayStr[1:-2])
print("Mean: ", mean)