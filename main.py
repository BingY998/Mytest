import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5 import uic

# class Stats:
#
#     def __init__(self):
#         # 从文件中加载UI定义
#         self.Window = uic.loadUi("deblur_ui.ui")
import deblur_ui
from mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()  # 实例化业务逻辑类
    # ui = deblur_ui.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    mainWin.show()
    sys.exit(app.exec_())  # 循环退出程序
