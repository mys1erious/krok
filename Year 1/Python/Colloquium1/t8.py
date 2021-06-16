age = int(input("Введите свой возраст: "))
if age>0 and age<=100:
    if age == 1:
        print(f"Вам {age} год ")
    elif age//10 != 1 and age%10 in range(1, 5):
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")