import sys
import random

from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, QDesktopWidget, QVBoxLayout, QAction,\
    QDialog, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

SUIT_LIST = ['C', 'D', 'H', 'S']

CARD_WIDTH = 130
CARD_HEIGHT = 190

STACK_CARD_SPACE = 35
DECK_CARD_SPACE = 0.5


class Card(QLabel):
    def __init__(self, value, suit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suit = suit
        self.value = value

        self.face_up = False
        self.top_card = False
        self.stack = None

        self.ui()

    def ui(self):
        self.load_image()
        self.setPixmap(self.back)

    @property
    def color(self):
        return 'r' if self.suit in ('H', 'D') else 'b'


    def load_image(self):
        self.face = QPixmap(f'cards/{self.value}{self.suit}.png')
        self.back = QPixmap('images/card_back.png')
        self.face = self.face.scaled(CARD_WIDTH, CARD_HEIGHT)
        self.back = self.back.scaled(CARD_WIDTH, CARD_HEIGHT)

    def turn_up(self):
        self.setPixmap(self.face)
        self.face_up = True

    def turn_down(self):
        self.setPixmap(self.back)
        self.face_up = False

    def mousePressEvent(self, ev):
        self.pos = ev.pos()
        self.win_press_pos = ev.windowPos()

        self.pop = None

        if self.top_card and self.stack[-1] == self and not isinstance(self.stack, FoundationStack):
            self.pop = self.stack.get_card()
            self.pop.raise_()

        # For moving stacks between WorkStacks
        elif self.top_card and isinstance(self.stack, WorkStack):
            self.pop = []
            ind = self.stack.deck.index(self)
            self.pop = self.stack.get_cards(ind)
            print(self.pop)  # For testing
            for c in self.pop:
                c.raise_()
        self.press_stack = self.stack

    def mouseMoveEvent(self, ev):
        win_pos = ev.windowPos()
        menu_bar_size = 20

        x = win_pos.x() - self.pos.x()
        y = win_pos.y() - self.pos.y() - menu_bar_size

        if self.top_card and not isinstance(self.pop, list) \
                and not isinstance(self.press_stack, StockDeck) \
                and not isinstance(self.press_stack, FoundationStack):
            self.move(int(x), int(y))

        # For moving stacks between WorkStacks
        elif isinstance(self.pop, list) and isinstance(self.press_stack, WorkStack):
            for i in range(len(self.pop)):
                if i == 0:
                    self.pop[i].move(int(x), int(y))
                else:
                    self.pop[i].move(int(x), int(y + STACK_CARD_SPACE))

    def mouseReleaseEvent(self, ev):
        self.win_release_pos = ev.windowPos()

        if self.top_card:

            # Adding cards to WasteDeck from StockDeck
            if isinstance(self.press_stack, StockDeck):
                    self.pop.turn_up()
                    self.parent().findChildren(WasteDeck)[0].add_card(self.pop)

            elif isinstance(self.press_stack, WasteDeck):

                # Adding cards to WorkStack from WasteDeck
                work_stack_added = False
                for work_stack in self.parent().findChildren(WorkStack):
                    if work_stack.x_left < self.win_release_pos.x() < work_stack.x_right and \
                            work_stack.y_top < self.win_release_pos.y() < work_stack.y_bot:
                        if work_stack.is_valid_drop(self.pop):
                            work_stack.add_card(self.pop)
                            try:
                                self.parent().findChildren(WasteDeck)[0][-1].turn_up()
                            except IndexError:
                                pass
                            work_stack_added = True
                            break

                # Adding cards to FoundationStack from WasteDeck
                fnd_stack_added = False
                if not work_stack_added:
                    for fnd_stack in self.parent().findChildren(FoundationStack):
                        if fnd_stack.x_left < self.win_release_pos.x() < fnd_stack.x_right and \
                                fnd_stack.y_top < self.win_release_pos.y() < fnd_stack.y_bot:
                            if fnd_stack.is_valid_drop(self.pop):
                                fnd_stack.add_card(self.pop)
                                try:
                                    self.parent().findChildren(WasteDeck)[0][-1].turn_up()
                                except IndexError:
                                    pass
                                fnd_stack_added = True
                                break

                # Returning card to initial position if card wasnt moved to any of the Stacks above
                if not work_stack_added and not fnd_stack_added:
                    self.parent().findChildren(WasteDeck)[0].add_card(self.pop)

            elif isinstance(self.press_stack, WorkStack):

                # Adding cards to WorkStack from WorkStack
                work_stack_added = False
                for work_stack in self.parent().findChildren(WorkStack):
                    if work_stack.x_left < self.win_release_pos.x() < work_stack.x_right and \
                            work_stack.y_top < self.win_release_pos.y() < work_stack.y_bot:

                        if not isinstance(self.pop, list):
                            if work_stack.is_valid_drop(self.pop):
                                work_stack.add_card(self.pop)
                                work_stack_added = True
                                break
                            else:
                                break
                        elif work_stack.is_valid_drop(self.pop[0]):
                            work_stack.add_cards(self.pop)
                            work_stack_added = True
                            break

                # Adding cards to FoundationStack from WorkStack
                fnd_stack_added = False
                if not work_stack_added and not isinstance(self.pop, list):
                    for fnd_stack in self.parent().findChildren(FoundationStack):
                        if fnd_stack.x_left < self.win_release_pos.x() < fnd_stack.x_right and \
                                fnd_stack.y_top < self.win_release_pos.y() < fnd_stack.y_bot:
                            if fnd_stack.is_valid_drop(self.pop):
                                fnd_stack.add_card(self.pop)
                                fnd_stack_added = True
                                break

                    if self.game_win_check(self.window().foundation_stacks):
                        self.game_win_animation()

                # Returning card to initial position if card wasnt moved to any of the Stacks above
                if not work_stack_added and not fnd_stack_added:
                    if not isinstance(self.pop, list):
                        self.press_stack.turn_down_last_card()
                        self.press_stack.add_card(self.pop)
                    else:
                        self.press_stack.turn_down_last_card()
                        self.press_stack.add_cards(self.pop)
        self.press_stack = None
        print(self.press_stack, self.stack, type(self.stack))  # For testing

    def game_win_check(self, fss):
        n = [0, 0, 0, 0]
        for fnd_stack in range(len(fss)):
            if len(fss[fnd_stack]) == 13:
                n[fnd_stack] = 1
            if n.count(n[0]) == len(n) and n[0] == 1:
                return True
        return False

    def game_win_animation(self):
        dialog = QDialog()
        dialog.setFixedSize(200, 90)

        w, h = 70, 30

        lbl = QLabel(dialog)
        lbl.setText('You Won')
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setFixedSize(w, h)

        btn_close = QPushButton('Close', dialog)
        btn_close.clicked.connect(self.exit_app)
        btn_close.setFixedSize(w, h)

        btn_restart = QPushButton('Restart', dialog)
        btn_restart.clicked.connect(lambda: MainWindow.restart(dialog))
        btn_restart.setFixedSize(w, h)

        lbl.move(65, 10)
        btn_close.move(25, 50)
        btn_restart.move(100, 50)

        dialog.exec()

    def exit_app(self):
        sys.exit(app.exec)

    def __str__(self):
        return f'{self.suit}{self.value}'

    def __repr__(self):
        return f'{self.suit}{self.value}'


class BaseDeck(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.deck = []
        self.index = 0

        self.pos_shift_x = 0
        self.pos_shift_y = 0

    def ui(self):
        self.setGeometry(self.pos_shift_x, self.pos_shift_y, int(CARD_WIDTH + len(self) / 2), CARD_HEIGHT)
        self.geometry_rect = self.geometry().getRect()
        self.x_left, self.y_top, self.x_right, self.y_bot = self.geometry_rect
        self.y_bot += self.y_top
        self.x_right += self.x_left

    def get_card(self):
        card = self.deck.pop()
        try:
            card.stack[-1].top_card = True
        except IndexError:
            pass
        return card

    def add_card(self, card):
        if len(self) > 0:
            self[-1].top_card = False
            self[-1].turn_down()
        card.top_card = True
        card.turn_up()
        card.stack = self
        self.deck.append(card)

    def index(self, value):
        return self.deck.index(value)

    def __setitem__(self, key, value):
        self.deck[key] = value

    def __getitem__(self, item):
        return self.deck[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.deck):
            raise StopIteration()
        self.index += 1
        return self.deck[self.index - 1]

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return f'{self.deck}'


class StockDeck(BaseDeck):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.pos_shift_x = 30
        self.pos_shift_y = 30

        self.ui()

    def ui(self):
        super().ui()

    def generate_deck(self):
        for s in SUIT_LIST:
            for v in range(1, 14):
                c = Card(v, s, parent=self.parent())
                c.stack = self
                self.deck.append(c)
        random.shuffle(self)
        for c in self:
            c.raise_()
        self[-1].top_card = True

        for i in range(len(self)):
            self[i].move(self.pos_shift_x + int(i * DECK_CARD_SPACE), self.pos_shift_y)

    def add_card(self, card):
        super().add_card(card)
        card.move(self.pos_shift_x + int(len(self) * DECK_CARD_SPACE), self.pos_shift_y)

    def generate_from_waste_deck(self):
        d = self.parent().findChildren(WasteDeck)[0]
        for i in range(len(d)):
            c = d.get_card()
            self.add_card(c)
        for c in self:
            c.raise_()
        self[-1].turn_down()

    def mousePressEvent(self, ev):
        if not self.deck:
            self.generate_from_waste_deck()


class WasteDeck(BaseDeck):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.pos_shift_x = 250
        self.pos_shift_y = 30

        self.ui()

    def ui(self):
        super().ui()

    def add_card(self, card):
        super().add_card(card)
        card.move(self.pos_shift_x + int(len(self) * DECK_CARD_SPACE), self.pos_shift_y)


class WorkStack(BaseDeck):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.pos_shift_x = 240
        self.pos_shift_y = 250
        self.ui()

    def ui(self):
        super().ui()
        self.setLayout(QVBoxLayout())
        t = QLabel('')
        self.layout().addWidget(t)
        self.setStyleSheet('border: 1px solid black;')

    def init_add_card(self, card):
        super().add_card(card)
        card.move(self.x_left, self.pos_shift_y + int(len(self) * STACK_CARD_SPACE))
        self.y_bot += STACK_CARD_SPACE

    def add_card(self, card):
        card.top_card = True
        card.turn_up()
        card.stack = self
        self.deck.append(card)

        card.move(self.x_left, self.pos_shift_y + int(len(self) * STACK_CARD_SPACE))
        self.y_bot += STACK_CARD_SPACE

    def add_cards(self, cards):
        for c in cards:
            c.stack = self
            self.deck.append(c)
            c.move(self.x_left, self.pos_shift_y + int(len(self) * STACK_CARD_SPACE))
        self.y_bot += STACK_CARD_SPACE * len(cards)

    def get_card(self):
        card = self.deck.pop()
        try:
            card.stack[-1].top_card = True
        except IndexError:
            pass
        return card

    def get_cards(self, index):
        cards = []
        while len(self) != index:
            cards.append(self.get_card())
        cards.reverse()
        return cards

    def is_valid_drop(self, card):
        if not self:
            return True
        elif card.color != self[-1].color and card.value == self[-1].value - 1:
            return True
        return False

    def turn_down_last_card(self):
        try:
            if not self[-1].face_up:
                self[-1].top_card = False
        except IndexError:
            pass


class FoundationStack(BaseDeck):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.pos_shift_x = 735
        self.pos_shift_y = 30

        self.ui()

    def ui(self):
        super().ui()
        self.setLayout(QVBoxLayout())
        t = QLabel('')
        self.layout().addWidget(t)
        self.setStyleSheet('border: 1px solid black;')

    def add_card(self, card):
        card.top_card = True
        card.turn_up()
        card.stack = self
        self.deck.append(card)
        card.move(self.x_left, self.pos_shift_y)

    def is_valid_drop(self, card):
        if not self:
            if card.value == 1:
                self.suit = card.suit
                return True
        else:
            if card.suit == self.suit and card.value == self[-1].value + 1:
                return True
        return False


class MainWindow(QMainWindow):
    singleton: 'MainWindow' = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui()
        self.show()

    def ui(self):
        self.setWindowTitle('Solitaire')
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        cc = QDesktopWidget().availableGeometry().center()
        self.frameGeometry().moveCenter(cc)
        self.setStyleSheet('MainWindow {background-image: url(images/background.jpg)}')

        self.menuBar()
        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(self.restart)
        self.menuBar().addAction(restart_action)

        self.container = QWidget()

        self.stock_deck = StockDeck(parent=self.container)

        self.waste_deck = WasteDeck(parent=self.container)

        self.work_stacks = []
        for i in range(7):
            work_stack = WorkStack(parent=self.container)
            if i == 0:
                work_stack.move(work_stack.pos_shift_x, work_stack.pos_shift_y)
            else:
                work_stack.move(self.work_stacks[i - 1].x_right + STACK_CARD_SPACE, work_stack.pos_shift_y)
                work_stack.x_left = self.work_stacks[i - 1].x_right + STACK_CARD_SPACE
                work_stack.x_right = work_stack.x_left + work_stack.geometry().getRect()[2]
            self.work_stacks.append(work_stack)

        self.foundation_stacks = []
        for i in range(4):

            fnd_stack = FoundationStack(parent=self.container)
            if i == 0:
                fnd_stack.move(fnd_stack.pos_shift_x, fnd_stack.pos_shift_y)
            else:
                fnd_stack.move(self.foundation_stacks[i - 1].x_right + STACK_CARD_SPACE, fnd_stack.pos_shift_y)
                fnd_stack.x_left = self.foundation_stacks[i - 1].x_right + STACK_CARD_SPACE
                fnd_stack.x_right = fnd_stack.x_left + fnd_stack.geometry().getRect()[2]
            self.foundation_stacks.append(fnd_stack)

        self.start_game()

        self.setCentralWidget(self.container)

    def start_game(self):
        self.stock_deck.generate_deck()
        for i in range(1, 8):
            for j in range(i):
                c = self.stock_deck.get_card()
                self.work_stacks[i-1].init_add_card(c)
            for c in self.work_stacks[i-1]:
                c.raise_()

    @staticmethod
    def restart(dialog=None):
        MainWindow.singleton = MainWindow()
        if dialog:
            dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow.restart()
    sys.exit(app.exec())