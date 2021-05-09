from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
# 引入之前的Widget
import pyqt11TreeWidget
import PyQt3SliderandSpinbox

# Pyqt5 Python37
# 20210509
# 停靠控件的用法
# 在制作软件时可以将窗口内容分开来做，在主窗口中引入
# 既方便整体更新，又方便局部维护


class QSample(QMainWindow):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(400, 300)
        self.setCentralWidget(QTextEdit())

        # 引用现有Widget
        self.dock_qt11 = QDockWidget()
        self.dock_qt11.setWidget(pyqt11TreeWidget.QSample())
        
        # 引用现有Widget
        self.dock_qt3 = QDockWidget()
        self.dock_qt3.setWidget(PyQt3SliderandSpinbox.QSample())        
        
        # 设定边栏控件
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_qt11)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_qt3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())