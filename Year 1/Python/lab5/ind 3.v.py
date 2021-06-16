def close_program():
    while True:
        closeProg = input("If u wanna continue type /c, if u wanna close the program type /exit: \n")
        if closeProg == '/exit':
            exit()
        elif closeProg == '/c':
            break
        else:
            print("Unidentified command, try again!")
            continue

while True:
    sentence = str(input("Enter sentence you wanna reverse: "))
    reversedSentence = reversed(sentence.split())
    print("Reversed sentence =", *reversedSentence)
    close_program()