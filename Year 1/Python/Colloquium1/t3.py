from math import fabs
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a>=b>=c:
    print(a*2, b*2, c*2)
else:
    print(fabs(a), fabs(b), fabs(c))