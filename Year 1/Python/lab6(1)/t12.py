from enum import Enum

class measure(Enum):
    millimetre = -3
    centimetre = -2
    decimetre = -1
    metre = 0
    kilometre = 3

try:
    x = float(input('length: '))
    p = measure[input('measure: ')]

    answ = (x*(10**p.value))
    print(f'{x} {p.name}s = {answ} metres')
except ValueError:
    print('Wrong length')
except KeyError:
    print('Wrong measure')


#ValueError, KeyError