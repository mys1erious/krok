import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QHBoxLayout, QWidget, QAction, QMessageBox, QLabel, \
    QFrame, QDockWidget, QListWidget, QTextEdit, QPushButton
from PyQt5 import QtCore, QtGui


class MyController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()
        self.show()

    def UI(self):
        exit_action = QAction(QtGui.QIcon('close-icon.svg'), 'E&xit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        message_action = QAction('&Message', self)
        message_action.setStatusTip('Message information')
        message_action.triggered.connect(self.message_show)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        main_menu.addMenu('&Edit')
        main_menu.addMenu('&Help')
        file_menu.addAction(exit_action)

        self.toolbar = self.addToolBar('')
        self.toolbar.addAction(exit_action)
        self.toolbar.addAction(message_action)
        self.toolbar.setAllowedAreas(QtCore.Qt.TopToolBarArea | QtCore.Qt.BottomToolBarArea)

        status_left = QLabel('Left', self)
        status_left.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        status_middle = QLabel('Middle', self)
        status_middle.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        status_right = QLabel('Right', self)
        status_right.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.statusBar().addPermanentWidget(status_left, 1)
        self.statusBar().addPermanentWidget(status_middle, 1)
        self.statusBar().addPermanentWidget(status_right, 2)

        contents_window = QDockWidget('Table of Contents', self)
        contents_window.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, contents_window)
        heading_list = QListWidget(contents_window)
        contents_window.setWidget(heading_list)
        self.setCentralWidget(QTextEdit())

        self.window_minimize = QCheckBox('Window minimize button')
        self.window_maximize = QCheckBox('Window maximize button')
        self.window_close = QCheckBox('Window close button')

        self.window_minimize.clicked.connect(self.update_hint)
        self.window_maximize.clicked.connect(self.update_hint)
        self.window_close.clicked.connect(self.update_hint)

        layout = QHBoxLayout()
        layout.addWidget(self.window_minimize)
        layout.addWidget(self.window_maximize)
        layout.addWidget(self.window_close)

        self.centreWidget = QWidget()
        self.setCentralWidget(self.centreWidget)
        self.centreWidget.setLayout(layout)

        self.setWindowTitle('Window Buttons Controller')

    def message_show(self):
        box = IngredientsChangerBox(self)
        box.setInformativeText('Choose what to do with ingredients: ')
        box.show()
        box.buttonClicked.connect(self.boxButtonClick)

        ans = box.exec()
        print(ans)
        if ans == QMessageBox.Ok:
            print('OK clicked')

    def boxButtonClick(self, i):
        print("Button clicked is:", i.text())

    def update_hint(self):
        flags = QtCore.Qt.WindowFlags()
        if self.window_minimize.isChecked():
            flags |= QtCore.Qt.WindowMinimizeButtonHint
        if self.window_maximize.isChecked():
            flags |= QtCore.Qt.WindowMaximizeButtonHint
        if self.window_close.isChecked():
            flags |= QtCore.Qt.WindowCloseButtonHint

        self.preview_window = MyTestWindow(flags)
        self.preview_window.move(0, 0)
        self.preview_window.show()


class IngredientsChangerBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ingredients changer')
        self.addButton(QPushButton('Add'), QMessageBox.YesRole)
        self.addButton(QPushButton('Remove'), QMessageBox.NoRole)


class MyTestWindow(QMainWindow):
    def __init__(self, flags, parent=None):
        super().__init__(parent)
        self.setWindowFlags(flags)
        self.setWindowTitle('Preview Window')
        self.setGeometry(0, 0, 200, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyController()
    sys.exit(app.exec())