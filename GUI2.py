import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    # 基本配置不动，然后只动第三个界面
    def __init__(self):
        # 初始化界面
        super().__init__()
        self.setWindowTitle('火灾检测系统')
        self.resize(1200, 800)
        central_widget = QWidget()

        vbox = QVBoxLayout()

        button = QPushButton('BUTTON')

        vbox.addWidget(button)

        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())