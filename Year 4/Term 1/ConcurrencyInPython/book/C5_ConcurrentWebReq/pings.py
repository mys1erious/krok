import threading
import requests
import time


URLS = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]
UPDATE_INTERVAL = 0.01


def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.text}')


def sequential_pings():
    start = time.time()
    for url in URLS:
        ping(url)
    print(f'Sequential time: {time.time() - start}')


class Thread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.res = f'{self.url}: Custom timeout'

    def run(self):
        res = requests.get(self.url)
        self.res = f'{self.url}: {res.text}'


def process_requests(threads, timeout=5):
    def alive_count():
        alive = [1 if thread.is_alive() else 0 for thread in threads]
        return sum(alive)

    while alive_count() > 0 and timeout > 0:
        timeout -= UPDATE_INTERVAL
        time.sleep(UPDATE_INTERVAL)

    for thread in threads:
        print(thread.res)


def parallel_pings():
    threads = []

    start = time.time()
    for url in URLS:
        thread = Thread(url)
        threads.append(thread)
        thread.setDaemon(True)
        thread.start()
    process_requests(threads)

    print(f'Parallel time: {time.time() - start}')


if __name__ == '__main__':
    # sequential_pings()
    parallel_pings()
