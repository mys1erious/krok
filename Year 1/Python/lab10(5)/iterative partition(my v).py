import sys
from functools import lru_cache


def iterative_splitting(n):
    i = n-1
    main_set = set()

    while i in range(n, 0, -1):
        main = []
        k = n-i
        if k > i:
            k = i

        main.insert(0, i)
        while k != 0 and sum(main) < n:
            if sum(main)+k <= n:
                main.append(k)
            else:
                main.append(n-sum(main))


        j = len(main)-1
        t = 1
        while j > 0:

            main_tup = tuple(main)
            main_set.add(main_tup)

            while main[t] != 1:
                pass

            else:
                j -= 1

        i-=1
    print(main_set)
    print(len(main_set))