def digit_amout(num):
    amount = 0
    if num > 0 and num <= 100:
        while True:
            num = num // 10
            amount += 1
            if num <= 0:
                break
    return amount

def digit_sum(num):
    if num > 0 and num <= 100:
        amount = (num//100 + num//10%10 + num%10)
    return amount

def first__digit(num):
    if num > 0 and num <= 100:
        while num >= 10:
            num = num // 10
    return num

def penultimate_digit(num):
    if num>=10 and num <=100:
        while num>99:
            num = num % 100
    num = num//10
    return num

number = int(input("Enter number from 0 to 100: "))
amount = digit_amout(number)
digSum = digit_sum(number)
firstDig = first__digit(number)
lastDig = number%10
penultimate = penultimate_digit(number)

print(f"Amount of digits = {amount}",
      f"Sum of digits = {digSum}",
      f"First digit of number = {firstDig}",
      f"Last digit of number = {lastDig}",
      f"Penultimate digit of number = {penultimate}",
      sep='\n')