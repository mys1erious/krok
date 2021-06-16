'''
Second task from oop lab 4

Author: Eugene Lavrinovych
'''


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime


ingredient_price = 20


class Scraper:
    '''
    Represents Scraper for Domino`s Pizza
    '''

    pizza_url = 'https://dominos.ua/en/irpin/Pizza/'
    ingredients_url = 'https://dominos.ua/en/irpin/create/'

    @staticmethod
    def get_html(url):
        '''
        Gets html of given url
        :param url: str
        :return: html
        '''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        # time.sleep(0.2)
        html = driver.page_source
        driver.quit()
        return html

    def scr_pizza(self):
        '''
        Scrapes pizza from Domino`s

        :return: list of pizza
        '''
        soup = BeautifulSoup(self.get_html(self.pizza_url), features='html.parser')
        lst = soup.find_all('div', class_="dp-product-list__item")
        pizza_lst = []
        for item in lst:
            ingredients_lst = []
            title = item.find('a', class_='dp-product-block__title-text').text
            price = item.find('span', class_='dp-product-block__price').text
            currency = item.find('span', class_='dp-product-block__currency').text
            _ingredients = item.find('div', class_='dp-product-block__toppings-row')
            ingredients = _ingredients.find('span').text
            ingredients = ingredients.split(', ')
            for i in ingredients:
                ingredients_lst.append(Ingredient(i, ingredient_price))
            pizza = Pizza(title, ingredients_lst, float(price), currency)
            pizza_lst.append(pizza)
        return pizza_lst

    def scr_ingredients(self):
        '''
        Scrapes ingredients from Domino`s

        :return: ingredients list
        '''
        soup = BeautifulSoup(self.get_html(self.ingredients_url), features='html.parser')
        lst = soup.find_all('div', class_="dp-constructor__ingredients-item")
        ingr_lst = []
        for item in lst:
            title = item.find('div', class_='title').text
            ingr = Ingredient(title, ingredient_price)
            ingr_lst.append(ingr)
        return ingr_lst


def type_check(name, obj, value, _type):
    '''
    Type checker

    :param name: name of variable (str)
    :param obj: name of class
    :param value: value to check for type
    :param _type: type for value
    :return: None
    '''
    if not isinstance(value, _type):
        raise TypeError(f"'{type(value).__name__}' object cannot be interpreted as a {name} of a {obj}")
    if not value:
        raise ValueError(f'{obj} cannot be without {name}')


class Menu(Scraper):
    '''
    Represents Menu class
    '''

    def __init__(self):
        self.pizza_menu = self.scr_pizza()
        self.ingredients_list = self.scr_ingredients()
        self.pizza_of_the_day = self.pizza_menu[datetime.datetime.today().weekday()]
        self.pizza_of_the_day.price *= 0.8


class Customer:
    '''
    Represents Customer Class
    '''

    def __init__(self, name, lastname, phone, address):
        '''
        Initialize Customer object

        :param name: str
        :param lastname: str
        :param phone: str
        :param address: str
        '''

        type_check('name', 'Customer', name, str)
        self.name = name

        type_check('lastname', 'Customer', lastname, str)
        self.lastname = lastname

        type_check('phone', 'Customer', phone, str)
        self.phone = phone

        type_check('address', 'Customer', address, str)
        self.address = address

    def __str__(self):
        '''
        :return: Customer info
        '''
        return f'Customer info:\n Name - {self.name} {self.lastname}\n Phone - {self.phone}\n Address - {self.address}'


class Pizza:
    '''
    Represents Pizza Class
    '''
    def __init__(self, title, ingredients, price, currency='uah'):
        '''
        Initialize Pizza object

        :param title: str
        :param ingredients: list
        :param price: float, int
        :param currency: str
        '''

        type_check('title', 'Pizza', title, str)
        self.title = title

        type_check('ingredients', 'Pizza', ingredients, list)
        self.ingredients = ingredients

        type_check('price', 'Pizza', float(price), (float, int))
        self.price = float(price)

        type_check('currency', 'Pizza', currency, str)
        self.currency = currency

    def add_ingredient(self, ingr_name):
        '''
        Adds ingredient to the pizza

        :param ingr: str
        '''
        self.ingredients.append(Ingredient(ingr_name, ingredient_price))

    def remove_ingredient(self, ingr_name):
        '''
        Removes ingredient from the pizza

        :param pizza: str
        :param ingr: str
        '''
        for i in self.ingredients:
            if i.title == ingr_name:
                self.ingredients.remove(i)

    def __str__(self):
        '''
        :return: Pizza info
        '''
        ingredients = ''
        for i in self.ingredients:
            ingredients += f'{i}, '
        ingredients = ingredients[:-2]
        return f' {self.title}\n' \
               f' Ingredients: {ingredients}\n' \
               f' Price: {self.price:.2f} {self.currency}\n'


class Ingredient:
    '''
    Represents Ingredient Class
    '''
    def __init__(self, title, price, currency='uah'):
        '''
        Initialize Ingrdient object

        :param title: str
        :param price: float, int
        :param currency: str
        '''

        type_check('title', 'Ingredient', title, str)
        self.title = title

        type_check('price', 'Ingredient', float(price), (int, float))
        self.price = int(price)

        type_check('currency', 'Ingredient', currency, str)
        self.currency = currency

    def __str__(self):
        '''
        :return: Ingredient title
        '''
        return f'{self.title}'


INGREDIENTS_MIN = 1
INGREDIENTS_MAX = 20
class IngredientsLimit(Exception):
    pass


class Order:
    '''
    Represents Order Class
    '''

    def __init__(self, customer, menu):
        '''
        :param customer: Customer()
        :param menu: Menu()
        '''
        if not isinstance(customer, Customer):
            raise TypeError(f'{type(customer).__name__} object cannot be interpreted as a customer')
        if not isinstance(menu, Menu):
            raise TypeError(f'{type(menu).__name__} object cannot be interpreted as a menu')

        self.customer = customer
        self.order = []
        self.menu = menu
        self._total_price = 0

    def add_item(self, name):
        '''
        Adds pizza to order

        :param name: str
        '''
        if not isinstance(name, str):
            raise ValueError(f'{type(name).__name__} object cannot be interpreted as a name of pizza')

        for i in self.menu.pizza_menu:
            if name == i.title:
                self.order.append(i)
                break

    def remove_item(self, name):
        '''
        Removes pizza from order

        :param name: str
        '''
        if not isinstance(name, str):
            raise ValueError(f'{type(name).__name__} object cannot be interpreted as a name of pizza')

        for i in self.menu.pizza_menu:
            if name == i.title:
                self.order.remove(i)
                break

    @property
    def total_price(self):
        '''
        Total price of order

        :return: float
        '''
        for i in self.order:
            self._total_price += i.price
        return self._total_price

    def __str__(self):
        '''
        :return: Order info
        '''
        order = ''
        for i in self.order:
            order += f'{i}\n'
        return f'{self.customer}\nOrder:\n{order}Total price: {self.total_price:.2f}'


if __name__ == '__main__':
    menu = Menu()

    # name, surname = input('Enter your name and surname: ').split()
    # phone = input('Phone: ')
    # address = input('Delivery address: ')

    customer = Customer(name='E', lastname='L', phone='095', address='Irp')

    t = input('--If you choose pizza-of-the-day you`ll get 20% discount--\nPress any button to continue')
    for i in menu.pizza_menu:
        print(i)
    print('Pizza of the day:\n', menu.pizza_of_the_day)

    order = Order(customer, menu)
    make_order = True
    while True:
        name = input('Name of pizza to add or "done" to finish your order: ')
        if name == 'done':
            break
        order.add_item(name)

    while True:
        check = input('Type "ingredients" to see ingredients list, add/remove to change ingredients in pizza,'
                      ' otherwise press any button: ')
        if check == 'ingredients':
            print(f'\nIngredients price: {ingredient_price}')
            for i in menu.ingredients_list:
                print(i)

        elif check == 'add':
            for i in order.order:
                print(i.title)
            pizza_title = input('Pizza name: ')
            for i in order.order:
                if i.title == pizza_title:
                    pizza = i
                    break
            ing = input('Ingredient name: ')
            pizza.add_ingredient(ing)

        elif check == 'remove':
            for i in order.order:
                print('\n', i.title, '\n--Ingredients--')

                for j in i.ingredients:
                    print(j)
            pizza_title = input('Pizza name:')
            for i in order.order:
                if i.title == pizza_title:
                    pizza = i
                    break
            ing = input('Ingredient name: ')
            pizza.remove_ingredient(ing)

        else:
            break
    print(order)
