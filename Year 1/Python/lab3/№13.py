a, b, b, c, a = input(), float(input()), input(),\
int(input()), float(input())
print(a, b, c, sep=';')
'''
Вывод:  -1.0;5;10
 Потому что последнее присвоенное число для:
a было -1 типа float
b было 5тип str по умолч.
c единственное 10 типа int
'''