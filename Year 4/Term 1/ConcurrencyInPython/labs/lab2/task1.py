"""
Написати Python-скрипт, який зчитує цілі числа,
    що вводяться користувачем, і поміщає їх в кінець списку.
При цьому кожні 30 секунд список сортується по зростанню.
При введенні порожнього рядка Python-скрипт повинен вивести на екран
    поточний стан списку і завершити роботу.
"""


import threading
import time


class SortThread(threading.Thread):
    def __init__(self, array, wait=30):
        super().__init__()
        self.array = array
        self.wait = wait
        self.is_active = True
        self.prev_time = time.time()

    def run(self):
        while True:
            if not self.is_active:
                break

            cur_time = time.time()
            if cur_time - self.prev_time >= self.wait:
                array.sort()
                self.prev_time = cur_time
                print(f'\nArray has been sorted: {array}')

            time.sleep(0.2)


if __name__ == '__main__':
    array = []
    wait_time = 5

    sort_thread = SortThread(array, wait_time)
    sort_thread.start()

    while True:
        value = input('Enter new integer value: ')

        if not value:
            sort_thread.is_active = False
            sort_thread.join()
            print(array)
            break
        elif not value.lstrip('-').isdigit():
            print('Only integers allowed')
            continue

        array.append(int(value))
