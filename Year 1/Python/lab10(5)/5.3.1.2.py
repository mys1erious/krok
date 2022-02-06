import random
import time
import os
import psutil
from inspect import signature


def inf(type, matrix, size=0, n=0):
    print(type.__name__+':')

    sig = signature(type)
    sig_len = len(sig.parameters)

    start_time = time.time()
    if sig_len == 1:
        ans = type(matrix)
    elif sig_len == 2:
        ans = type(matrix, n)
    elif sig_len == 3:
        ans = type(matrix, size)
    elif sig_len == 4:
        ans = type(matrix, size, n)
    print("Execution time:", "%s seconds" % (time.time() - start_time))

    process = psutil.Process(os.getpid())
    print('Memory usage: ', process.memory_info().rss)

    return ans


def create_matrix(size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(input(f"Enter {i} {j} element if matrix: "))
    return matrix


def iterative_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum += matrix[i][j]
    return sum


def recursive_sum(matrix, size, i=0):
    if size == 0:
        i+=1
        size = len(matrix)
    if i == len(matrix):
        return 0
    return recursive_sum(matrix, size-1, i) + matrix[i][size-1]


def iterative_product(matrix):
    sum = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum *= matrix[i][j]
    return sum


def recursive_product(matrix, size, i=0):
    if size == 0:
        i+=1
        size = len(matrix)
    if i == len(matrix):
        return 1
    return recursive_product(matrix, size-1, i) * matrix[i][size-1]


def iterative_search(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if n == matrix[i][j]:
                return [i, j]
    return -1


def recursive_search(matrix, size, n, i=0):
    if size == 0:
        i += 1
        size = len(matrix)
    if i == len(matrix):
        return -1
    if matrix[i][size-1] == n:
        return [i, size-1]
    return recursive_search(matrix, size-1, n, i)


try:
    size = int(input("Enter square matrix size: "))
    check = input("Enter /random if u wanna create random matrix\n"
                  "   or /create if u wanna create matrix with ur own values\n")

    if check == '/create':
        arr = create_matrix(size)
    elif check == '/random':
        arr = [[random.randint(1, 100) for i in range(size)]for j in range(size)]

    print(arr)
    num = int(input('Enter value that u wanna find: \n'))

    print(inf(iterative_sum, arr))
    print(inf(recursive_sum, arr, len(arr)), '\n')

    print(inf(iterative_product, arr))
    print(inf(recursive_product, arr, len(arr)), '\n')

    print(inf(iterative_search, arr, n=num))
    print(inf(recursive_search, arr, len(arr), num))

except ValueError:
    print('Size of matrix can only be given as an integer')
except NameError:
    print('Incorrect input')

