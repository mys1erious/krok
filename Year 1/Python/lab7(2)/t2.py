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


sequence = input("Enter words on ru lang:  ")
sequence = sequence.replace(' ', ',', len(sequence))
words = sequence.split(',')
vowel = "уеыаоэяиюь"
vowel = set(vowel)
listAll = list()

for i in range(len(words)):
    listAll.extend(set(words[i])-vowel)

setAll = set(listAll)

ans = set()
for j in setAll:
    if listAll.count(j) == 1:
        ans.add(j)

ans = sorted(ans)

print("Consonants which appear only in one word: ", ans)
close_program()