import numpy as np

surname = []
line = 5
leng = 0


for i in range(line):
    surn = input(f"Surname{i+1}: ")
    surname.append(surn)
    if leng < len(surn):
        leng = len(surn)

array = np.full((0, leng), ' ')

for j in range(line):
    if len(surname[j]) <= leng:
        surname[j] = surname[j]+(' '*(leng-len(surname[j])))
        array = np.insert(array, j, list(surname[j]), axis=0)

letter = input("Letter: ")

i=0
j=0

for i in array:
    if i[0] == letter:
        print(''.join(i))