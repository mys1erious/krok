import time
from concurrent.futures import ThreadPoolExecutor


class LocklessCounter:
    def __init__(self):
        self.value = 0

    def increment(self, x):
        new_value = self.value + x
        time.sleep(0.001)
        self.value = new_value

    def get_value(self):
        return self.value


if __name__ == '__main__':
    counter = LocklessCounter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(counter.increment, [1 for _ in range(300)])

    print(f'Final counter: {counter.get_value()}')
