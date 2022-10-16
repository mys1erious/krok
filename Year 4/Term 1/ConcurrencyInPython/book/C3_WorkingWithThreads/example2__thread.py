from math import sqrt
import _thread as thread


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


if __name__ == '__main__':
    my_input = [2, 193, 323, 1327, 433785907]

    for x in my_input:
        thread.start_new_thread(is_prime, (x, ))

    a = input('quit:\n')
