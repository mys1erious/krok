import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QSlider, QVBoxLayout
from PyQt5 import QtCore, QtGui


class SignalSlotExample(QWidget):
    def __init__(self):
        super(SignalSlotExample, self).__init__()

        font = QtGui.QFont('Times', 18, QtGui.QFont.Bold)

        self.label = QLabel('0')
        self.label.setFont(font)

        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.slider.valueChanged.connect(self.set_label_text)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        self.setGeometry(300, 300, 320, 180)

    def set_label_text(self, value):
        self.label.setText(str(value))

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SignalSlotExample()
    mainWindow.show()

    sys.exit(app.exec())