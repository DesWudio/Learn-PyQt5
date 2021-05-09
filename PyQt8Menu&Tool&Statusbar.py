from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, math

# Pyqt5 Python37
# 20210507
# MenuBar，QtoolBar，QStatusBar设置和用法

class QSample(QMainWindow):
    def __init__(self):
        super(QSample, self).__init__()
        self.setWindowTitle('QMenubar')
        self.resize(400, 300)

        self.Menubar = self.menuBar()
        
        # 定义菜单栏内容
        self.Menu_file = self.Menubar.addMenu('Documents')
        
        self.doc_open = QAction('Open doc',self)
        self.doc_open.setShortcut('Ctrl+o') # 注意：shortcut部分不能有空格
        self.Menu_file.addAction(self.doc_open)
        self.doc_open.triggered.connect(lambda:self.processTrigger(self.doc_open))
        
        self.doc_savefile = QAction('Save File', self)
        self.doc_savefile.setShortcut('Ctrl+s')
        self.Menu_file.addAction(self.doc_savefile)
        self.doc_savefile.triggered.connect(lambda:self.processTrigger(self.doc_savefile))

        self.Menu_edit = self.Menubar.addMenu('Edit')

        self.edit_undo = QAction('Redo',self)
        self.edit_undo.setShortcut('Ctrl+z')
        self.Menu_edit.addAction(self.edit_undo)
        self.edit_undo.triggered.connect(lambda:self.processTrigger(self.edit_undo))
        
        # 定义工具栏
        self.LToolBar = self.addToolBar('LeftBar')
        self.LToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) # 工具栏控制图标与文字显示
        # self.LToolBar.setOrientation(Qt.Vertical) # 设置工具栏朝向
        self.LToolBar.actionTriggered.connect(self.processTrigger) # 工具栏响应（可直接传送，无需采用lambda）
        
        self.Lbar_Arrow = QAction(QIcon('.\\ico_dark\\arrow_dark.ico'),'Arrow',self)
        self.LToolBar.addAction(self.Lbar_Arrow)

        self.Lbar_Hand = QAction(QIcon('.\\ico_dark\\hand_dark.ico'),'Hand',self)
        self.LToolBar.addAction(self.Lbar_Hand)

        # 定义状态栏
        # self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    # 将操作响应至状态栏
    def processTrigger(self, a):
        self.statusBar.showMessage(a.text(),3000)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())