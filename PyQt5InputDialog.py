from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys

# Pyqt5 Python37
# 20210506
# 对话框集合

class QSample(QWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(300, 200)

        layout = QVBoxLayout()

        # 通用对话框
        self.btn1 = QPushButton('dialog1', self)
        self.btn1.clicked.connect(self.showDialog)

        # 信息对话框（发出通知：~~已经···，无图标）
        self.btn2 = QPushButton('infodialog', self)
        self.btn2.clicked.connect(self.showalldialog)

        # 消息对话框（请求确认：是否确定要···，信息i图表）
        self.btn3 = QPushButton('messagebox', self)
        self.btn3.clicked.connect(self.showalldialog)

        # 警告对话框（发出警告信息，叹号图标）
        self.btn4 = QPushButton('alertbox', self)
        self.btn4.clicked.connect(self.showalldialog)

        # 严重错误对话框（报错，红色X图标）
        self.btn5 = QPushButton('criticaltbox', self)
        self.btn5.clicked.connect(self.showalldialog)

        # 疑问对话框（发出疑问，蓝色？图标）
        self.btn6 = QPushButton('questbox', self)
        self.btn6.clicked.connect(self.showalldialog)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        layout.addWidget(self.btn6)
        self.setLayout(layout)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('OK', dialog)
        button.move(50, 50)
        button.clicked.connect(dialog.close)
        dialog.setWindowTitle('dialog1')
        dialog.setWindowModality(Qt.ApplicationModal)  # 以模式方式显示（仅关闭后可操作其他）

        dialog.exec_()

    def showalldialog(self):
        text = self.sender().text()
        if (text == 'infodialog'):
            QMessageBox.about(self, 'info', 'This is a infodialog')
        elif (text == 'messagebox'):
            reply = QMessageBox.information(self, 'message',
                                            'This is a messagedialog',
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
            print(reply == QMessageBox.Yes)  # 返回选取结果
        elif(text=='alertbox'):
            reply = QMessageBox.warning(self,'Warning','This is an alertdialog', 
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif(text=='criticaltbox'):
            QMessageBox.critical(self,'critic','This is a criticaldialog', 
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
        elif(text=='questbox'):
            reply = QMessageBox.question(self,'Quest','This is a questdialog', 
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
            print(reply == QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())