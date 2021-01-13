import sys

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow

from move_widget import MoveWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(MoveWidget("content"))

    def keyPressEvent(self, a0: QKeyEvent):
        self.centralWidget().key_press(a0.key())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
