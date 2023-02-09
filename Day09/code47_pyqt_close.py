# 윈도우 창닫기 엡
# 2023.02.09
# 정재영

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit',self)
        btn.move(315,170)
        btn.resize(btn.sizeHint())
        # 버튼 툴 팁
        btn.setToolTip('저장하지 않고 누를시, 내용이 <b>삭제</b>됩니다')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(900,200,400,200)   #x, y, w, h
        self.setWindowIcon(QIcon('./Day09/python.png'))               
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
