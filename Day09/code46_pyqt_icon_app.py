import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        # GUI 화면 설정
        self.resize(400,200)
        self.show() #핵심
        self.setWindowTitle('python Window') 
        # icon 추가
        self.setWindowIcon(QIcon('./Day09/python.png'))               


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
