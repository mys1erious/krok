import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class QFontDialogExample(QWidget):
    def __init__(self):
        super().__init__(parent=None)

        self.vbox = QVBoxLayout()

        self.btn1 = QPushButton('Dialog', self)
        self.btn1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.showFont)

        self.lbl = QLabel('Knowledge only matter', self)
        self.lbl.move(130, 20)


        self.btn2 = QPushButton('Color', self)
        self.btn2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn2.move(20, 20)
        self.btn2.clicked.connect(self.showColor)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('Qwidget { background-color: %s }' % QColor(0,0,0).name())
        self.frm.setGeometry(130, 22, 100, 100)


        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.lbl)

        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.frm)


        self.setLayout(self.vbox)
        self.setGeometry(600, 600, 500, 360)
        self.setWindowTitle('Font/Color dialog')

        self.show()

    def showFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' %col.name())
            self.lbl.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QFontDialogExample()
    sys.exit(app.exec())