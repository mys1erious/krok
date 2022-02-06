from math import sqrt
fNum = int(input("Enter first num: "))
sNum = int(input("Enter second num: "))

arithmetMean = (fNum + sNum)/2

geometSum = (fNum * sNum)
geometMean = sqrt(geometSum)

print ("Arithmetic Mean: ", arithmetMean)
print ("Geometric Mean: ", geometMean)