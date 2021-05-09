from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys

# Pyqt5 Python37
# 20210506
# 滑动与计数器控件用法

class QSample(QWidget):
    
    def __init__(self):
        super(QSample, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSample')
        self.resize(400,300)

        layout = QVBoxLayout()
        self.label = QLabel('Text Here')
        self.label.setAlignment(Qt.AlignCenter)
        
        # slider
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)

        # set parameters
        self.slider.setMinimum(12)
        self.slider.setMaximum(36)
        self.slider.setSingleStep(3)
        self.slider.setValue(22) # or the minimal one
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(6) # or 10

        self.slider.valueChanged.connect(lambda:self.showValue(self.label, self.slider))
        layout.addWidget(self.slider)

        # spinbox
        self.spinbox = QSpinBox()
        layout.addWidget(self.spinbox)
        self.spinbox.setRange(12,36)
        self.spinbox.valueChanged.connect(lambda:self.showValue(self.label, self.spinbox))

        self.setLayout(layout)
        
    def showValue(self ,label, changer):
        size = changer.value()
        label.setFont(QFont('Arial',size))
        print(changer.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSample()
    main.show()
    sys.exit(app.exec_())