from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic # User Interface Compiler

class MyGUI(QMainWindow): 

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('Simple-GUI-Text-Editor/Editor.ui', self)
        self.show()

def main():
    app = QApplication([])
    windows = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()