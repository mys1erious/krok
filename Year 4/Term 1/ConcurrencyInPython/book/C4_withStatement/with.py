from threading import Lock


my_lock = Lock()


def get_data_from_file_v1(filename):
    with my_lock, open(filename, 'r') as f:
        data.append(f.read())


data = []


try:
    get_data_from_file_v1('output2/sample0.txt')
except FileNotFoundError:
    print('Encountered an exception...')

my_lock.acquire()
print('Lock acquired.')
