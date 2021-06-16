'''
Second task from oop lab 2

Author: Eugene Lavrinovych
'''


class VAT:
    '''
    Represents VAT class
    '''
    vat = {
        'EU': 0.2,
        'US': 0.1}

    def __init__(self, price, country):
        '''
        :param price:  int, float
        :param country: Country to get VAT price (str)
        '''
        self._price = price
        self.country = country

    @property
    def vat_price(self):
        '''
        :return: Price with vat or -1 if country name not in vat class variable
        '''
        try:
            return self._price * (1 + VAT.vat.get(self.country))
        except TypeError:
            return -1


class Invoice(VAT):
    '''
    Represents an invoice object for an item sold at the store
    '''

    def __init__(self, num, desc, quantity, price, country=''):
        '''
        Initialize invoice object

        :param num: Part number (str)
        :param desc: Part description (str)
        :param quantity: Quantity of the item being purchased (int)
        :param price: Price per item (float, int)
        :param country: Country to get VAT price (str)
        '''
        super().__init__(price, country)
        self._num = num
        self._desc = desc
        self._quantity = quantity

    @property
    def num(self):
        '''
        :return: Part number
        '''
        return self._num

    @property
    def desc(self):
        '''
        :return: Part description
        '''
        return self._desc

    @property
    def quantity(self):
        '''
        :return: Quantity of the item being purchased
        '''
        return self._quantity

    @property
    def price(self):
        '''
        :return: Price per item
        '''
        return self._price

    @num.setter
    def num(self, value):
        '''
        :param value: new part number to set
        :return: None
        '''
        if not isinstance(value, str):
            raise TypeError('Wrong data input')
        self._num = value

    @desc.setter
    def desc(self, value):
        '''
        :param value: New part description to set
        :return: None
        '''
        if not isinstance(value, str):
            raise TypeError('Wrong data input')
        self._desc = value

    @quantity.setter
    def quantity(self, value):
        '''
        :param value: New quantity to set
        :return: None
        '''

        if not isinstance(value, int):
            raise TypeError('Wrong data input')
        self._quantity = value

    @price.setter
    def price(self, value):
        '''
        :param value: New price per item to set
        :return: None
        '''
        if not isinstance(value, (float, int)):
            raise TypeError('Wrong data input')
        self._price = value

    def get_invoice_amount(self):
        '''
        Multiplies the quantity by the price per item to get invoice amount

        Tuple[0] - invoice amount without VAT
        Tuple[1] - invoice amount wit VAT
        :return: Tuple (int, int)
        '''
        if self.quantity < 0 or self.price < 0:
            return 0
        if self.vat_price == -1:
            vat_inv = -1
        else:
            vat_inv = int(self.quantity * self.vat_price)
        return int(self.quantity * self.price), vat_inv

    def __str__(self):
        return f'Part number: {self.num}\nDescription: {self.desc}\n' \
               f'Quantity of the item being purchased: {self.quantity}\n' \
               f'Price per item: {self.price}\n' \
               f'Price per item including VAT {self.vat_price}'


if __name__ == '__main__':

    t = Invoice('number 14', 'what', 55, 160.4, 'EU')
    print(t)
    print('Invoice amount: ', t.get_invoice_amount(), '\n')

    t.price = 14

    print('Price per item: ', t.price)
    print('Price per item with vat: ', t.vat_price)
    print('Invoice amount: ', t.get_invoice_amount())
