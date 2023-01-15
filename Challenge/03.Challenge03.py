from PyQt5.QtWidgets import *
import sys


class CEVS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('중앙 전자 투표 시스템')

def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제d')

        self.tab1 = Tab1()
        self.tab2 = Tab2()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1, '투표')
        self.tabs.addTab(self.tab2, '투표생성')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)

        self.setLayout(self.vbox_layout)



class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.group_box = QGroupBox('투표 결과')

        self.progressbarA1 = QProgressBar()
        self.progressbarA1.setRange(0, 100)

        self.progressbarA2 = QProgressBar()
        self.progressbarA2.setRange(0, 100)

        self.progressbarA3 = QProgressBar()
        self.progressbarA3.setRange(0, 100)

        self.value = 0
        self.progressbarA1.setValue(self.value)
        self.progressbarA2.setValue(self.value)
        self.progressbarA3.setValue(self.value)

        self.buttonA1 = QPushButton('A1')
        self.buttonA1.clicked.connect(self.buttonA1_click)
        self.buttonA2 = QPushButton('A2')
        self.buttonA2.clicked.connect(self.buttonA2_click)
        self.buttonA3 = QPushButton('A3')
        self.buttonA3.clicked.connect(self.buttonA3_click)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.progressbarA1)
        self.vbox_layout.addWidget(self.progressbarA2)
        self.vbox_layout.addWidget(self.progressbarA3)

        self.group_box.setLayout(self.vbox_layout)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.group_box, 2, 0, 1, 1)



        self.setLayout(self.grid_layout)

    def buttonA1_click(self):
        self.value += 1
        self.progressbarA1.setValue(self.value)

    def buttonA2_click(self):
        self.value += 1
        self.progressbarA2.setValue(self.value)

    def buttonA3_click(self):
        self.value += 1
        self.progressbarA3.setValue(self.value)


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        self.form_layout = QFormLayout()

        self.line_edit = QLineEdit()
        self.button1 = QPushButton('버튼')
        self.line_edit = QLineEdit()
        self.button2 = QPushButton('초기화')
        self.line_edit_Q1 = QLineEdit()

        self.line_edit_A1 = QLineEdit()
        self.line_edit_A2 = QLineEdit()
        self.line_edit_A3 = QLineEdit()

        self.form_layout.addRow('질문: ', self.line_edit_Q1)
        self.form_layout.addRow('선택지: ', self.line_edit_A1)
        self.form_layout.addRow('', self.line_edit_A2)
        self.form_layout.addRow('', self.line_edit_A3)
        self.form_layout.addRow('', self.button1)
        self.form_layout.addRow('', self.button2)

        self.setLayout(self.form_layout)




def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
