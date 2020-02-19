# import basic libraries
import sys
import os

# import PyQt5 libraries
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# import custom classes
from main_ui import Ui_MainWindow

__appname__ = "Car Crash Annotation GUI Tool"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.dir_name = None
        self.files = []

        self.OpenDirBtn.pressed.connect(self.openDir)

    def openDir(self):
        # wait user choose a directory
        self.get_dir()
        # chekc all the .jpg files in that directory
        self.scan_dir()

        if len(self.files) == 0:
            QErrorMessage("No .jpg images in this directory.")
            print("Error!")  # no .jpg files
        else:
            self.load_images()

        # update the window title
        self.setWindowTitle(__appname__ + " ---- " + self.dir_name)
    
    def get_dir(self):
        w = QWidget()
        w.resize(320, 240)
        # open directory from current directory
        if self.dir_name is None:
            self.dir_name = QFileDialog.getExistingDirectory(
                w, 'Open File', './')
        else:
            self.dir_name = QFileDialog.getExistingDirectory(
                w, 'Open File', self.dir_name)

    def scan_dir(self):
        self.files = os.listdir(self.dir_name)
        for file in self.files:
            # all the frame files are .jpg file
            if not file.endswith('jpg'):
                self.files.remove(file)

    def load_images(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
