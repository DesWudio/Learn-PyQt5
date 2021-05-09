from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import sys

# Pyqt5 Python37
# 20210507
# 绘图工具
# 绘制文本
# 绘制图形
# 绘制图像


class QSample(QWidget):
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(400, 300)

    # # 绘制文本
    # def paintEvent(self, evnet):
    #     painter = QPainter(self)
    #     painter.begin(self)
    #     self.text = 'Here\'s The Sample Text'
    #     painter.setPen(QColor(150,43,5))
    #     painter.setFont(QFont('SimSun',25))
    #     painter.drawText(evnet.rect(),Qt.AlignCenter,self.text) # 内容始终剧中
    #     painter.end()
    
    # 绘制正弦曲线
    def paintEvent(self, evnet):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * 3.14 / 50) + size.height()/2.0
            painter.drawPoint(x, y)       
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())