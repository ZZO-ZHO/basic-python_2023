# 다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btnDlg = QPushButton('Dialog', self)
        self.btnDlg.move(20, 20)
        self.btnDlg.clicked.connect(self.onCliked)

        self.textInput = QLineEdit(self)
        self.textInput.move(20, 50)

        # 필수 설정
        self.setWindowTitle('다이얼로그 위젯')
        self.setGeometry(300,300,300,300)
        self.show()

    def onCliked(self):
        text, ok = QInputDialog.getText(self, '인풋다이얼로그', '이름을 적으세요')

        if ok:
            self.textInput.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())