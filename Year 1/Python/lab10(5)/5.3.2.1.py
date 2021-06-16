import time
from functools import lru_cache
import os
import psutil

def inf(type, n, m):
    print(type.__name__+':')

    start_time = time.time()
    ans = type(n, m)
    print("Execution time:", "%s seconds" % (time.time() - start_time))

    process = psutil.Process(os.getpid())
    print('Memory usage: ', process.memory_info().rss)
    return ans


@lru_cache()
def recursive_ackermann(n, m):
    if n == 0:
        return m+1
    elif n > 0 and m == 0:
        return recursive_ackermann(n-1, 1)
    elif n > 0 and m > 0:
        return recursive_ackermann(n-1, recursive_ackermann(n, m-1))


def iterative_ackermann(n, m):
    stack = []
    stack.append(n)

    while stack:
        n = stack.pop()
        if n == 0:
            m += 1
        elif n > 0 and m == 0:
            m = 1
            stack.append(n-1)
        elif n > 0 and m > 0:
            m -= 1
            stack.append(n-1)
            stack.append(n)
    return m


try:
    n = int(input("n: "))
    m = int(input("m: "))
    if n > 0 and m > 0:
        print(inf(recursive_ackermann, n, m))
        print(inf(iterative_ackermann, n, m))

    else:
        print('n, m must be non-negative integers')
except ValueError:
    print('n, m must be non-negative integers')
except RecursionError:
    print('Too big to calculate')
