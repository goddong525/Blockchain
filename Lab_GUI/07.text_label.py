# How to use PyQt

from PyQt5.QtWidgets import *  # 안에 있는것들을 전부 import 해주겠다.

import sys


class GUI(QWidget):  # 창을 띄울수 있는
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label = QLabel()
        self.text_label.setText('텍스트')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)

        self.setLayout(self.vbox_layout)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
