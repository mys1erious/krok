"""
Написати Python-скрипт, який імітує роботу виробничої лінії,
    що виготовляє гвинтики (widget).
Гвинтик збирається з деталі C і модуля, який, в свою чергу,
    складається з деталей A і B.
Для виготовлення деталі A потрібно 1 секунда,
    В - дві секунди, С - три секунди.
"""


from abc import ABC, abstractmethod
import time
import threading
import queue


class Widget(ABC):
    def __init__(self, id):
        self.id = id
        self.is_built = False

    @abstractmethod
    def build(self):
        self.is_built = True
        print(f'{self} has been made.')

    def __str__(self):
        return f'{type(self).__name__} {self.id}'


class Screw(Widget):
    def __init__(self, id):
        super().__init__(id)
        self.item_c = None
        self.module = None

    def build(self):
        item_c_thread = WidgetThread(ItemC(self.id))
        item_c_thread.start()

        module_thread = WidgetThread(Module(self.id))
        module_thread.start()

        item_c_thread.join()
        module_thread.join()

        self.item_c = item_c_thread.widget
        self.module = module_thread.widget

        super().build()

    def __repr__(self):
        return f'Screw {self.id}'


class ItemC(Widget):
    def build(self):
        time.sleep(3)
        super().build()


class Module(Widget):
    def __init__(self, id):
        super().__init__(id)
        self.item_a = None
        self.item_b = None

    def build(self):
        item_a_thread = WidgetThread(ItemA(self.id))
        item_a_thread.start()

        item_b_thread = WidgetThread(ItemB(self.id))
        item_b_thread.start()

        item_a_thread.join()
        item_b_thread.join()

        self.item_a = item_a_thread.widget
        self.item_b = item_b_thread.widget

        super().build()


class ItemA(Widget):
    def build(self):
        time.sleep(1)
        super().build()


class ItemB(Widget):
    def build(self):
        time.sleep(2)
        super().build()


class ScrewThread(threading.Thread):
    def __init__(self, q, screws):
        super().__init__()
        self.q = q
        self.screws = screws

    def run(self):
        process_screws_queue(self.q, self.screws)


def process_screws_queue(q, screws):
    while True:
        try: screw = q.get(block=False)
        except queue.Empty: return
        else:
            screw.build()
            screws.append(screw)


class WidgetThread(threading.Thread):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def run(self):
        self.widget.build()


def print_screw_info(screw):
    print(f'{screw}; '
          f'is_built={screw.is_built}; '
          f'item_c={screw.item_c.is_built}; '
          f'module={screw.module.is_built}')


def screw_production_line_concurrent(n):
    screws_queue = queue.Queue()
    screws = []
    threads = []

    for i in range(n):
        screws_queue.put(Screw(i))

    for i in range(n):
        thread = ScrewThread(screws_queue, screws)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('-'*100)
    for screw in screws:
        print_screw_info(screw)


if __name__ == '__main__':
    num_of_screws = 100

    start = time.time()
    screw_production_line_concurrent(num_of_screws)
    print('Time: ', time.time() - start)
