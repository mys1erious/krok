'''
First task from oop lab 5

Author: Eugene Lavrinovych
'''

import math


class Rational:
    '''
    Represents Rational number class.

    Rational(2, 4) will produce a rational number equivalent to 1/2.
    '''
    def __init__(self, numerator=0, denominator=None, reduce=True):
        '''
        Constructs Rational number.

        :param numerator: int
        :param denominator: int
        :param reduce: bool
        '''
        if denominator is None:
            if isinstance(numerator, int):
                self._numerator = numerator
                self._denominator = 1
        elif denominator == 0:
            raise ZeroDivisionError('Denominator cant be 0')
        else:
            if not isinstance(numerator, int):
                raise ValueError(f'{type(numerator)} cant be represented as numerator')
            elif not isinstance(denominator, int):
                raise ValueError(f'{type(denominator)} cant be represented as denominator')
            self._numerator = numerator
            self._denominator = denominator
        if reduce: self._reduce()

    @property
    def numerator(self):
        '''
        :return: int
        '''
        return self._numerator

    @property
    def denominator(self):
        '''
        :return: int
        '''
        return self._denominator

    def _reduce(self):
        '''
        Reduces Rational number using gcd.

        :return: None
        '''
        g = math.gcd(self._numerator, self._denominator)
        self._numerator //= g
        self._denominator //= g

    def __add__(self, other):
        ''' self + other'''
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        ''' self - other'''
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        '''self * other'''
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        '''self / other'''
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __floordiv__(self, other):
        '''self // other'''
        return (self.numerator * other.denominator) // (self.denominator * other.numerator)

    def __mod__(self, other):
        ''' self % other'''
        return Rational((self.numerator * other.denominator) % (other.numerator * self.denominator),
                        self.denominator * other.denominator)

    def __pos__(self):
        '''+self'''
        return Rational(self._numerator, self._denominator)

    def __neg__(self):
        '''-self'''
        return Rational(-self._numerator, self._denominator)

    def __eq__(self, other):
        '''self == other'''
        return self._numerator == other.numerator and self._denominator == other.denominator

    def __str__(self):
        '''
        :return: numerator/denominator
        '''
        return f'{self._numerator}/{self._denominator}'


if __name__ == '__main__':
    t1 = Rational(8, 1)
    t2 = Rational(16, 2)
    print(f'+: {t1 + t2}, -: {t1 - t2}, *: {t1 * t2}, /: {t1 / t2}, //: {t1 // t2}, %: {t1 % t2}, {-t1},'
          f' ==: {t1 == t2}, !=: {t1 != t2}')