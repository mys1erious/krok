import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
import random as rnd


class QLabelExample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi('app_interface.ui')
        self.ui.btn_text.clicked.connect(self.label_text)
        self.ui.btn_image.clicked.connect(self.label_image)
        self.ui.btn_gif.clicked.connect(self.label_gif)
        timer = QtCore.QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.show_time)

        self.show_time()
        self.ui.show()

    def label_text(self):
        self.ui.label.setText('text')

    def label_image(self):
        pixmap = QtGui.QPixmap('im1.png')
        pixmap = pixmap.scaled(256, 256)
        self.ui.label.setPixmap(pixmap)

    def label_gif(self):
        movie = QtGui.QMovie('giphy.gif')
        self.ui.label.setMovie(movie)
        movie.start()

    def show_time(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('mm:ss')
        self.ui.lcd_timer.display(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QLabelExample()
    sys.exit(app.exec())