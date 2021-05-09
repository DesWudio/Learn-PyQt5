from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys

# Pyqt5 Python37
# 20210506
# 文本字体选择器
# 文本颜色选择器
# 文本背景选择器

class QSample(QWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(400, 300)

        layout = QVBoxLayout()

        # 展示效果文本
        self.label = QLabel('Text Sample Here')
        self.label.setAlignment(Qt.AlignCenter)

        # 字体选择
        self.btn1 = QPushButton('Select Font')
        self.btn1.clicked.connect(self.getFont)

        # 文本颜色选择
        self.btn2 = QPushButton('Select Textcolor')
        self.btn2.clicked.connect(self.getTextColor)

        # Label背景色选择
        self.btn3 = QPushButton('Select Backgroundcolor')
        self.btn3.clicked.connect(self.getBGColor)

        # 载入图片（文件对话框）
        self.btn4 = QPushButton('Select An Image')
        self.btn4.clicked.connect(self.getfile)
        self.imglabel = QLabel()

        # 载入文本文档
        self.btn5 = QPushButton('Select a txt file')
        self.btn5.clicked.connect(self.gettxt)
        self.textedit = QTextEdit()

        layout.addWidget(self.label)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.imglabel)
        layout.addWidget(self.btn5)
        layout.addWidget(self.textedit)

        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if (ok):
            self.label.setFont(font)

    def getTextColor(self):
        color = QColorDialog.getColor()
        p = QPalette()  # 使用QPalette解释(unpack)颜色
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, '.', '*.jpg') # self, 路径，格式
        self.imglabel.setPixmap(QPixmap(fname))

    def gettxt(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  #可读任何文件
        dialog.setFilter(QDir.Files)  # 获取的目标为文件

        if (dialog.exec_()):
            fname = dialog.selectedFiles() # 获取选中的文件路径
            # 读txt标准方法
            f = open(fname[0],encoding='utf-8',mode='r')
            with f:
                data = f.read()
                self.textedit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())