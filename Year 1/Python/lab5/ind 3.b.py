def close_program():

    # Gives you the choice to continue or close the program.

    while True:
        closeProg = input("----If u wanna continue type /c, if u wanna close the program type /exit: \n")
        if closeProg == '/exit':
            exit()
        elif closeProg == '/c':
            break
        else:
            print("Unidentified command, try again!")
            continue

def normal_sequence(sentence):

    #Creates sequence-list of given string. From 2 to 20 words, 1 word contains up to 5 letters.

    sentence = sentence.casefold()
    sentList = sentence.split(' ', 19)

    length = len(sentList)
    listOfNormalWords = list()

    for i in range(length):
        taken = sentList.pop()
        lettersOfTaken = list(taken)
        while len(lettersOfTaken) > 5:
            lettersOfTaken.pop()
            fiveLetters = lettersOfTaken
        else:
            fiveLetters = lettersOfTaken
            wordOfFive = ''.join(fiveLetters)
            listOfNormalWords.append(wordOfFive)

    listOfNormalWords.reverse()
    return listOfNormalWords

def without_lasts(sentence):

    # Deletes all words which same to the last one from given list.

    sentenceCopy = sentence.copy()
    lastWord = sentenceCopy.pop()
    sentenceCopy.append(lastWord)
    length = len(sentenceCopy)
    newList = list()

    for j in range(length):
        taken = sentenceCopy.pop()
        if taken != lastWord:
            newList.append(taken)

    newList.reverse()
    return newList

def deletes_from_given_sequence(sentence, toDel):

    # Deletes all words from given list in which letters sequentially arranged with beggining of UA alphabet.

    sentenceCopy = sentence.copy()
    sentenceCopy2 = sentence.copy()
    length = len(sentence)

    toDelList = list(toDel)
    toDelCopy = toDelList.copy()

    for i in range(length):
        taken = sentenceCopy2.pop()
        for j in range(len(toDelList)):
            str = ''.join(toDelList)
            if taken == str:
                sentenceCopy.remove(taken)
            toDelList.pop()
        toDelList = toDelCopy.copy()
    return sentenceCopy

while True:
    sentence = input("Enter any string: ")
    toDel = 'abvgd'

    sequence = normal_sequence(sentence)

    noLast = without_lasts(sequence)
    noAbvgd = deletes_from_given_sequence(sequence, toDel)
    noLast, noAbvgd = ' '.join(noLast), ' '.join(noAbvgd)

    print("Sequence of given string: ", sequence)
    print("All words except same to the last: ", noLast, sep='\n--')
    print("All words except those which letters sequentially arranged with beggining of UA alphabet: ", noAbvgd, sep='\n--')
    close_program()