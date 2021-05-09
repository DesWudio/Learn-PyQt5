from PyQt5.QtWidgets import *
import sys

# Pyqt5 Python37
# 20210505
# 多行文本输入
# 内容获取
# HTML获取

class EditorSample(QWidget):
    def __init__(self):
        super(EditorSample, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Sample_Editor')
        self.resize(300,200)
        
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHtml = QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHtml = QPushButton('获取html')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHtml)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onclickButtonText)
        self.buttonHtml.clicked.connect(self.onclickButtonHTML)
        self.buttonToText.clicked.connect(self.onclickButtonToText)
        self.buttonToHtml.clicked.connect(self.onclickButtonToHtml)

    def onclickButtonText(self):
        self.textEdit.setPlainText('Hello There')
    
    def onclickButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello There!!</font>')

    def onclickButtonToText(self):
        try:
            print(self.textEdit.toPlainText())
        except:
            pass

    def onclickButtonToHtml(self):
        try:
            print(self.textEdit.toHtml())
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EditorSample()
    main.show()
    sys.exit(app.exec_())