import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        # GUI 화면 설정
        self.resize(400,200)
        self.show() #핵심
        self.setWindowTitle('Simple Window')                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
