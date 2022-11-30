import time
import threading
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt


class LockedCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, x):
        with self.lock:
            new_value = self.value + x
            time.sleep(0.001)
            self.value = new_value

    def get_value(self):
        with self.lock:
            value = self.value
        return value


class ApproximateCounter:
    def __init__(self, global_counter):
        self.value = 0
        self.lock = threading.Lock()
        self.global_counter = global_counter
        self.threshold = 10

    def increment(self, x):
        with self.lock:
            new_value = self.value + x
            time.sleep(0.001)
            self.value = new_value

            if self.value > self.threshold:
                self.global_counter.increment(self.value)
                self.value = 0

    def get_value(self):
        with self.lock:
            value = self.value
        return value


def main_locked():
    n_threads = []
    times = []

    for n_workers in range(1, 11):
        n_threads.append(n_workers)

        counter = LockedCounter()

        start = time.time()
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            executor.map(counter.increment, [1 for _ in range(100*n_workers)])
        times.append(time.time() - start)

        print(f'Number of threads: {n_workers}')
        print(f'Final counter: {counter.get_value()}')
        print('-'*40)

    plt.plot(n_threads, times)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in seconds')
    plt.ylim(-0.25, 2)
    plt.show()


def main_approx():
    def thread_increment(counter):
        counter.increment(1)

    n_threads = []
    times = []

    for n_workers in range(1, 11):
        n_threads.append(n_workers)

        global_counter = LockedCounter()

        start = time.time()
        local_counters = [ApproximateCounter(global_counter) for _ in range(n_workers)]
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            executor.map(thread_increment, local_counters)
        times.append(time.time() - start)

        print(f'Number of threads: {n_workers}')
        print(f'Final counter: {global_counter.get_value()}')
        print('-' * 40)

    plt.plot(n_threads, times)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in seconds')
    plt.ylim(-0.25, 2)
    plt.show()


if __name__ == '__main__':
    main_locked()
    main_approx()
