from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from inst import *


txt_title = 'Health'
txt_name = 'Enter Your full name:'
txt_hintname = "Full name"
txt_hintage = "0"
txt_test1 = 'Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\nWrite down the result in the appropriate field.'
txt_test2 = 'Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button\nto start the squat counter.'
txt_test3 = 'Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\nPress the "Start final test" button to start the timer.\nThe seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.'
txt_sendresults = 'Send the results'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Start the first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start the final test'
txt_timer = ''


txt_age = 'Full years:'
txt_finalwin = 'Results'
txt_index = 'Roufier Index: '
txt_workheart = 'Cardi'

win_x, win_y = 200, 100
win_width, win_height = 1000, 600



class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.set_appear()

        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)