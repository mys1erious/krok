from enum import Enum

class colors(Enum):
    green = 1
    red = 2
    yellow = 3
    white = 4
    black = 5

class animal_names(Enum):
    rat = 1
    cow = 2
    tiger = 3
    bunny = 4
    dragon = 5
    snake = 6
    horse = 7
    sheep = 8
    ape = 9
    chicken = 10
    dog = 11
    pig = 12

yearNow = int(input("Enter the year of our era: "))
japCyc = range(1, 6)
namesCyc = range(1, 13)
test = []

for i in japCyc:
    color = colors(i)
    for j in namesCyc:
        animal = animal_names(j)
        name = f'{color.name} {animal.name}'
        test.append(name)

realYear = (yearNow%60)-4

print('Entered year translated to ancient japanese calender :', test[realYear])