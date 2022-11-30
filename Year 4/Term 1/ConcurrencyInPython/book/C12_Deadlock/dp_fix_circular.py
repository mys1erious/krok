import threading


def philosopher(left, right):
    while True:
        with Acquire(left, right):
            print(f'Philosopher at {threading.currentThread()} is eating.')


class Acquire:
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False


if __name__ == '__main__':
    N_FORKS = 5
    forks = [threading.Lock() for n in range(N_FORKS)]

    phils = [threading.Thread(
        target=philosopher,
        args=(forks[n], forks[(n+1) % N_FORKS])
    ) for n in range(N_FORKS)]

    for p in phils:
        p.start()
