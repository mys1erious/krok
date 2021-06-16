from math import sqrt
n = int(input("Enter any number: "))
if n>0:
    answer = sqrt(3+sqrt(6+sqrt(3*(n-1)+sqrt(3*n))))
    print("Answer = ", answer)