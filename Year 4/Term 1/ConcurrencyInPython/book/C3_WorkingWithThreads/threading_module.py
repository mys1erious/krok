import threading
from math import sqrt


def is_prime(x):
    if x < 2:
        print(f'{x} is not a prime.')
        return False
    elif x == 2:
        print(f'{x} is a prime.')
        return True
    elif x % 2 == 0:
        print(f'{x} is not a prime.')
        return False

    limit = int(sqrt(x) + 1)
    for i in range(3, limit, 2):
        if x % i == 0:
            print(f'{x} is not a prime.')
            return False

    print(f'{x} is a prime.')
    return True


class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        print(f'Starting processing {self.x}...')
        is_prime(self.x)


if __name__ == '__main__':
    my_input = [2, 193, 323, 1327, 433785907]
    threads = []

    for x in my_input:
        temp_thread = MyThread(x)
        temp_thread.start()
        threads.append(temp_thread)

    for thread in threads:
        thread.join()

    print('Finished')

