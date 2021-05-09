from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys

# Pyqt5 Python37
# 20210506
# 输入框集合

class QSample(QWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(300, 200)

        # 表格布局
        layout = QFormLayout()

        # 可选输入框
        self.btn1 = QPushButton('Get List', self)
        self.btn1.clicked.connect(self.getItem)
        self.edit1 = QLineEdit()
        layout.addRow(self.btn1,self.edit1) # 加入表格行

        # 文本输入框
        self.btn2 = QPushButton('Get String', self)
        self.btn2.clicked.connect(self.getText)
        self.edit2 = QLineEdit()
        layout.addRow(self.btn2,self.edit2)

        # 整数输入框
        self.btn3 = QPushButton('Get Integrate', self)
        self.btn3.clicked.connect(self.getInt)
        self.edit3 = QLineEdit()
        layout.addRow(self.btn3,self.edit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('item1','item2','item3','item4')
        item, ok = QInputDialog.getItem(self,'Please Select:','list of itmes:',items)
        if ok and item: # 填写完成后
            self.edit1.setText(item)

    def getText(self):
        content, ok = QInputDialog.getText(self,'Please Input:','Input Text')
        if ok and content:
            self.edit2.setText(content)
    
    def getInt(self):
        num, ok = QInputDialog.getInt(self,'Please Input Intergrate','Input Intergrate')
        if ok and num:
            self.edit3.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())