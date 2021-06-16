sentence = input("Enter any sentence: ")
if sentence.count('*') == 0:
    print(sentence)
else:
    i = 0
    sentence = list(sentence)
    while sentence[i-1] != '*':
        i+=1
    else:
        while i < len(sentence):
            sentence.insert(i, '-')
            sentence.pop()
            i+=1
    strSent = ''.join(sentence)

    print(strSent)