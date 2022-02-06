second = int(input("Enter seconds: "))

minute = second/60
hour = int(minute//60)
minute = int(minute%60)


print("Hours =", hour, "Minutes =", minute)