from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel

from PyQt5.QtWidgets import QPushButton

# 此.py文件实现具体的业务逻辑
import action
from deblur_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):  # 基本设置，改类名
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 接下来写信号和槽函数，从而保证python的逻辑代码和界面分离
        # 打开文件夹选择图片
        self.selectPicture.clicked.connect(self.open_img)
        # 点击按钮，实现第一个程序的运行
        self.Way1.clicked.connect(self.button_clicked1)
        self.Way2.clicked.connect(self.button_clicked2)
        self.Way3.clicked.connect(self.button_clicked3)
        self.Way4.clicked.connect(self.button_clicked4)
        self.Way5.clicked.connect(self.button_clicked5)

    def button_clicked1(self):
        print("方法一被点击了！")
        action.ActionFunction1(self)

    def button_clicked2(self):
        print("方法二被点击了！")
        action.ActionFunction2(self)

    def button_clicked3(self):
        print("方法三被点击了！")
        action.ActionFunction3(self)

    def button_clicked4(self):
        print("方法四被点击了！")
        action.ActionFunction4(self)

    def button_clicked5(self):
        print("方法五被点击了！")
        action.ActionFunction5(self)

    def open_img(self):
        frame, _ = QFileDialog.getOpenFileName(self, '打开文件', 'F:/', '图像文件(*.jpg *.png *.bmp)')
        self.blurlabel.setScaledContents(True)  # 图片自适应label大小
        self.blurlabel.setPixmap(QPixmap(frame))  # 显示图片在label上
