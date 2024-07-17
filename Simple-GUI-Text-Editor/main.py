from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic # User Interface Compiler

class MyGUI(QMainWindow): 

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('Simple-GUI-Text-Editor/Editor.ui', self)
        self.show()

        # Set windows title name and font-size actions
        self.setWindowTitle("Notepad - Simple GUI Text Editor")
        self.action12_pt.triggered.connect(lambda: self.change_font_size(12))
        self.action18_pt.triggered.connect(lambda: self.change_font_size(18))
        self.action24_pt.triggered.connect(lambda: self.change_font_size(24))

        # Set action when user clicks on "Open"
        self.actionOpen.triggered.connect(self.open_file)

    # Font-size change function, takes size as argument
    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))
    
    # Open file function 
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options = options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

def main():
    app = QApplication([])
    windows = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()