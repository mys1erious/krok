import multiprocessing


class Worker:
    def __init__(self, x):
        self.x = x

    def process(self):
        pname = multiprocessing.current_process().name
        print(f'Starting process {pname} for number {self.x}')


def work(q):
    worker = q.get()
    worker.process()


if __name__ == '__main__':
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=work, args=(q,))
    p.start()

    q.put(Worker(10))
    q.close()
    q.join_thread()
    p.join()

    print('Done')
