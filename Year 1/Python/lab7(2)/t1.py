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

while True:
    sequence = input("Enter only integers: ")
    sequence = sequence.split()
    try:
        seqInt = set(map(int, sequence))
    except ValueError:
        print("U entered sth other than int")
        exit()

    print("Amount of repeated integers:", len(sequence) - len(seqInt))
    close_program()