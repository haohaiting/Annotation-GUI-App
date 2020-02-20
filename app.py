# import basic libraries
import sys
import os
import json

# import PyQt5 libraries
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

# import custom classes
from main_ui import Ui_MainWindow


__appname__ = "Car Crash Annotation GUI Tool"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(__appname__)

        self.dir_name = None
        self.save_dir = "./output/"
        self.save_filename = None
        self.files = []

        # ==================================================
        # left
        # ==================================================

        self.OpenDirBtn.pressed.connect(self.open_dir)
        self.NewBoxBtn.pressed.connect(self.create_box)

        self.egoReason_comboBox.activated.connect(self.addEgoReason)
        self.delEgoReasonBtn.pressed.connect(self.delEgoReason)
        self.basicResetBtn.pressed.connect(self.resetBasicInfo)
        self.basicSaveBtn.pressed.connect(self.saveBasicInfo)

        self.fileListWidget.itemDoubleClicked.connect(
            self.fileitemDoubleClicked)

        # ==================================================
        # middle
        # ==================================================
        self.prev5Btn.pressed.connect(lambda x=5: self.prev(x))
        self.prevBtn.pressed.connect(self.prev)
        self.next5Btn.pressed.connect(lambda x=5: self.next(x))
        self.nextBtn.pressed.connect(self.next)

        self.setStartBtn.pressed.connect(
            lambda x="start": self.fillFrame(x))
        self.setEndBtn.pressed.connect(
            lambda x="end": self.fillFrame(x))
        self.setCrashStartBtn.pressed.connect(
            lambda x="crash": self.fillFrame(x))

        # ==================================================
        # right
        # ==================================================

        self.objReason_comboBox.activated.connect(self.addObjReason)
        self.delObjReasonBtn.pressed.connect(self.delObjReason)

        self.resetObjBtn.pressed.connect(self.resetObj)
        self.addObjBtn.pressed.connect(self.addObjToList)
    
        self.delObjBtn.pressed.connect(self.delObjFromList)
        self.editObjBtn.pressed.connect(self.editObjInList)
        self.saveObjBtn.pressed.connect(self.saveObj)

    # ==================================================
    # open directory
    # load images
    # list all the images in the directory
    # click image in the list, show the image
    # ==================================================

    def open_dir(self):
        # wait user choose a directory
        self.get_dir()
        # chekc all the .jpg files in that directory
        if self.dir_name != None and self.dir_name != '':
            self.scan_dir()
            if len(self.files) == 0:
                # QErrorMessage.showMessage("No .jpg images in this directory.")
                print("Error!")  # no .jpg files
            else:
                print("Open Directory: ", self.dir_name)
                self.save_filename = self.dir_name.split("/")[-1] + '.txt'
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
            # all the frame files in this project are .jpg files
            if not file.endswith('.jpg'):
                self.files.remove(file)
        self.files = sorted(self.files)

    def load_images(self):
        self.list_images()
        self.load_image(self.fileListWidget.currentItem())
    
    def load_image(self, item):
        path = "/".join((self.dir_name, item.text()))
        print("Load...", path)
        self.pixMap = QPixmap(path)
        self.imageLabel.setPixmap(self.pixMap)
    
    def list_images(self):
        self.fileListWidget.clear()
        self.fileListWidget.addItems(self.files)
        self.fileListWidget.setCurrentRow(0)
    
    def fileitemDoubleClicked(self, item=None):
        self.load_image(item)

    def prev(self, n=1):
        if self.fileListWidget.currentRow() - n >= 0:
            self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow()-n)
            self.load_image(self.fileListWidget.currentItem())

    def next(self, n=1):
        if self.fileListWidget.currentRow() + n < len(self.files):
            self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow()+n)
            self.load_image(self.fileListWidget.currentItem())
    
    def fillFrame(self, label_name):
        if len(self.files) != 0:
            frame_num = self.fileListWidget.currentItem().text().split(".")[0]
            if label_name == "start":
                self.startFrame_lineEdit.setText(frame_num)
                print("Set clip start frame as ", frame_num)
            elif label_name == "end":
                self.endFrame_lineEdit.setText(frame_num)
                print("Set clip end frame as ", frame_num)
            elif label_name == "crash":
                self.crashStartFrame_lineEdit.setText(frame_num)
                print("Set crash start frame as ", frame_num)
    
    def addEgoReason(self):
        # get all current items
        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())
        # check if the reason has been selected
        activated_reason = self.egoReason_comboBox.currentText()
        print(activated_reason)
        if activated_reason not in all_items:
            # if it's a new reason, add to the reason list
            self.EgoReasonList.addItem(activated_reason)
            print("Add a new reason for ego car: ", activated_reason)
        else:
            print("The reason exists in the reason list.")
    
    def delEgoReason(self):
        # if there is selected reason in the reason list
        if self.EgoReasonList.selectedItems():
            # remove the reason from the list
            selected_reason = self.EgoReasonList.row(
                self.EgoReasonList.selectedItems()[0])
            self.EgoReasonList.takeItem(selected_reason)
            print("Delete reason: ", selected_reason)
        else:
            print("No reason selected. Delete nothing.")
    
    def checkBasicInfo(self):
        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())

        if self.startFrame_lineEdit.text() is not None \
            and self.crashStartFrame_lineEdit.text() is not None \
            and self.endFrame_lineEdit.text() is not None \
            and self.ifDay_comboBox.currentText() is not None \
            and self.weather_comboBox.currentText() is not None \
            and self.ifEgo_comboBox.currentText() is not None \
            and all_items != []:
            if self.startFrame_lineEdit.text() < self.crashStartFrame_lineEdit.text() < self.endFrame_lineEdit.text():
                print("Frame sequence is good.")
            else:
                # QErrorMessage.showMessage("Check frame numbers, pls!")
                print("[Error]Save Failed: frame numbers are wrong.")
        else:
            # QErrorMessage.showMessage("Basic Information Not Complete!")
            print("[Error]Save Failed: basic information is not completed.")
        return True

    def saveBasicInfo(self):
        save_path = "/".join((self.save_dir, self.save_filename))

        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())

        if self.checkBasicInfo():
            with open(save_path, 'w') as f:
                basicInfo = ",".join((self.startFrame_lineEdit.text(),
                                      self.crashStartFrame_lineEdit.text(),
                                      self.endFrame_lineEdit.text(),
                                      self.ifDay_comboBox.currentText(),
                                      self.weather_comboBox.currentText(),
                                      self.ifEgo_comboBox.currentText(),
                                      str(all_items)))
                f.write(basicInfo)
                f.write("\n")
                print("[Success] Saved basic information!")
                # data = json.dump(basicInfo, f)

    def resetBasicInfo(self):
        print("Clicked Reset Button for Basic Information.")


    # ==================================================
    # objects related
    # ==================================================

    def addObjReason(self):
        # get all current items
        all_items = []
        for idx in range(self.objReasonList.count()):
            all_items.append(self.objReasonList.item(idx).text())
        # check if the reason has been selected
        activated_reason = self.objReason_comboBox.currentText()
        print(activated_reason)
        if activated_reason not in all_items:
            # if it's a new reason, add to the reason list
            self.objReasonList.addItem(activated_reason)
            print("Add a new reason for current object: ", activated_reason)
        else:
            print("The reason exists in the reason list.")

    def delObjReason(self):
        # if there is selected reason in the reason list
        if self.objReasonList.selectedItems():
            # remove the reason from the list
            selected_reason = self.objReasonList.row(
                self.objReasonList.selectedItems()[0])
            self.objReasonList.takeItem(selected_reason)
            print("Delete reason: ", selected_reason)
        else:
            print("No reason selected. Delete nothing.")

    def resetObj(self):
        print("Clicked reset object button!")
    
    def addObjToList(self):
        print("Clicked add object button!")

    def delObjFromList(self):
        print("Clicked del object button!")

    def editObjInList(self):
        print("Trying to edit object in list!")

    def saveObj(self):
        print("Trying to save objects for current clip!")

    def create_box(self):
        # create painter instance with pixmap
        self.painterInstance = QPainter(self.pixMap)

        # set rectangle color and thickness
        self.penRectangle = QPen(Qt.red)
        self.penRectangle.setWidth(3)

        # draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(100, 100, 50, 50)

        # set pixmap onto the label widget
        self.imageLabel.setPixmap(self.pixMap)
        self.imageLabel.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
