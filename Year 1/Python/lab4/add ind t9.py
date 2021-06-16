import math

firstSide = float(input("Enter the first side of the triangle: "))
secondSide = float(input("Enter the second side of the triangle: "))
betweenCorner = float(input("Enter the corner between sides: "))

radians = math.radians(betweenCorner)
cosine = math.cos(radians)
thirdSide = (firstSide**2 + secondSide**2 - 2*firstSide*secondSide*cosine)
thirdSide = math.sqrt(thirdSide)

p = (firstSide+secondSide+thirdSide)/2
S = math.sqrt(p*(p-firstSide)*(p-secondSide)*(p-thirdSide))

print("Third side =", thirdSide, "S =",  S,)




