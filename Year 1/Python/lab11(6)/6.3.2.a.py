import random


def floyd_warshall(matrix):

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix


n = int(input("n: "))
matrix = [[random.randint(-1, n) for i in range(n)] for i in range(n)]
INF = float("inf")
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] < 1:
            matrix[i][j] = INF
    print(matrix[i])
print('\n\n')


test = floyd_warshall(matrix)
print("Shortest path from each town to each town: ")
for i in test:
    print(i)