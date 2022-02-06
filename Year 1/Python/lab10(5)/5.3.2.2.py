from inspect import signature
import time
from functools import lru_cache
import os
import psutil

def inf(type, n, k=0):
    print(type.__name__+':')

    sig = signature(type)
    sig_len = len(sig.parameters)

    start_time = time.time()
    if sig_len == 1:
        ans = type(n)
    elif sig_len == 2:
        ans = type(n, k)
    print("Execution time:", "%s seconds" % (time.time() - start_time))

    process = psutil.Process(os.getpid())
    print('Memory usage: ', process.memory_info().rss)
    return ans


@lru_cache()
def recursive_partition(n, k):
    if k == 0:
        if n == 0:
            return 1
        return 0
    if k <= n:
        return recursive_partition(n, k-1) + recursive_partition(n-k, k)
    elif k > n:
        return recursive_partition(n, n)


def iterative_partition(n):
    n += 1
    matrix = [[0] * n for i in range(n)]

    for i in range(0, n):
        matrix[i][0] = 1

    for i in range(1, n):
        for j in range(1, n):
            if i > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                without_term = matrix[i-1][j]
                with_term = matrix[i][j - i]

                matrix[i][j] = without_term + with_term
    n -= 1

    return matrix[n][n]



n = int(input("n: "))

print(inf(iterative_partition, n))
print(inf(recursive_partition, n, n))

