# How to use PyQt

from PyQt5.QtWidgets import *  # 안에 있는것들을 전부 import 해주겠다.

import sys


class GUI(QWidget):  # 창을 띄울수 있는
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label = QLabel()

        self.list = QListWidget()
        self.list.addItem('아이템 1')
        self.list.addItem('아이템 2')
        self.list.clicked.connect(self.select_item)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.text_label)
        self.hbox_layout.addWidget(self.list)

        self.setLayout(self.hbox_layout)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
