from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel)
from inst import *
from second_win import *

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Welcome to the Health status detection program!'
txt_next = 'Start'
txt_instruction = ('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                    'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                    'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \n'
                    'then, within 45 seconds, the subject performs 30 squats.\n'
                    'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                    'and then for the last 15 seconds of the first minute of the recovery period.\n'
                    'Important! If you feel unwell during the test (dizziness,\n'
                    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.' )
txt_title = 'Health'

class MainWin(QWidget):
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__()

        # creating and configuring graphic elements:
        self.initUI()

        #establishes connections between elements
        self.connects()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start:
        self.show()


    def initUI(self):
        ''' creates graphic elements '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    
    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
