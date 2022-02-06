def checks_digit_in_number_square(number, digit):
    number = number**2
    print("Square of entered num =", number)
    summ = 0

    while number > 0:
        a1 = number // 10
        a2 = a1 * 10
        a3 = number - a2
        summ = a3
        number = number // 10
        if summ == digit:
            print(f"Digit {digit} is in square")
            break
    else:
        print(f"Digit {digit} isnt in square")

def reversed_number(number):
    nCopy = number
    amount = 0
    reverse = 0

    while nCopy>0:
        nCopy = nCopy//10
        amount+=1

    while amount>0:
        a1 = number//10
        a1 = a1 * 10
        a2 = number - a1
        a2 = a2*10**(amount-1)
        reverse +=a2
        amount -= 1
        number = number//10

    print("Reversed version of num =", reverse)

def changes_first_and_last_digits(number):
    n2 = number
    n3 = number
    c2 = n3
    i2 = 0

    while (c2 != 0):
        c2 = int(c2 // 10)
        i2 += 1
    changed = (n3 % 10) * (10 ** (i2 - 1)) + (((n3 % (10 ** (i2 - 1))) // 10) * 10) + (n3 // (10 ** (i2 - 1)))
    print("Number with first and last digit changes =", changed)

n = int(input("Enter any number: "))

checks_digit_in_number_square(n, 3)
reversed_number(n)
changes_first_and_last_digits(n)
