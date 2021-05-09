from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Pyqt5 Python37
# 20210508
# ListWidget用法，形如好友列表的界面形式
# 对tree的内容进行添加，修改，删除

class QSample(QWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(400, 300)

        # 定义树控件
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)  #列数
        self.tree.setHeaderLabel('Tree Name')
        self.tree.setColumnWidth(0, 180)  # 第一个数字用于定位被设置的列位置，下同
        self.tree.clicked.connect(self.onclicked)  # 响应事件

        # 定义根目录
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'Root')
        root.setIcon(0, QIcon('./lock.jpg'))  # 用于设定图标
        # 初始化根目录下一级成员
        root_child1 = QTreeWidgetItem(root)
        root_child1.setText(0, 'child1')
        root_child2 = QTreeWidgetItem(root)
        root_child2.setText(0, 'child2')
        root_child3 = QTreeWidgetItem(root)
        root_child3.setText(0, 'child3')
        root_child4 = QTreeWidgetItem(root)
        root_child4.setText(0, 'child4')
        root_child4.setCheckState(0, Qt.Checked)  # 设定是否可选
        # 初始化二级成员
        root_child4_itme1 = QTreeWidgetItem(root_child4)
        root_child4_itme1.setText(0, 'item1')
        root_child4_itme2 = QTreeWidgetItem(root_child4)
        root_child4_itme2.setText(0, 'item2')

        # 定义操作功能
        self.input = QLineEdit(self)
        self.addbtn = QPushButton('Add Item')
        self.addbtn.clicked.connect(self.addItem)
        self.updatebtn = QPushButton('Edit Item')
        self.updatebtn.clicked.connect(self.updateItem)
        self.deletebtn = QPushButton('Delete Item')
        self.deletebtn.clicked.connect(self.deleteItem)
        
        # 操作区布局
        operatelayout = QVBoxLayout()
        operatelayout.addWidget(self.input)
        operatelayout.addWidget(self.addbtn)
        operatelayout.addWidget(self.updatebtn)
        operatelayout.addWidget(self.deletebtn)

        # 窗口布局
        MainLayout = QHBoxLayout()
        MainLayout.addWidget(self.tree)
        MainLayout.addLayout(operatelayout) # 嵌套操作区布局

        self.setLayout(MainLayout)

    # 显示选中item名称
    def onclicked(self):
        item = self.tree.currentItem() # 获取当前tree中被选中的item
        print(item.text(0) + ' is selected')  # 此处必须在text括号内加0，表明返回值所在列数
        self.input.setText(item.text(0)) # 将选中的item名称传送至输入框

    # 添加item
    def addItem(self):
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0, self.input.text())

    # 修改item
    def updateItem(self):
        item = self.tree.currentItem()
        item.setText(0, self.input.text())

    # 删除item
    def deleteItem(self):
        item = self.tree.currentItem()
        for items in self.tree.selectedItems():
            #注意:删除Root会报错，故改用try结构
            try:
                item.parent().removeChild(item)
            except:
                QMessageBox.warning(self,'Warning','Can Not Remove Root')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())
