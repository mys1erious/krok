num = int(input("Enter 3-digit num: "))
one = num%10
two = num%100//10
three = num//100
print(one, two, three, sep = '')