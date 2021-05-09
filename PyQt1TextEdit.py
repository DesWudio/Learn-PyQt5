from PyQt5.QtWidgets import *
import sys

# Pyqt5 Python37
# 20210505
# 多行文本输入
# 内容获取
# HTML获取

# 定义界面类，Qwidegt是Qt中的控件，可以同时存在多个嵌套


class EditorSample(QWidget):
    def __init__(self):  # 初始化实例
        super(EditorSample, self).__init__()  # 调用父类
        self.initUI()  # 初始化界面

    # 界面初始化函数(写在上一个里边也可以)
    def initUI(self):
        self.setWindowTitle('Sample_Editor')  # 定义窗体名称
        self.resize(300, 200)

        # 定义多行文本显示
        self.textEdit = QTextEdit()

        # 定义操作按钮
        self.buttonText = QPushButton('显示文本')
        self.buttonHtml = QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHtml = QPushButton('获取html')

        # 定义布局
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)  # 将控件加入布局
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHtml)

        self.setLayout(layout)  # 将layout布局应用给self

        # 为按钮绑定槽函数
        self.buttonText.clicked.connect(self.onclickButtonText)
        self.buttonHtml.clicked.connect(self.onclickButtonHTML)
        self.buttonToText.clicked.connect(self.onclickButtonToText)
        self.buttonToHtml.clicked.connect(self.onclickButtonToHtml)

    def onclickButtonText(self):
        self.textEdit.setPlainText('Hello There')  # 在多行文本控件内显示内容

    def onclickButtonHTML(self):
        self.textEdit.setHtml(
            '<font color="blue" size="5">Hello There!!</font>')

    # 取多行文本控件中的内容
    def onclickButtonToText(self):
        try:
            print(self.textEdit.toPlainText())
        except:
            pass

    # 取多行文本控件中的HTML内容
    def onclickButtonToHtml(self):
        try:
            print(self.textEdit.toHtml())
        except:
            pass


# 主函数
if __name__ == '__main__':
    # 标准流程
    app = QApplication(sys.argv)
    main = EditorSample()
    main.show()
    # 退出响应
    sys.exit(app.exec_())
