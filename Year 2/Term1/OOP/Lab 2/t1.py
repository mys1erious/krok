'''
First task from oop lab 2

Author: Eugene Lavrinovych
'''


class Date:
    """
    Represents date object --> (day, month, year)
    """
    def __init__(self, day, month, year):
        """
        Initialize date object
        :param day: int
        :param month: int
        :param year: int
        """
        self._day = day
        self._month = month
        self._year = year

    @staticmethod
    def type_check(name, value):
        """
        Checks type and range of given date for Date class.

        Raises an error if given value doesnt fit type or 'name' date range.
        Range for day -> 1, 31
        Range for month -> 1, 12
        Range for year -> 1, 9999

        :param name: date name (str)
        :param value: int, None
        :return: None
        """
        start = 1
        end = 0
        if name == 'day':
            end = 32
        elif name == 'month':
            end = 13
        elif name == 'year':
            end = 9999
        else:
            raise TypeError(f'Wrong name')

        if not isinstance(value, (int, type(None))):
            raise TypeError(f'{name} must be in int format.\nYour input: type={type(value)}')
        elif value not in range(start, end) and value is not None:
            raise ValueError(f'{name} must be in range {start} - {end}.\nYour input: {value}')

    @property
    def day(self):
        """
        day 1-31
        :return: day
        """
        return self._day

    @property
    def month(self):
        """
        month 1-12
        :return: month
        """
        return self._month

    @property
    def year(self):
        """
        year 1-9999
        :return: year
        """
        return self._year

    @day.setter
    def day(self, value):
        """
        Sets new day
        :param value: new day
        :return: None
        """
        self.type_check('day', value)
        self._day = value

    @month.setter
    def month(self, value):
        """
        Sets new month
        :param value: new month to set
        :return: None
        """
        self.type_check('month', value)
        self._month = value

    @year.setter
    def year(self, value):
        """
        Sets new year
        :param year: new year to set
        :return: None
        """
        self.type_check('year', value)
        self._year = value

    @property
    def fulldate(self):
        """
        Tuple (day, month, year)
        :return: tuple
        """
        return self.day, self.month, self.year

    @fulldate.setter
    def fulldate(self, *args):
        """
        Sets new day, month, year
        :param args: 3 args to set new date(day, month, year)
        :return: None
        """
        args = args[0]
        if len(args) != 3:
            raise ValueError('You have to input 3 int`s (day, month, year)')

        self.type_check('day', args[0])
        self.day = args[0]
        self.type_check('month', args[1])
        self.month = args[1]
        self.type_check('year', args[2])
        self.year = args[2]

    @fulldate.deleter
    def fulldate(self):
        """
        Deletes(sets to None) date
        :return: None
        """
        self._day = None
        self._month = None
        self._year = None

    def __str__(self):
        """
        :return: date in format day/month/year
        """
        return f'{self.day}/{self.month}/{self.year}'


if __name__ == '__main__':

    dt = Date(22, 8, 2020)
    print('1. Making instance', dt, dt.fulldate, dt.day, sep='\n')

    dt.fulldate = 15, 2, 2023
    print('2. Changing date with .fulldate', dt, dt.fulldate, dt.day, sep='\n')

    del dt.fulldate
    print('3. Deleting date', dt, dt.day, sep='\n')
