import math


def save_to_file(func):
    def saver(a, b):
        res = func(a, b)
        with open('results.txt', 'a') as f:
            f.write(f'Res: {res}\n')
            return res
    return saver


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
        if reduce: self.reduce()

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

    def reduce(self):
        '''
        Reduces Rational number using gcd.

        :return: None
        '''
        g = math.gcd(self._numerator, self._denominator)
        self._numerator //= g
        self._denominator //= g

    @save_to_file
    def __add__(self, other):
        ''' self + other'''
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    @save_to_file
    def __sub__(self, other):
        ''' self - other'''
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    @save_to_file
    def __mul__(self, other):
        '''self * other'''
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    @save_to_file
    def __truediv__(self, other):
        '''self / other'''
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    @save_to_file
    def __floordiv__(self, other):
        '''self // other'''
        return (self.numerator * other.denominator) // (self.denominator * other.numerator)

    @save_to_file
    def __mod__(self, other):
        ''' self % other'''
        return Rational((self.numerator * other.denominator) % (other.numerator * self.denominator),
                        self.denominator * other.denominator)

    @save_to_file
    def __pos__(self):
        '''+self'''
        return Rational(self._numerator, self._denominator)

    @save_to_file
    def __neg__(self):
        '''-self'''
        return Rational(-self._numerator, self._denominator)

    @save_to_file
    def __eq__(self, other):
        '''self == other'''
        return self._numerator == other.numerator and self._denominator == other.denominator

    def __str__(self):
        '''
        :return: numerator/denominator
        '''
        return f'{self._numerator}/{self._denominator}'



c1 = Rational(4, 2)
c2 = Rational(6, 2)
c3 = c1+c2
c4 = c2-c1
print(c3)
print(c4)