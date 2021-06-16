x = float(input("Enter x number: "))
y = float(input("Enter y number: "))
z = float(input("Enter c number: "))

kit = [x, y, z]
kit.sort()

if x!=y!=z and x+y+z < 1:
    kit[0] = (kit[1] + kit[2])/2
    print(kit[0])
else:
    least = min(x, y)
    maximum = max(x, y)
    least = maximum + z
    print(least)