'''
ННИИКТ, КН19, Лавринович Евгений

PS: Здравствуйте, увидел в группе информацию, что лабы можно сдавать не только в Excel, но и на Python, собственно,
    мне удобнее делать на Python, по этому сдаю в таком виде, я нахожусь на инд. форме обучения,
    и возможно что-то не так понял, если нужно сдавать только в Excel,
    отпишите пожалуйста в комментарии к оцениванию(или куда вам удобнее)
'''


import numpy as np


def threshold(y):
    for i in range(len(y)):
        if y[i] >= 0: y[i] = 1
        else: y[i] = -1

    return y


def hopfield_network(W, y, iter_num=50):
    while True:
        previous_y = y

        y = np.dot(W, y)
        y = threshold(y)

        if iter_num == 0: return -1
        iter_num -= 1

        if np.array_equal(y, previous_y):
            break

    return y


# Задание: Серед наявних трьох зразків розпізнати зіпсований зразок використовуючи мережу Гопфілда


# Образцы
x1 = np.array([[1, 1, 1],
               [-1, 1, -1],
               [-1, 1, -1]])

x2 = np.array([[1, 1, 1],
               [1, -1, 1],
               [1, -1, 1]])

x3 = np.array([[1, -1, 1],
               [1, 1, 1],
               [-1, -1, 1]])

y = np.array([[1, 1, -1],
              [1, -1, 1],
              [1, -1, 1]])


# Преобразуем матрицы образцов в векторы
x1 = x1.flatten()
x2 = x2.flatten()
x3 = x3.flatten()
y = y.flatten()


# Умножаем транспонированый вектор на обычный
x1_mult_matrix = x1 * x1.reshape(-1, 1)
x2_mult_matrix = x2 * x2.reshape(-1, 1)
x3_mult_matrix = x3 * x3.reshape(-1, 1)


# Плюсуем полученые матрицы и меняем диагональные значения на 0
W = x1_mult_matrix + x2_mult_matrix + x3_mult_matrix
np.fill_diagonal(W, 0)


# Умножаем W на вектор испорченного образца и пропускаем через функцию порога,
# повторяем до тех пор, пока вектор не перестанет изменятся
result = hopfield_network(W, y)


# В результате испорченный образец распознан как буква П
print(result.reshape(3, 3))
