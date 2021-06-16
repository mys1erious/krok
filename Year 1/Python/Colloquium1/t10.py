from math import factorial
x = int(input("Enter any number: "))
if x>0:
    answer = (x-(x**3/factorial(3))+(x**5/factorial(5))-(x**7/factorial(7))+(x**9/factorial(9))-(x**11/factorial(11))+(x**13/factorial(13)))
    print("Answer: ", answer)
