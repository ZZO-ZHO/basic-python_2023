import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        #   메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'),'Exit',self)
        actExit.setShortcut('Ctrl+Q') # 단축키 지정
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'),'Save',self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MineToolBar')
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate()   # 현재시각
        time = QTime.currentTime()
        self.statusBar().showMessage(now.toString('yyyy.MM.dd ddd') + ' ' + time.toString('hh:mm'))
        self.setWindowIcon(QIcon('./Day09/python.png'))               

        # GUI 화면 설정
        self.resize(400,200)
        self.setCenter()
    
        self.show() #핵심
        self.setWindowTitle('Bar Window')

    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry()   # 윈도우 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터의 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
