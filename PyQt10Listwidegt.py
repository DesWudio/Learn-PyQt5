from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Pyqt5 Python37
# 20210508
# ListWidget用法
# 形如windows打开方式对话框

class QSample(QMainWindow):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(300, 270)
        

        # 定义状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 定义listwedgit
        self.listwidege = QListWidget()
        self.listwidege.addItems(['item1','item2','item3','item4','item5'])
        self.listwidege.itemClicked.connect(self.processTrigger)
        
        self.setCentralWidget(self.listwidege)
    
    # 状态栏响应
    def processTrigger(self, a):
        self.statusBar.showMessage(a.text() + ' is selected', 3000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())