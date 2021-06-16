import numpy as np

namesArr = np.array(['name1', 'name2', 'name3', 'name4', 'name5'])
priceArr = np.array([100,      200,     300,     400,     500])

print(namesArr)
print(priceArr)

P = int(input("Enter P: "))
indexP = np.where(priceArr == 300)
indexP = int(indexP[0])

if P in priceArr:
    priceArr = np.delete(priceArr, indexP)
    namesArr = np.delete(namesArr, indexP)

print(namesArr)
print(priceArr)