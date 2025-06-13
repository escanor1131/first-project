# my_app.py

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import txt_title, txt_hello, txt_instruction, txt_next, win_width, win_height, win_x, win_y
from second_win import TestWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()
        self.setup_layout()
        self.setup_connections()
        self.show()

    def setup_window(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def create_widgets(self):
        self.label_hello = QLabel(txt_hello)
        self.label_instruction = QLabel(txt_instruction)
        self.button_start = QPushButton(txt_next)

    def setup_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label_hello)
        layout.addWidget(self.label_instruction)
        layout.addWidget(self.button_start)
        self.setLayout(layout)

    def setup_connections(self):
        self.button_start.clicked.connect(self.open_test_window)

    def open_test_window(self):
        self.hide()
        self.test_window = TestWin()

if __name__ == '__main__':
    app = QApplication([])
    main_win = MainWindow()
    app.exec_()
