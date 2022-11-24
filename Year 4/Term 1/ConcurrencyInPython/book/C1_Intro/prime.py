import concurrent.futures
from math import sqrt
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


def sequential(nums):
    start = timer()
    res = []
    for num in nums:
        if is_prime(num):
            res.append(num)

    print('Sequential res: ', res)
    print(f'Took {(timer()-start):.2f} seconds')


# Faster, but result isnt in order
def concurrent_(nums):
    start = timer()
    res = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(is_prime, num) for num in nums]

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                res.append(nums[i])

    print('Concurrent res: ', res)
    print(f'Took {(timer()-start):.2f} seconds')


if __name__ == '__main__':
    nums = [i for i in range(10**13, 10**13 + 500)]
    sequential(nums)
    concurrent_(nums)
