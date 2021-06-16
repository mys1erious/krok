a = int(input("Enter any non negavite number: "))
b = int(input("Enter any positive number: "))
r = float(input("Enter supposed remainder of division r: "))
s = float(input("Enter supposed remainder of division s: "))

if a>=0 and b>0 :
    div = a/b
    if div == r or div == s:
        print("U guessed right")
    else:
        print("U guessed wrong")