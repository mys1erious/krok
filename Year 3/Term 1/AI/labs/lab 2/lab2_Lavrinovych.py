import numpy as np


def F(S):
    if S >= 0: return 1
    return 0


def delta_func(y, t):
    if y == t: return 0
    elif y == 0 and t == 1: return 1
    elif y == 1 and t == 0: return -1


def w_adjust(w_prev, delta, x):
    return w_prev + delta * x


def neuron_training(X, T, W, iter_num=100):
    i = 1
    while True:
        if i == len(X):
            i = 0

        prev_W = W

        S = np.dot(X[i], prev_W)
        y = F(S)
        delta = delta_func(y, T[i])

        W = w_adjust(prev_W, delta, X[i])

        if np.array_equal(W, prev_W):
            return W

        if iter_num == 0:
            return -1

        iter_num -= 1
        i += 1


# Задание: Обучение распознавания 2-х образов с помощью искусственного нейрона


# Образцы
x1 = np.array([[1, 1, 1],
               [1, 0, 1],
               [1, 0, 1]])
t1 = 1

x2 = np.array([[1, 1, 1],
               [0, 1, 0],
               [0, 1, 0]])
t2 = 0


# Преобразуем матрицы образцов в векторы
x1 = x1.flatten()
x2 = x2.flatten()


# Создаем 1 массив из x-ов и t
X = np.array([x1, x2])
T = np.array([t1, t2])


# Инициализируем первую W нулями
W = np.zeros(len(x1))


# Проводим обучение, пока W не перестанет изменятся
final_W = neuron_training(X, T, W)

print("Final W: ", final_W)


# Для проверки полученного результата 'испортим' входные образцы и подадим их на вход
x1 = np.array([[1, 1, 0],
               [1, 0, 1],
               [1, 0, 1]])
x2 = np.array([[1, 1, 1],
               [0, 0, 0],
               [0, 1, 0]])
x1 = x1.flatten()
x2 = x2.flatten()


# x1_y = 1, первый символ распознан как 'П'
# x2_y = 0, второй символ распознан как 'Т'
x1_y = F(np.dot(x1, final_W))
x2_y = F(np.dot(x2, final_W))

print("x1_y: ", x1_y)
print("x2_y: ", x2_y)
