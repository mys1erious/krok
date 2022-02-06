'''
Qt rework for ticket lab from previous term
'''

import sys
import datetime
import uuid

from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QMainWindow, QWidget, QPushButton, QHBoxLayout, \
    QScrollArea, QGridLayout, QLineEdit, QApplication, QInputDialog, QCheckBox, QErrorMessage
from PyQt5.QtCore import Qt


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
        self.price = int(self.price)


class TicketQT(QFrame):
    def __init__(self, ticket):
        super().__init__()

        self.ticket = ticket

        self.ui()

    def ui(self):
        width = 250
        height = 200

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedSize(width, height)
        self.setObjectName('ticket_frame')

        number = QLabel(f'{self.ticket.number}')
        number.setFixedHeight(30)
        number.setObjectName('number')

        ticket_type = QLabel(f'Type: {self.ticket.__class__.__name__}')
        ticket_type.setFixedHeight(30)
        ticket_type.setObjectName('ticket_type')

        price = QLabel(f'Price: {int(self.ticket.price)}')
        price.setFixedHeight(30)
        price.setObjectName('price')

        self.setStyleSheet('#ticket_frame {border: 1px solid black; background-color: white; }'
                           '#number, #ticket_type, #price {border: 1px solid black;}')

        self.layout().addWidget(number)
        self.layout().addWidget(ticket_type)
        self.layout().addWidget(price)


class TicketsList(QMainWindow):
    def __init__(self, event, parent=None):
        super().__init__(parent)

        self.event = event
        self.ui()

    def ui(self):

        self.setFixedSize(1200, 500)

        area = QScrollArea()
        container = QWidget()
        container.setLayout(QGridLayout())

        j = 0
        for i in range(len(self.event.tickets)):
            if i % 4 == 0:
                j += 1
            container.layout().addWidget(TicketQT(self.event.tickets[i]), j, i % 4)

        area.setWidgetResizable(True)
        area.setWidget(container)

        self.setCentralWidget(area)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui()
        self.show()

    def ui(self):
        container = QWidget()
        container.setLayout(QHBoxLayout())

        self.event = self.set_event_date()

        build_btn = QPushButton('Build ticket')
        build_btn.clicked.connect(self.ticket_builder)

        show_tickets_btn = QPushButton('Tickets list')
        show_tickets_btn.clicked.connect(self.tickets_list)

        container.layout().addWidget(build_btn)
        container.layout().addWidget(show_tickets_btn)
        self.setCentralWidget(container)

    def set_event_date(self):
        date, ok = QInputDialog.getText(self, 'Event date', 'Enter event date\nFormat: year month day')
        if ok and date:
            date = date.split(' ')
            date = list(map(int, date))
            event = Event(datetime.datetime(date[0], date[1], date[2]).date())
        else:
            event = Event()
        return event

    def ticket_builder(self):
        mw = QMainWindow(self)
        mw.setWindowTitle('Ticket builder')
        mw.setObjectName('main_window')
        mw.setFixedSize(250, 250)
        container = QWidget()
        container.setLayout(QHBoxLayout())

        builder = self.ticket_builder_view()

        container.layout().addWidget(builder)

        mw.setCentralWidget(container)
        mw.show()

    def ticket_builder_view(self):
        container = QFrame()
        container.setLayout(QVBoxLayout())
        container.layout().setAlignment(Qt.AlignTop)
        container.setFixedSize(200, 200)

        self.number_field = QLineEdit()
        self.number_field.setPlaceholderText('Ticket number: ')

        self.student = False
        student_field = QWidget()
        student_field.setLayout(QHBoxLayout())
        student_label = QLabel(f'Student:')
        student_label.setFixedWidth(150)
        self.student_checkbox = QCheckBox()
        self.student_checkbox.stateChanged.connect(self.student_status)
        student_field.layout().addWidget(student_label)
        student_field.layout().addWidget(self.student_checkbox)

        make_btn = QPushButton('Make ticket')
        make_btn.clicked.connect(lambda: self.event.buy_ticket(self.number_field.text(), self.student))

        container.layout().addWidget(self.number_field)
        container.layout().addWidget(student_field)
        container.layout().addWidget(make_btn)

        return container

    def student_status(self):
        if self.student_checkbox.isChecked():
            self.student = True
        else:
            self.student = False

    def tickets_list(self):
        tickets_list = TicketsList(self.event, self)
        tickets_list.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())