days = range(1, 32)
months = range(1, 13)
years = range(1901, 2016)
d, m, y = int(input('day: ')),\
int(input('month: ')),\
int(input('year: '))

if d in days and m in months and y in years:
    if d == days[-1]:
        d = 1
        m += 1
        if m > months[-1]:
            m = 1
            y += 1
    else:
        d += 1
    print(d, m, y)
else:
    print('Ur date not in range')
