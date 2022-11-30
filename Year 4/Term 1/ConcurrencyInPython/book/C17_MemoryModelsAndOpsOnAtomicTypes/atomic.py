import sys
import threading


sys.setswitchinterval(.000001)


def non_atomic_foo():
    global n
    n += 1


def non_atomic():
    global n

    threads = []
    for i in range(1000):
        thread = threading.Thread(target=non_atomic_foo)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final value: {n}.')


def atomic_foo():
    global lst
    lst.append(1)


# list.append is atomic - it guarantees that there is no race condition
def atomic():
    global lst

    threads = []
    for i in range(1000):
        thread = threading.Thread(target=atomic_foo)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final list len: {len(lst)}.')


if __name__ == '__main__':
    n = 0
    lst = []

    while True:
        non_atomic()
        atomic()
