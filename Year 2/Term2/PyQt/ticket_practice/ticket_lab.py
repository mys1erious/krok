'''
First task from oop lab 4

Author: Eugene Lavrinovych
'''


import uuid
import datetime


class Event:
    '''
    Represents Event class
    '''

    def __init__(self, event_date=datetime.datetime.today().date()):
        '''
        Initialize event object

        :param event_date: datetime.date
        '''
        if not isinstance(event_date, datetime.date):
            raise TypeError(f'{type(event_date).__name__} object cant be interpreted as event date')
        self.event_date = event_date
        self.today = datetime.datetime.today().date()
        self.tickets = []

    def buy_ticket(self, number=None, student=False):
        '''
        Buys a ticket depending on date and student status

        :param number: ticket number (str, uuid.UUID)
        :param student: bool
        :return: ticket
        '''

        if not isinstance(student, bool):
            raise TypeError(f'{type(student).__name__} cant be interpreted as student status')

        if student and (self.event_date - self.today).days >= 10:
            t = StudentTicket(number)
        elif (self.event_date - self.today).days < 10:
            t = LateTicket(number)
        elif (self.event_date - self.today).days >= 60:
            t = AdvancedTicket(number)
        else:
            t = Ticket(number)

        for i in self.tickets:
            if t.number == i.number:
                raise ValueError('Cant be 2 tickets with same numbers')
        self.tickets.append(t)
        return t


class Ticket:
    '''
    Represents Ticket Class
    '''

    def __init__(self, number=None):
        '''
        Initialize Ticket object

        :param number: ticket number (str, uuid.UUID)
        '''
        if not isinstance(number, (str, uuid.UUID, type(None))):
            raise TypeError(f'{type(number).__name__} cant be interpreted as number of the ticket')

        self.uuid = uuid.uuid4()
        self._number = number
        self.price = 100

    @property
    def number(self):
        '''
        :return: ticket number
        '''
        if not self._number:
            return self.uuid
        else:
            return self._number

    def __str__(self):
        '''
        :return: Info about ticket
        '''
        return f'Number: {self.number}\nType: {self.__class__.__name__}\nPrice: {self.price}\n'


class AdvancedTicket(Ticket):
    '''
    Represents Advanced Ticket

    discount 40% of the regular ticket price
    '''
    def __init__(self, number):
        super().__init__(number)
        self.price *= 0.6


class StudentTicket(Ticket):
    '''
    Represents Student Ticket

    discount 40% of the regular ticket price
    '''
    def __init__(self, number):
        super().__init__(number)
        self.price *= 0.5


class LateTicket(Ticket):
    '''
    Represents Late Ticket

    additional 10% to the regular ticket price
    '''
    def __init__(self, number):
        super().__init__(number)
        self.price *= 1.1


if __name__ == '__main__':
    ev = Event(datetime.datetime(2021, 11, 3).date())

    t1 = ev.buy_ticket()
    #t2 = ev.buy_ticket(student=True)
    #t3 = ev.buy_ticket('123')

    for i in range(len(ev.tickets)):
        print(f'{i} {ev.tickets[i]} {id(ev.tickets[i])}')
    for i in range(len(ev.tickets)):
        print(f'{i} {ev.tickets[i]} {id(ev.tickets[i])}')

    #print('t1:\n', t1.price, sep='')
    #print(t1)