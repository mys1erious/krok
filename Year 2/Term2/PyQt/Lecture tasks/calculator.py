import sys
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(320, 340)
        self.setLayout(qtw.QVBoxLayout())

        self.buttons = {
            '0': (5, 0),
            '1': (4, 0),
            '2': (4, 1),
            '3': (4, 2),
            '4': (3, 0),
            '5': (3, 1),
            '6': (3, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '+': (4, 3),
            '-': (3, 3),
            '*': (2, 3),
            '/': (1, 3),
            '=': (5, 2, 1, 2),
            '.': (5, 1),
            'TBD': (1, 0),
            'Clear': (1, 1),
            'Del': (1, 2)
        }
        self.operators = ['+', '-', '/', '*', '=']
        self.data = []

        self.ui()

        self.show()

    def ui(self):

        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.res_field = qtw.QLineEdit('0')
        self.res_field.setFixedSize(284, 40)
        self.res_field.setReadOnly(True)
        container.layout().addWidget(self.res_field)
        for item, pos in self.buttons.items():
            btn = qtw.QPushButton(item)
            btn.setFixedSize(70, 50)
            btn.clicked.connect(self.btn_clicked)
            if item == '=':
                btn.setFixedSize(142, 50)
                container.layout().addWidget(btn, pos[0], pos[1], pos[2], pos[3])
            else:
                container.layout().addWidget(btn, pos[0], pos[1])
        self.layout().addWidget(container)

    def btn_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == 'Clear':
            self.data.clear()
        elif text == 'Del':
            try: self.data.pop()
            except IndexError: pass
        elif text == 'TBD':
            pass
        elif text in self.operators and not self.data:
            pass
        elif text == '=':
            if '=' in self.data:
                s = self.data.index('=') # 10+14=14; s=5; del self.data[:6]
                del self.data[:s+1]
            else:
                data_res = '='
                data_res += str(eval(''.join(self.data)))
                self.data.extend(data_res)
        elif text in self.operators and self.data[-1] in self.operators:
            self.data = self.data[:-1]
            self.data += text
        else:
            self.data.append(text)
        print(self.data)
        self.res_field.setText(''.join(self.data))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    sys.exit(app.exec())
