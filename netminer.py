import sys

from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow

from config import CONTENT_DIR
from src.move_widget import MoveWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(MoveWidget(CONTENT_DIR))
        self.setWindowTitle("NetMiner - сдаём сети на изи")
        self.setWindowIcon(QIcon("icon.png"))

    def keyPressEvent(self, a0: QKeyEvent):
        self.centralWidget().key_press(a0.key())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
