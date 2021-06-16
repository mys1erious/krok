from enum import Enum

class Season(Enum):
    winter = 1
    spring = 2
    summer = 3
    autumn = 4
x, y = Season(1), Season(4)

#A
'''
x==y - False 
x!=y - True 
x is y - False 
x in Season - True 
y.name == autumn - True 
x.value != 4 - True 
'''

#B
'''
for i in range(Season.autumn.value): pass
for i in range(Season.winter.value, Season.autumn.value): pass

Допустимы, в первом случаее Season.autumn.value = 4, цикл выполнится 4 раз
Во втором случаее Season.winter.value = 1, Season.autumn.value = 4, цикл выпонился 3 раза
(value выводит число, которые принадлежит заданому элементу в Enum типе)
'''

#V
'''
x = Season(int(input())) - допустим, считывает номер элемента
x = Season[input()] - допустим, считывает название элемента
print(x)
'''