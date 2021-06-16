'''
Computational Mathematics
Lab №2
# 1

Author: Eugene Lavrinovych
'''


import math


def double_factorial(n):
    f = 1
    start = 1
    if n >= 1:
        if n % 2 == 0:
            start+=1
        for i in range(start, n+1, 2):
            f *= i
    return f


def arccos(x, e=1e-8):
    if not -1 <= x <= 1:
        raise ValueError('Arccos(x) can only be defined in range -1, 1')

    z = (1-x)/4
    u = 1
    s = u

    for k in range(1, 1000):
        if not abs(u) < e:
            u = (double_factorial(2*k-1) / math.factorial(k)) * (z**k / (2*k+1))
            s += u
            print(f'k = {k}    u = {u:.8f}    sum = {s:.8f}')
        else:
            s *= math.sqrt(2-2*x)
            print(f'arccos({x}) = {s}')
            return s


x = float(input('x-> '))
e = float(input('e-> '))

acos1 = arccos(x, e)
acos2 = math.acos(x)
dif = abs(acos1-acos2)
print('\nMy function:', acos1)
print('Built-in function:', acos2)
print('Their difference:', dif)
