# 콤보박스
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblOption = QLabel('선택값 ', self)            # self. 를 사용하면 전역변수 사용안하면 지역변수 전역변수는 def에 쓰는거랑 같음
        self.lblOption.move(20, 20)
        
        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')
        cbOption.move(20, 40)

        cbOption.activated[str].connect(self.onActivated)

        # 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300,300,300,300)
        self.show()

    def onActivated(self,text):
        self.lblOption.setText('선택값 : ' + text)
        self.lblOption.adjustSize() # 글자수만큼 라벨의 넓이 조정

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())