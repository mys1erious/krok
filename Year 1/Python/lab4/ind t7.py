
number = int(input("Enter day of the year (max365): "))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if number >= 1 and number <= 365:
    intnum = number%7
    print(week[intnum])
