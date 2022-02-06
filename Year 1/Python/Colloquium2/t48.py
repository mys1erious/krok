import numpy as np


def array_of_words(line):

    # Array of entered words using numpy.

    wordList = []
    leng = 0
    for i in range(line):
        word = input(f"Word{i + 1}: ")
        wordList.append(word)
        if leng < len(word):
            leng = len(word)

    array = np.full((0, leng), ' ')

    for j in range(line):
        if len(wordList[j]) <= leng:
            wordList[j] = wordList[j] + (' ' * (leng - len(wordList[j])))
            array = np.insert(array, j, list(wordList[j]), axis=0)
    return(array)


N = int(input("Enter the number of brokers surnames: "))
brokerLastNames = array_of_words(N)
print(brokerLastNames)

brokerLastNames = np.flip(brokerLastNames, axis=0)
print('\n\n', brokerLastNames)