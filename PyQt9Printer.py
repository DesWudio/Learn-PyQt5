from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtPrintSupport
from PyQt5.QtPrintSupport import *
import sys, math

# Pyqt5 Python37
# 20210507
# 在文件菜单栏中打印
# 直接打印
# 使用打印对话框打印
# 打印设定操作


class QSample(QMainWindow):
    def __init__(self):
        super(QSample, self).__init__()
        self.setWindowTitle('QMenubar')
        self.resize(400, 300)

        # 定义打印机
        self.printer = QPrinter()

        # 定义状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 定义菜单栏
        self.Menubar = self.menuBar()
        self.Menu_file = self.Menubar.addMenu('Documents')
        # 打开文本
        self.doc_open = QAction('Open File', self)
        self.doc_open.setShortcut('Ctrl+o')
        self.Menu_file.addAction(self.doc_open)
        self.doc_open.triggered.connect(
            lambda: self.processTrigger(self.doc_open))
        self.doc_open.triggered.connect(self.gettxt)

        # 打印前需设定
        self.doc_print = QAction('Print', self)
        self.doc_print.setShortcut('Ctrl+p')
        self.Menu_file.addAction(self.doc_print)
        self.doc_print.triggered.connect(
            lambda: self.processTrigger(self.doc_print))
        self.doc_print.triggered.connect(lambda: self.dialogprint())
        
        # 直接打印
        self.doc_print_direct = QAction('Print Directly', self)
        self.Menu_file.addAction(self.doc_print_direct)
        self.doc_print_direct.triggered.connect(
            lambda: self.processTrigger(self.doc_print_direct))
        self.doc_print_direct.triggered.connect(lambda: self.Print())

        # 打印设置
        self.doc_printset = QAction('Print Setting')
        self.Menu_file.addAction(self.doc_printset)
        self.doc_printset.triggered.connect(
            lambda: self.processTrigger(self.doc_printset))
        self.doc_printset.triggered.connect(lambda: self.setprint())

        # 打开文本容器
        self.editor = QTextEdit("Please Open A File", self)
        self.editor.setGeometry(30, 30, 340, 250)

    # 读取文本
    def gettxt(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  #可读任何文件
        dialog.setFilter(QDir.Files)  # 获取的目标为文件

        if (dialog.exec_()):
            fname = dialog.selectedFiles()  # 获取选中的文件路径
            # 读txt标准方法
            f = open(fname[0], encoding='utf-8', mode='r')
            with f:
                data = f.read()
                self.editor.setText(data)

    # 状态栏响应函数
    def processTrigger(self, a):
        self.statusBar.showMessage(a.text(), 3000)

    # 打印设定
    def setprint(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec()

    # 打印对话框
    def dialogprint(self):
        printdialog = QPrintDialog(self.printer, self)
        if (QDialog.accepted == printdialog.exec()):
            self.editor.print(self.printer)

    # 开始打印
    # 注意：此方法仅打印控件区域内容
    def Print(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        src = self.editor.grab()
        painter.drawPixmap(10, 10, src)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())