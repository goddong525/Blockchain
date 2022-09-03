# How to use PyQt

from PyQt5.QtWidgets import *  # 안에 있는것들을 전부 import 해주겠다.

import sys


class GUI(QWidget):  # 창을 띄울수 있는
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.button1, 0, 0, 1, 2)  # 좌표(0,0) 크기 세로1 가로 2
        self.grid_layout.addWidget(self.button2, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button3, 1, 1, 1, 1)

        self.setLayout(self.grid_layout)

    def button1_click(self):
        self.button1.setEnabled(False)  # 버튼이 누르면 회색으로 바뀌면서 못누르게 됨
        self.button1.setText('button 1 clicked')

    def button2_click(self):
        self.button1.setEnabled(True)  # 1번 버튼 다시 활성화
        self.button2.setEnabled(False)
        self.button2.setText('button 2 clicked')

    def button3_click(self):
        self.button1.setEnabled(True)
        self.button2.setEnabled(True)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
