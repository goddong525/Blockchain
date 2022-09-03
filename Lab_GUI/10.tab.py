# How to use PyQt

from PyQt5.QtWidgets import *  # 안에 있는것들을 전부 import 해주겠다.

import sys


class tab1:  # 창을 띄울수 있는
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.progressbar = QProgressBar()
        self.progressbar.setRange(0, 100)  # 0 , 100 게이지바 왼쪽이 최솟값, 끝이 100 그래서 100 에서 150 이렇게도 가능.

        self.value = 0
        self.progressbar.setValue(self.value)

        self.button = QPushButton('+1')
        self.button.clicked.connect(self.button_click)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.progressbar, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button, 1, 0, 1, 1)

        self.setLayout(self.grid_layout)

    def button_click(self):
        self.value += 1
        self.progressbar.setValue(self.value)


class GUI(QWidget):  # 창을 띄울수 있는
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.tabs = QTabWidget()
        # self.tabs.addTab

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
