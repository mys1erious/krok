import time
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


def iterative_nod(n, m):

    while(m):
        n, m = m, n%m
    return n


def recursive_nod(n, m):

    if m == 0:
        return n
    else:
        r = n % m
        return recursive_nod(m, r)


try:
    n = int(input("n: "))
    m = int(input("m: "))
    if n == 0 or m == 0:
        raise ZeroDivisionError('U cant find nod of 0')
except ValueError:
    print('Numbers must me integers')


print(inf(iterative_nod, n, m), '\n')
print(inf(recursive_nod, n, m))
