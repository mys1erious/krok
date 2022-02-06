from enum import Enum

class country(Enum):
    Laos = 1
    Bangladesh = 1

    Cuba = 2

    Germany = 3
    Monaco = 3
    Ukraine = 3

class continent(Enum):
    Asia = 1
    America = 2
    Europe = 3

try:
    s = country[input('country: ')]
    sVal = s.value
    print(continent(sVal))
except KeyError:
    print('This country doesnt exist at all, or still hasnt been added to this list')