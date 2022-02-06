import os
import random


path = 'D:/+brain/KROK/Programming/Labs/Year1/lab11(6)'

for i in range(1, 6):
    filename = f'f{i}.txt'
    seq = [random.uniform(0, 100)for i in range(10)]
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.close()
    with open(filename, 'w+') as f:
        seq = str(seq)
        seq = seq[1:-1]
        f.write(seq)


transferSeq = [[1, 3], [2, 4], [3, 5], [4, 2], [5, 1]]

helpFile = 'h.txt'
for i in range(len(transferSeq)):
    f1 = f'f{transferSeq[i][0]}.txt'
    f2 = f'f{transferSeq[i][1]}.txt'

    f_1 = open(f1, 'r+')
    text1 = f_1.read()
    f_1.truncate(0)
    f_2 = open(f2, 'r+')
    text2 = f_2.read()
    f_2.truncate(0)
    f_2.seek(0)
    f_2.write(text1)
    f_1.seek(0)
    f_1.write(text2)

    f_1.close()
    f_2.close()
