import threading
import queue
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Starting thread {self.name}')
        process_queue()
        print(f'Finished thread {self.name}')


def process_queue():
    while True:
        try: x = my_queue.get(block=False)
        except queue.Empty: return
        else:
            print_factors(x)

        time.sleep(1)


def print_factors(x):
    res_str = f'Positive factors of {x} are: '
    for i in range(1, x+1):
        if x % i == 0:
            res_str += str(i) + ' '
    res_str += '\n' + '_'*20

    print(res_str)


if __name__ == '__main__':
    input_ = [1, 10, 4, 3]
    my_queue = queue.Queue()

    for x in input_:
        my_queue.put(x)

    thread1 = MyThread('A')
    thread2 = MyThread('B')
    thread3 = MyThread('C')

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print('Finished')
