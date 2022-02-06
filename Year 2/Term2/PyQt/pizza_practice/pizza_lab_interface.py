'''
Qt rework for pizza lab from previous term
'''

import sys
import copy

from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QMainWindow, QWidget, QPushButton, QHBoxLayout, \
    QScrollArea, QGridLayout, QLineEdit, QApplication, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from pizza_lab import *


class PizzaQT(QFrame):
    def __init__(self, pizza):
        super().__init__()

        self.pizza = pizza

        self.selected = False
        self.ordered = False

        self.ui()

    def ui(self):
        width = 305
        height = 350

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedSize(width, height)
        self.setObjectName('pizza_frame')

        title = QLabel(f'{self.pizza.title}')
        title.setFixedHeight(30)
        title.setObjectName('title')

        image = QLabel()
        pixmap = QPixmap(self.pizza.photo)
        pixmap = pixmap.scaled(295, 180)
        image.setPixmap(pixmap)
        image.setObjectName('image')

        self.ingredients = QLabel()
        ans = ''
        for i in self.pizza.ingredients:
            ans += f'{i}, '
        ans = ans[:-2]
        self.ingredients.setText(ans)
        self.ingredients.setFixedHeight(50)
        self.ingredients.setWordWrap(True)
        self.ingredients.setObjectName('ingredients')

        price = QLabel(f'{self.pizza.price} {self.pizza.currency}')
        price.setFixedHeight(30)
        price.setObjectName('price')

        if self.pizza.daily:
            daily = QLabel('Pizza of the day')
            daily.setFixedHeight(30)
            daily.setObjectName('daily')
            self.layout().addWidget(daily)

        self.setStyleSheet('#pizza_frame {border: 1px solid black;}'
                           '#title, #image, #ingredients, #price, #daily {border: 1px solid black;}')

        self.layout().addWidget(image)
        self.layout().addWidget(title)
        self.layout().addWidget(self.ingredients)
        self.layout().addWidget(price)

    def change_ingredients(self):
        box = IngredientsChangerBox(self)
        box.setInformativeText('Choose what to do with ingredients: ')
        box.show()

        ans = box.exec()
        if ans == 0:
            self.add_ingredients()
        elif ans == 1:
            self.remove_ingredients()

    def add_ingredients(self):
        ingr, ok = QInputDialog.getText(self, 'Add', 'Enter ingredient to add: ')
        if ok:
            self.pizza.add_ingredient(ingr)

            old = self.ingredients.text()
            new = old + f', {ingr}'
            self.ingredients.setText(new)

    def remove_ingredients(self):
        ingr, ok = QInputDialog.getText(self, 'Remove', 'Enter ingredient to remove: ')
        if ok:
            self.pizza.remove_ingredient(ingr)

            old = self.ingredients.text()
            new = old.replace(f'{ingr}', '')
            self.ingredients.setText(new)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            stl = self.styleSheet()
            if not self.selected:
                stl = stl.replace('#pizza_frame {border: 1px solid black;}', '#pizza_frame {border: 3px solid blue;}')
                self.selected = True
            else:
                stl = stl.replace('#pizza_frame {border: 3px solid blue;}', '#pizza_frame {border: 1px solid black;}')
                self.selected = False
            self.setStyleSheet(stl)

        elif e.button() == Qt.RightButton:
            if self.ordered:
                self.change_ingredients()


class IngredientsChangerBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ingredients changer')
        self.addButton(QPushButton('Add'), QMessageBox.YesRole)
        self.addButton(QPushButton('Remove'), QMessageBox.NoRole)


class MenuQT(QScrollArea):
    def __init__(self):
        super().__init__()
        self.menu = Menu()

        self.ui()

    def ui(self):
        self.menu_container = QWidget()
        self.menu_container.setLayout(QGridLayout())

        j = 0
        for i in range(len(self.menu.pizza_menu)):
            if i % 4 == 0:
                j += 1
            self.menu_container.layout().addWidget(PizzaQT(self.menu.pizza_menu[i]), j, i % 4)

        self.setWidgetResizable(True)
        self.setWidget(self.menu_container)


class OrderQT(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.customer = None
        self.menu = menu

        self.order = Order(self.customer, self.menu)

        self.ui()

    def ui(self):
        self.setLayout(QHBoxLayout())

        order_info = self.order_info()
        order_items = self.order_items()

        self.layout().addWidget(order_info)
        self.layout().addWidget(order_items)

    def order_info(self):
        order_info = QFrame()
        order_info.setLayout(QVBoxLayout())
        order_info.layout().setAlignment(Qt.AlignTop)

        self.customer_name = QLineEdit()
        self.customer_name.setPlaceholderText('First name')

        self.customer_surname = QLineEdit()
        self.customer_surname.setPlaceholderText('Last name')

        self.customer_phone = QLineEdit()
        self.customer_phone.setPlaceholderText('Phone')

        self.customer_address = QLineEdit()
        self.customer_address.setPlaceholderText('Address')

        self.customer_btn = QPushButton('Make Order')
        self.customer_btn.clicked.connect(self.make_order)

        order_info.layout().addWidget(self.customer_name)
        order_info.layout().addWidget(self.customer_surname)
        order_info.layout().addWidget(self.customer_phone)
        order_info.layout().addWidget(self.customer_address)
        order_info.layout().addWidget(self.customer_btn)

        return order_info

    def order_items(self):
        area = QScrollArea()

        self.order_items_container = QWidget()
        self.order_items_container.setLayout(QGridLayout())

        area.setWidgetResizable(True)
        area.setWidget(self.order_items_container)

        return area

    def make_order(self):
        name = self.customer_name.text()
        surname = self.customer_surname.text()
        phone = self.customer_phone.text()
        address = self.customer_address.text()
        self.customer = Customer(name, surname, phone, address)
        self.order.customer = self.customer

        order = copy.deepcopy(self.order)
        orders_list.append(order)
        print(orders_list)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui()
        self.show()

    def ui(self):
        self.setWindowTitle('Pizza app')
        self.setObjectName('main_window')
        self.setFixedSize(1600, 900)

        self.container = QWidget()
        self.container.setLayout(QVBoxLayout())

        self.nav_bar = self.nav_bar_view()

        self.menu = MenuQT()
        self.customer = None
        self.order = OrderQT(self.menu.menu)
        self.order.hide()

        self.container.layout().addWidget(self.nav_bar)
        self.container.layout().addWidget(self.menu)
        self.container.layout().addWidget(self.order)

        self.setCentralWidget(self.container)

    def nav_bar_view(self):
        menu_btn = QPushButton('Menu')
        menu_btn.clicked.connect(self.show_menu)

        order_btn = QPushButton('Order')
        order_btn.clicked.connect(self.show_order)

        self.add_to_order_btn = QPushButton('Add to order')
        self.add_to_order_btn.clicked.connect(self.add_to_order)

        self.remove_from_order_btn = QPushButton('Remove from order')
        self.remove_from_order_btn.clicked.connect(self.remove_from_order)
        self.remove_from_order_btn.hide()

        nav_bar = QWidget()
        nav_bar.setFixedHeight(50)
        nav_bar.setLayout(QHBoxLayout())
        nav_bar.layout().addWidget(menu_btn)
        nav_bar.layout().addWidget(order_btn)
        nav_bar.layout().addWidget(self.add_to_order_btn)
        nav_bar.layout().addWidget(self.remove_from_order_btn)

        return nav_bar

    def add_to_order(self):
        for i in self.menu.menu_container.findChildren(PizzaQT):
            if i.selected:
                self.order.order.add_item(i.pizza.title)

                p = PizzaQT(Pizza(i.pizza.title, i.pizza.ingredients, i.pizza.price))
                p.ordered = True
                self.order.order_items_container.layout().addWidget(p)

    def remove_from_order(self):
        for i in self.order.order_items_container.findChildren(PizzaQT):
            if i.selected and i.ordered:
                self.order.order.remove_item(i.pizza.title)

                i.setParent(None)
                self.order.order_items_container.layout().removeWidget(i)

    def show_menu(self):
        self.order.hide()
        self.menu.show()

        self.add_to_order_btn.show()
        self.remove_from_order_btn.hide()

    def show_order(self):
        self.order.show()
        self.menu.hide()

        self.add_to_order_btn.hide()
        self.remove_from_order_btn.show()


if __name__ == '__main__':

    orders_list = []

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())