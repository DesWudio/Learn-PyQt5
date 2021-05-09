from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys

# Pyqt5 Python37
# 20210505
# 普通按钮
# 单选按钮
# 多选按钮
# 复选按钮
# GroupBox
# 下拉菜单

class QPushButtonSample(QWidget):
    def __init__(self):
        super(QPushButtonSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sample_Editor')
        self.resize(400, 300)

        # 普通按钮
        self.button1 = QPushButton('Button1')
        self.button1.setText('普通按钮')
        self.button1.setCheckable(True)
        self.button1.toggle()  # 使按钮状态为按下（不执行按钮事件函数）
        # 使用lambda句式自定义传入参数
        self.button1.clicked.connect(lambda: self.pushbtnclick(self.button1))

        # 带图标按钮
        self.button2 = QPushButton('图标按钮')
        self.button2.setIcon(QIcon(QPixmap('./lock.jpg')))  # 多种格式支持
        self.button2.clicked.connect(lambda: self.pushbtnclick(self.button2))

        # 单选按钮
        self.mode1 = QRadioButton('MODE-1')
        self.mode1.setChecked(True)
        self.mode1.toggled.connect(lambda:self.showRadioButtonState(self.mode1))

        self.mode2 = QRadioButton('MODE-2')
        self.mode2.toggled.connect(lambda:self.showRadioButtonState(self.mode2))

        self.mode3 = QRadioButton('MODE-3')
        self.mode3.toggled.connect(lambda:self.showRadioButtonState(self.mode3))

        # 复选按钮
        self.checkbox1 = QCheckBox('Func-1')
        self.checkbox1.stateChanged.connect(lambda:self.showCheckBoxState(self.checkbox1))

        self.checkbox2 = QCheckBox('Func-2')
        self.checkbox2.stateChanged.connect(lambda:self.showCheckBoxState(self.checkbox2))

        self.checkbox3 = QCheckBox('Func-3')
        self.checkbox3.stateChanged.connect(lambda:self.showCheckBoxState(self.checkbox3))

        # 下拉菜单
        self.comboxlabel = QLabel('PleaseS elect')
        self.combox = QComboBox()
        self.combox.addItem('C++')
        self.combox.addItems(['C#','JavaScript','Python'])
        
        self.combox.currentIndexChanged.connect(lambda:self.showComBoxState(self.comboxlabel,self.combox))


        # 布局定义
        self.layout = QVBoxLayout()

        # 单选部分
        self.box1layout = QHBoxLayout()
        self.groupbox1 = QGroupBox('Mode Switch', self)
        self.box1layout.addWidget(self.mode1)
        self.box1layout.addWidget(self.mode2)
        self.box1layout.addWidget(self.mode3)
        self.groupbox1.setLayout(self.box1layout)

        # 复选部分
        self.checkboxlayout = QHBoxLayout()
        self.groupbox2 = QGroupBox('Func Include', self)
        self.checkboxlayout.addWidget(self.checkbox1)
        self.checkboxlayout.addWidget(self.checkbox2)
        self.checkboxlayout.addWidget(self.checkbox3)
        self.groupbox2.setLayout(self.checkboxlayout)

        # 下拉部分
        self.comboxlayout = QHBoxLayout()
        self.groupbox3 = QGroupBox('ComboBox',self)
        self.comboxlayout.addWidget(self.comboxlabel)
        self.comboxlayout.addWidget(self.combox)
        self.groupbox3.setLayout(self.comboxlayout)

        # 总体布局
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.groupbox1)
        self.layout.addWidget(self.groupbox2)
        self.layout.addWidget(self.groupbox3)

        self.setLayout(self.layout)

        # self.setLayout(self.layout)

    # 按钮事件
    def pushbtnclick(self, btn):
        print('The button ' + btn.text() + ' has been clicked')
        if(btn.isChecked()):
            print('checked')
        else:
            print('unchecked')

    # 单选事件
    def showRadioButtonState(self, rbtn):
        if(rbtn.isChecked() == True):
            print(rbtn.text() + ' checked')
        else:
            print(rbtn.text() + ' unchecked')

    # 复选事件
    def showCheckBoxState(self, cbtn):
        if(cbtn.isChecked()):
            print(cbtn.text() + ' activated')
        else:
            print(cbtn.text() + ' deactivated')
    
    def showComBoxState(self, label, cb):
        label.setText('Now it\'s: ' + cb.currentText())
        print(cb.currentText() + ' selected')
        if(cb.currentText()=='Python'):
            print('Warning: It\'s Current Using')
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonSample()
    main.show()
    sys.exit(app.exec_())