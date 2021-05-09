from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
# 引入之前的Widget
import pyqt11TreeWidget

# Pyqt5 Python37
# 20210509
# 选项卡控件的使用
# 引用已有Widget控件
# 自定义新控件加入选项卡

class QSample(QTabWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTab')
        self.resize(400, 300)
        
        # 引入现有Widget
        self.tab1 = pyqt11TreeWidget.QSample()
        self.addTab(self.tab1, 'tab1')
        # 自定义widget
        self.tab2 = QWidget()
        self.addTab(self.tab2, 'tab2')

        self.tab2setUI()

    # 自定tab2内容
    def tab2setUI(self):
        layout = QVBoxLayout()
        self.edit = QLineEdit('Sample Text')
        self.btn = QPushButton('Button')

        layout.addWidget(self.edit)
        layout.addWidget(self.btn)

        self.tab2.setLayout(layout) # tab为容器主体，故为tab2设定布局



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())