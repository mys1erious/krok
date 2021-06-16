'''
First task from oop lab 1

Author: Eugene Lavrinovych
'''


class Date:
    '''
    Represents date object --> (day, month, year)
    '''
    def __init__(self, day, month, year):
        '''
        Initialize date object
        :param day: int
        :param month: int
        :param year: int
        '''
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError(f'Data must be in int format')
        if day not in range(1, 32):
            raise ValueError(f'There`s no month with {day} days in it')
        if month not in range(1, 13):
            raise ValueError(f'There`s only 12 months in a year')

        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        '''
        :return: day
        '''
        return self.day

    def get_month(self):
        '''
        :return: month
        '''
        return self.month

    def get_year(self):
        '''
        :return: year
        '''
        return self.year

    def set_day(self, day):
        '''
        Sets new day
        :param day: new day to set
        :return: None
        '''
        if not isinstance(day, int):
            raise TypeError(f'Data must be in int format')
        if day not in range(1, 32):
            raise ValueError(f'There`s no month with {day} days in it')
        self.day = day

    def set_month(self, month):
        '''
        Sets new month
        :param month: new month to set
        :return: None
        '''
        if not isinstance(month, int):
            raise TypeError(f'Data must be in int format')
        if month not in range(1, 13):
            raise ValueError(f'There`s only 12 months in a year')
        self.month = month

    def set_year(self, year):
        '''
        Sets new year
        :param year: new year to set
        :return: None
        '''
        if not isinstance(year, int):
            raise TypeError(f'Data must be in int format')
        self.year = year

    def display_date(self):
        '''
        :return: date in format day/month/year
        '''
        return f'{self.day}/{self.month}/{self.year}'


t = Date(15, 12, 2004)
print('Date: ', t.display_date())

t.set_day(4)

print('Date after change:', t.display_date())
print('Day:', t.get_day())
