writtenNum = int(input("Enter three-digit number: "))
sumOfNums = (writtenNum//100 + (writtenNum%100//10) + writtenNum%10)
print("Sum of ur numbers is: ", sumOfNums)