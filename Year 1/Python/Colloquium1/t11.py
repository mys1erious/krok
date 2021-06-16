n = int(input("Enter first number: "))
m = int(input("Enter the amount of last digits in first number: "))
mCopy = m
if n > 0 and m > 0:
    toMin = n // 10**m
    toMin = toMin * 10**m
    lastDigs = n - toMin
    summ = 0
    while m > 0:
        m -= 1
        a1 = lastDigs // 10
        a2 = a1 * 10
        a3 = lastDigs - a2
        summ += a3
        lastDigs = lastDigs // 10
print(f"Sum of {mCopy} last digits of first number =", summ)
