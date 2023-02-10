# 다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onCliked)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # 필수 설정
        self.setWindowTitle('파일 다이얼로그 위젯')
        self.setGeometry(300,300,300,300)
        self.show()

    def onCliked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')

        if fname[0]: # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data)
            
            file.close()

        QMessageBox.about(self, '종료', '로드했습니다,')
        
    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  # 프로그램 종료
        else:
            event.ignore()  # 상태유지


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())