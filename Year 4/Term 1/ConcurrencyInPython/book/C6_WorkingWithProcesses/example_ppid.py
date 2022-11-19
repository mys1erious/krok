from multiprocessing import Process, current_process
import time
import os


def print_info(title):
    print(title)

    if hasattr(os, 'getppid'):
        print(f'Parent process ID: {os.getppid()}')

    print(f'Current process ID: {os.getpid()}\n')


def f():
    print_info('Function f')

    pname = current_process().name
    print(f'Starting process: {pname}')
    time.sleep(1)
    print(f'Exiting process: {pname}')


if __name__ == '__main__':
    print_info('Main program')

    p = Process(target=f)
    p.start()
    p.join()

    print('Done')
