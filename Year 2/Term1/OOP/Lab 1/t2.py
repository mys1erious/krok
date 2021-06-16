'''
Second task from oop lab 1

Author: Eugene Lavrinovych
'''


class Invoice:
    '''
    Represents an invoice object for an item sold at the store
    '''
    def __init__(self, num, desc, quantity, price):
        '''
        Initialize invoice object

        :param num: Part number (str)
        :param desc: Part description (str)
        :param quantity: Quantity of the item being purchased (int)
        :param price: Price per item (float, int)
        '''
        if not isinstance(num, str) or not isinstance(desc, str) or not isinstance(quantity, int) \
        or not isinstance(price, (float, int)):
            raise TypeError('Wrong data input')

        self.num = num
        self.desc = desc
        self.quantity = quantity
        self.price = price

    def get_num(self):
        '''
        :return: Part number
        '''
        return self.num

    def get_desc(self):
        '''
        :return: Part description
        '''
        return self.desc

    def get_quantity(self):
        '''
        :return: Quantity of the item being purchased
        '''
        return self.quantity

    def get_price(self):
        '''
        :return: Price per item
        '''
        return self.price

    def set_num(self, num):
        '''
        :param num: new part number to set
        :return: None
        '''
        if not isinstance(num, str):
            raise TypeError('Wrong data input')
        self.num = num

    def set_desc(self, desc):
        '''
        :param desc: new part description to set
        :return: None
        '''
        if not isinstance(desc, str):
            raise TypeError('Wrong data input')
        self.desc = desc

    def set_quantity(self, quantity):
        '''
        :param quantity: mew quantity to set
        :return: None
        '''
        if not isinstance(quantity, int):
            raise TypeError('Wrong data input')
        self.quantity = quantity

    def set_price(self, price):
        '''
        :param price: new price per item to set
        :return: None
        '''
        if not isinstance(price, (float, int)):
            raise TypeError('Wrong data input')
        self.price = price

    def get_invoice_amount(self):
        '''
        Multiplies the quantity by the price per item to get invoice amount
        :return: invoice amount (int)
        '''
        if self.quantity < 0 or self.price < 0:
            return 0
        return int(self.quantity * self.price)

    def __str__(self):
        return f'Part number: {self.num}\nDescription: {self.desc}\n' \
               f'Quantity of the item being purchased: {self.quantity}\nPrice per item: {self.price}'


t = Invoice('number 14', 'what', 55, 160.4)
print(t)
print('Invoice amount: ', t.get_invoice_amount(), '\n')

t.set_price(14)

print('Price per item: ', t.get_price())
print('Invoice amount: ', t.get_invoice_amount())
