import random

numList = []
for i in range(0,37):
    numList.append(random.randint(-37,37))
    if numList[i] >0:
        numList[i] -= 0.5

numList.sort()
print(numList)