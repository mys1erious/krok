hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
second = int(input("Enter second: "))

oneHourDeg = 30
oneMinDeg = 0.5
oneSecDeg = 0.5/60

if hour in range(0, 12) and minute in range(0, 60) and second in range(0, 60):
    corner = hour*oneHourDeg + minute*oneMinDeg + second*oneSecDeg
    print("Corner between the beginning of the day and entered time is:", corner)
else:
    print("Cant identify a corner")

