"""
Написати Python-програму, яка моделює роботу автостоянки,
використовуючи багатопоточність - машина рухається по автостоянці,
поки не виявляє перше порожнє місце, стає на нього,
знаходиться на місці довільний час,
виїжджає зі стоянки і повертається на неї через деякий час;
якщо місць на стоянці немає, машина виїжджає.
"""


import random as rnd
import time
import threading
import uuid


class Car:
    def __init__(self):
        self.id = uuid.uuid4()
        self.pos = 0

    def __str__(self):
        return f'({self.id})'

    def __repr__(self):
        return f'({self.id})'


class ParkingSpot:
    def __init__(self, pos):
        self.taken = False
        self.pos = pos
        self.car = None

    def __str__(self):
        return f'(pos: {self.pos}, taken: {self.taken})'

    def __repr__(self):
        return f'(pos: {self.pos}, taken: {self.taken}, car: {self.car})'


class ParkingLot:
    def __init__(self):
        self.max_spots = 5
        self.entry_pos = 0
        self.exit_pos = self.max_spots + 1

        self.parking_spots = [
            ParkingSpot(i)
            for i in range(1, self.max_spots+1)
        ]

    def car_enter(self, car):
        car.pos = self.entry_pos
        print(f'car: {car} entered the parking lot')

    def take_spot_if_free(self, car):
        # Taking the first available spot
        for spot in self.parking_spots:
            if not spot.taken:
                car.pos = spot.pos
                spot.taken = True
                spot.car = car
                print(f'car: {car} took spot: {spot}')
                return True

        # Leaving the parking if theres no free spot left
        car.pos = self.exit_pos
        print(f'parking has no free spots left for car: {car}')
        return False

    def leave_spot(self, car):
        for spot in self.parking_spots:
            if spot.car and spot.car.id == car.id:
                spot.taken = False
                spot.car = None
                break

        car.pos = self.exit_pos
        print(f'car: {car} left the parking lot')

    def __str__(self):
        return f'({self.parking_spots})'


class CarThread(threading.Thread):
    def __init__(self, car, parking_lot):
        super().__init__()
        self.car = car
        self.parking_lot = parking_lot

    def run(self):
        self.imitate()

    def imitate(self):
        self.parking_lot.car_enter(self.car)
        parked = self.parking_lot.take_spot_if_free(self.car)
        if parked:
            time.sleep(rnd.uniform(0, 1))
            self.parking_lot.leave_spot(self.car)

        time.sleep(rnd.uniform(0, 1))

        self.parking_lot.car_enter(self.car)
        self.parking_lot.take_spot_if_free(self.car)


if __name__ == '__main__':
    parking_lot = ParkingLot()
    cars = [Car() for i in range(6)]

    threads = []

    for car in cars:
        thread = CarThread(car, parking_lot)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
