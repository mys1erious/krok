import threading
import time


def thread_a():
    print('Thread A is starting...')

    print('Thread A is performing some calculation...')
    time.sleep(2)

    print('Thread A is performing some calculation...')
    time.sleep(2)


def thread_b():
    print('Thread B is starting...')

    print('Thread B is performing some calculation...')
    time.sleep(5)

    print('Thread B is performing some calculation...')
    time.sleep(5)


if __name__ == '__main__':
    start = time.time()

    thread1 = threading.Thread(target=thread_a)
    thread2 = threading.Thread(target=thread_b)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Took {time.time()-start}')
    print('Finished.')
