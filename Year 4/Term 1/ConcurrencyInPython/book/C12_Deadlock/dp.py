# Dining Philosophers Problem
import threading


def philosopher(left, right):
    while True:
        with left:
            with right:
                print(f'Philosopher at {threading.currentThread()} is eating.')


if __name__ == '__main__':
    N_FORKS = 5
    forks = [threading.Lock() for n in range(N_FORKS)]

    phils = [threading.Thread(
        target=philosopher,
        args=(forks[n], forks[(n+1) % N_FORKS])
    ) for n in range(N_FORKS)]

    for p in phils:
        p.start()
