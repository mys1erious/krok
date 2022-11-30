import time
import threading
from random import choice
from copy import deepcopy


class Network:
    def __init__(self, primary_key, primary_value):
        self.primary_key = primary_key
        self.data = {primary_key: primary_value}

    def __str__(self):
        res = '{\n'
        for key in self.data:
            res += f'\t{key}: {self.data[key]};\n'
        return res + '}'

    def add_node(self, key, value):
        if key not in self.data:
            self.data[key] = value
            return True
        return False

    # precondition: the object has more than one node left
    def refresh_primary(self):
        del self.data[self.primary_key]
        self.primary_key = choice(list(self.data))

    def get_primary_value(self):
        # RCU solution
        copy_network = deepcopy(self)

        primary_key = copy_network.primary_key
        time.sleep(1)
        return copy_network.data[primary_key]


if __name__ == '__main__':
    def print_network_primary_value():
        global my_network
        print(f'Current primary value: {my_network.get_primary_value()}')

    my_network = Network('A', 1)
    print(f'Initial network: {my_network}')

    my_network.add_node('B', 1)
    my_network.add_node('C', 1)

    print(f'Full network: {my_network}')
    print()

    thread1 = threading.Thread(target=print_network_primary_value)
    thread2 = threading.Thread(target=my_network.refresh_primary)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Final network: {my_network}')
