import concurrent.futures
from timeit import default_timer as timer


def f(x):
    return x * x - x + 1


def sequential():
    start = timer()
    res = 3
    for i in range(20):
        res = f(res)

    print('Result is very large. Only printing the last 5 digits:', res % 100000)
    print(f'Sequential took: {(timer() - start):.2f} seconds.')


res = 3
def concurrent_():
    start = timer()

    def concurrent_f(x):
        global res
        res = f(res)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(concurrent_f, i) for i in range(20)]
        _ = concurrent.futures.as_completed(futures)

    print('Result is very large. Only printing the last 5 digits:', res % 100000)
    print(f'Concurrent took: {(timer() - start):.2f} seconds.')


if __name__ == '__main__':
    sequential()
    concurrent_()
