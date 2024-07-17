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

        # Set action when user clicks on "Save"
        self.actionSave.triggered.connect(self.save_file)

        # Set action when user clicks on "Exit at top of window"
        self.actionClose.triggered.connect(exit)

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

    # Saves the file, writes to text files folder
    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text File (*.txt);;All Files (*)", options = options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event): # Not custom function, overriding
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole) # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole) # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) # 2

        answer = dialog.exec_()
        
        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()

def main():
    app = QApplication([])
    windows = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()