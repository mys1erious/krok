import multiprocessing
from math import sqrt
import concurrent.futures
from timeit import default_timer as timer


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    limit = int(sqrt(x) + 1)
    for i in range(3, limit, 2):
        if x % i == 0:
            return False

    return True


def concurrent_solve(n_workers):
    print('Num of workers:', n_workers)

    start = timer()
    res = []

    with concurrent.futures.ProcessPoolExecutor(
        max_workers=n_workers
    ) as executor:
        futures = [executor.submit(is_prime, i) for i in input]
        completed_futures = concurrent.futures.as_completed(futures)

        sub_start = timer()

        for i, future in enumerate(completed_futures):
            if future.result():
                res.append(future.result())

        sub_duration = timer() - sub_start

    duration = timer() - start
    print(f'Sub took: {sub_duration:.4f} seconds')
    print(f'Took: {duration:.4f} seconds')


if __name__ == '__main__':
    input = [i for i in range(10**13, 10**13 + 1000)]
    for n_workers in range(1, multiprocessing.cpu_count() + 1):
        concurrent_solve(n_workers)
        print('_'*20)
