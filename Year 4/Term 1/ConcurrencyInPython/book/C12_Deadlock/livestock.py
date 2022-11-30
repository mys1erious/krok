import threading
import time


class Spouse(threading.Thread):
    def __init__(self, name, partner):
        super().__init__()
        self.name = name
        self.partner = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print(f'{self.name} is hungry and wants to eat.')

            if self.partner.hungry:
                print(f'{self.name} is waiting for their partner to eat first...')
            else:
                with fork:
                    print(f'{self.name} has started eating.')
                    time.sleep(5)

                    print(f'{self.name} is now full.')
                    self.hungry = False


if __name__ == '__main__':
    fork = threading.Lock()

    partner1 = Spouse('P1', None)
    partner2 = Spouse('P2', partner1)
    partner1.partner = partner2

    partner1.start()
    partner2.start()

    partner1.join()
    partner2.join()

    print('Finished.')
