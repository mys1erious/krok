import numpy as np

arr = np.array(['Coca‑Cola', 'Diet Coke', 'Coke Zero Sugar', 'Coca‑Cola Life', 'Cherry Coke', 'Caffeine-free Diet Coke'])

for i in range(len(arr)-1):
    if arr[0] == arr[i+1]:
        arr = np.delete(arr, 0)
        break

print(arr)