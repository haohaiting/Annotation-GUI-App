# import basic libraries
import sys
import os
import json
import re
import time
import numpy as np

# import PyQt5 libraries
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

# import custom classes
from main_ui import Ui_MainWindow
from canvas import Canvas


__appname__ = "Car Crash Annotation GUI Tool"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(__appname__)

        # ==================================================
        # ui-related...
        # ==================================================

        self.canvas = Canvas(self.scrollArea)
        self.canvas.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.canvas)

        self.emsg = QErrorMessage()
        self.emsg.setWindowModality(Qt.WindowModal)

        self.labelCoordinates = QLabel(' ')
        self.statusBar().addPermanentWidget(self.labelCoordinates)

        # ==================================================
        # settings
        # ==================================================

        self.dir_name = None
        # self.save_dir = "./output/"
        self.save_path = None
        self.files = []
        self.draw = False

        # check status
        self.savedBasicInfo = False
        self.savedObjects = False

        # ==================================================
        # left
        # ==================================================

        self.OpenDirBtn.pressed.connect(self.open_dir)
        self.NewBoxBtn.pressed.connect(self.create_box)

        self.egoReason_comboBox.activated.connect(self.addEgoReason)
        # self.delEgoReasonBtn.pressed.connect(self.delEgoReason)
        self.basicEditBtn.pressed.connect(self.editBasicInfo)
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

        # right
        # ==================================================

        self.objReason_comboBox.activated.connect(self.addObjReason)
        # self.delObjReasonBtn.pressed.connect(self.delObjReason)

        # self.resetObjBtn.pressed.connect(self.resetObj)
        self.addObjBtn.pressed.connect(self.addObjToList)

        # self.delObjBtn.pressed.connect(self.delObjFromList)
        self.editObjBtn.pressed.connect(self.editObjInList)
        self.saveObjBtn.pressed.connect(self.saveObj)

    # ==================================================
    # open directory, load images
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
                self.emsg.showMessage("No .jpg images in this directory.")
                print("Error: No .jpg images in this directory.")
            else:
                print("Open Directory: ", self.dir_name)

                # handle save path
                save_filename = self.dir_name.split("/")[-1] + '.txt'
                self.save_path = "/".join((self.dir_name, save_filename))
                if os.path.exists(self.save_path):
                    with open(self.save_path) as f:
                        lines = f.readlines()
                        if lines[-1].startswith("0"):
                            self.loadBasicInfo(lines[-1])

                # load images
                self.load_images()

            # update the window title
            self.setWindowTitle(__appname__ + " ---- " + self.dir_name)
            self.OpenDirBtn.setCheckable(False)

        else:
            self.OpenDirBtn.setCheckable(False)

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
        pixmap = QPixmap(path)
        scaledPixmap = pixmap.scaled(
            self.scrollArea.size(),
            Qt.KeepAspectRatio)
        self.canvas.setPixmap(scaledPixmap)

        # help for calculate the real coordinates of the bounding box
        self.canvas.originalWidth = pixmap.size().width()
        self.canvas.originalHeight = pixmap.size().height()

        # print("Original Pixmap--- Width: ", pixmap.size().width(),
        #       "Height: ", pixmap.size().height())
        # print("Scaled Pixmap --- Width: ", self.canvas.pixmap().size().width(), 
        #       "Height: ", self.canvas.pixmap().size().height())
        # print("Scroll --- Width: ", self.scrollArea.width(), 
        #       "Height: ", self.scrollArea.height())
        # print("Offset -- XOffset: ", 
        #       (self.canvas.pixmap().size().width() - self.scrollArea.width()) / 2,
        #     "YOffset: ", 
        #       (self.canvas.pixmap().size().height() - self.scrollArea.height()) / 2)

        # refresh
        self.load_bbox()
        self.canvas.repaint()

    def list_images(self):
        self.fileListWidget.clear()
        self.fileListWidget.addItems(self.files)
        self.fileListWidget.setCurrentRow(0)

    def fileitemDoubleClicked(self, item=None):
        self.load_image(item)

    # buttons' function under image ==============================================

    def prev(self, n=1):
        """Show previous image in the folder.
        When n = 1, show the previous one image.
        """
        if len(self.files) == 0:
            return

        if self.fileListWidget.currentRow() - n >= 0:
            self.fileListWidget.setCurrentRow(
                self.fileListWidget.currentRow()-n)
        self.load_image(self.fileListWidget.currentItem())

    def next(self, n=1):
        """Show next image in the folder.
        When n = 1, show the next ONE image.
        """
        if len(self.files) == 0:
            return

        if self.fileListWidget.currentRow() + n < len(self.files):
            self.fileListWidget.setCurrentRow(
                self.fileListWidget.currentRow()+n)

        self.load_image(self.fileListWidget.currentItem())

    def fillFrame(self, label_name):
        """Fill the frame information using the current 
        frame num by clicking buttons.
        """
        if len(self.files) == 0:
            return

        if len(self.files) != 0:
            frame_num = self.fileListWidget.currentItem().text().split(".")[0]
            if label_name == "start":
                self.startFrame_lineEdit.setText(frame_num)
                self.startFrame_lineEdit.update()
                print("Set clip start frame as ", frame_num)
            elif label_name == "end":
                self.endFrame_lineEdit.setText(frame_num)
                self.endFrame_lineEdit.update()
                print("Set clip end frame as ", frame_num)
            elif label_name == "crash":
                self.crashStartFrame_lineEdit.setText(frame_num)
                self.crashStartFrame_lineEdit.update()
                print("Set crash start frame as ", frame_num)

    def addEgoReason(self):
        # get all current items
        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())
        # check if the reason has been selected
        activated_reason = self.egoReason_comboBox.currentText()
        if activated_reason not in all_items:
            # if it's a new reason, add to the reason list
            self.EgoReasonList.addItem(activated_reason)
            print("Add a new reason for ego car: ", activated_reason)
            self.setStatusTip(
                "Add a new reason for current ego car: " + activated_reason)
        else:
            print("The reason exists in the reason list.")
            self.setStatusTip(
                "The reason exists in the reason list for this ego car.")

    # Handle by key event
    # def delEgoReason(self):
    #     # if there is selected reason in the reason list
    #     if self.EgoReasonList.selectedItems():
    #         # remove the reason from the list
    #         selected_reason = self.EgoReasonList.row(
    #             self.EgoReasonList.selectedItems()[0])
    #         self.EgoReasonList.takeItem(selected_reason)
    #         print("Delete reason: ", selected_reason)
    #     else:
    #         print("No reason selected. Delete nothing.")

    # Save Basic Info ============================================================

    def checkBasicInfo(self, all_reasons):
        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())

        # check if the information is complete
        if self.startFrame_lineEdit.text() is not None \
                and self.crashStartFrame_lineEdit.text() is not None \
                and self.endFrame_lineEdit.text() is not None \
                and self.ifDay_comboBox.currentText() is not None \
                and self.weather_comboBox.currentText() is not None \
                and self.ifEgo_comboBox.currentText() is not None \
                and all_items != []:

            # check the format pattern
            pattern = "^0\d{5}$"
            start = re.match(pattern, self.startFrame_lineEdit.text())
            crash = re.match(pattern, self.crashStartFrame_lineEdit.text())
            end = re.match(pattern, self.endFrame_lineEdit.text())
            if start and crash and end:
                print("[Checked] Frame format is good.")
            else:
                self.emsg.showMessage("The format of frames seems wrong.")
                print("[Error] Save Failed: The format of frames seems wrong.")
                return False
            
            # check the format sequence
            if self.startFrame_lineEdit.text() < self.crashStartFrame_lineEdit.text() <= self.endFrame_lineEdit.text():
                print("[Checked] Frame sequence is good.")
            else:
                self.emsg.showMessage("The sequence of frames seems wrong.")
                print("[Error] Save Failed: frame numbers are wrong.")
                return False
            
            if int(self.crashStartFrame_lineEdit.text()) - int(self.startFrame_lineEdit.text()) < 30:
                self.emsg.showMessage("No more than 3s before car crash.")
                print("[Error] Save Failed: No more than 3s before car crash..")
                return False

            if os.path.exists(self.save_path):
                with open(self.save_path) as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith("0"):
                            if int(line.split(",")[0]) <= int(self.startFrame_lineEdit.text()) <= int(line.split(",")[2]) or \
                            int(line.split(",")[0]) <= int(self.endFrame_lineEdit.text()) <= int(line.split(",")[2]):
                                self.emsg.showMessage(
                                    "The frames are overlapped with a saved clip, please check.")
                                print("[Error] Save Failed: frame overlapped with saved ones.")
                                return False

            # check 
            if self.ifEgo_comboBox.currentText() == "No":
                if len(all_reasons) != 1 or all_reasons[0] != "None":
                    self.emsg.showMessage(
                        "Reason should be 'None' if ego car not involved.")
                    print(
                        "[Error] Reason should be 'None' if ego car is not involved.")
            else:
                if "None" in all_reasons:
                    self.emsg.showMessage(
                        "Reason should not be 'None' if ego car is involved.")
                    print(
                        "[Error] Save Failed: Reason should not include 'None' if ego car is involved.")
        else:
            self.emsg.showMessage("Basic information is not complete!")
            print("[Error] Save Failed: basic information is not completed.")
            return False
        return True

    def saveBasicInfo(self):
        if not self.dir_name:
            self.emsg.showMessage(
                "Please load images first.")
            return

        all_items = []
        for idx in range(self.EgoReasonList.count()):
            all_items.append(self.EgoReasonList.item(idx).text())

        mode = 'a' if os.path.exists(self.save_path) else 'w'
        # if pass all the check
        if self.checkBasicInfo(all_items):
            with open(self.save_path, mode) as f:
                basicInfo = ",".join((self.startFrame_lineEdit.text(),
                                    self.crashStartFrame_lineEdit.text(),
                                    self.endFrame_lineEdit.text(),
                                    self.ifDay_comboBox.currentText(),
                                    self.weather_comboBox.currentText(),
                                    self.ifEgo_comboBox.currentText(),
                                    str(all_items)))
                f.write(basicInfo)
                f.write("\n")

            # disable editing
            self.setEnabledBasicInfo(False)

            # boolean var
            self.savedBasicInfo = True

            # status info
            print("[Success] Saved basic information!")
            self.setStatusTip(
                "The reason exists in the reason list for this ego car.")

            # data = json.dump(basicInfo, f)

    def editBasicInfo(self):

        if self.savedBasicInfo:

            # reset objects related contents
            self.resetObj()
            self.resetObjList()

            # delete previous record
            beginning = ",".join((self.startFrame_lineEdit.text(),
                                 self.crashStartFrame_lineEdit.text(),
                                 self.endFrame_lineEdit.text()))
            
            with open(self.save_path, "r") as f:
                lines = f.readlines()
                lines.reverse()
                for i in range(len(lines)):
                    if lines[i].startswith(beginning):
                        for j in range(0, i+1):
                            del lines[j]
                    break
                lines.reverse()
                
            with open(self.save_path, "w") as f:
                for line in lines:
                    f.write(line)

            # enable editing
            self.setEnabledBasicInfo(True)
            # boolean var
            self.saveBasicInfo = False

            # status info
            print("[Success] Edit Basic Information Form.")
        else:
            pass

    def loadBasicInfo(self, line):
        # reset objects related contents
        self.resetObj()
        self.resetObjList()
        # disable editing
        self.setEnabledBasicInfo(False)
        # boolean var
        self.savedBasicInfo = True

        # load all the info
        info = line.strip().split(",")

        self.startFrame_lineEdit.setText(info[0])
        self.crashStartFrame_lineEdit.setText(info[1])
        self.endFrame_lineEdit.setText(info[2])

        day_idx = self.ifDay_comboBox.findText(
            info[3], Qt.MatchFixedString)
        if day_idx >= 0:
            self.ifDay_comboBox.setCurrentIndex(day_idx)

        weather_idx = self.weather_comboBox.findText(
            info[4], Qt.MatchFixedString)
        if weather_idx >= 0:
            self.weather_comboBox.setCurrentIndex(weather_idx)

        ego_idx = self.egoReason_comboBox.findText(
            info[5], Qt.MatchFixedString)
        if ego_idx >= 0:
            self.egoReason_comboBox.setCurrentIndex(ego_idx)

        self.EgoReasonList.clear()
        if len(info) == 7:
            reasons = eval(info[6])
        else:
            reasons = eval(",".join(info[6:]))
        for reason in reasons:
            self.EgoReasonList.addItem(reason)

    def setEnabledBasicInfo(self, state):
        self.startFrame_lineEdit.setEnabled(state)
        self.crashStartFrame_lineEdit.setEnabled(state)
        self.endFrame_lineEdit.setEnabled(state)
        self.ifDay_comboBox.setEnabled(state)
        self.weather_comboBox.setEnabled(state)
        self.ifEgo_comboBox.setEnabled(state)
        self.egoReason_comboBox.setEnabled(state)
        self.basicSaveBtn.setEnabled(state)
        self.EgoReasonList.setEnabled(state)

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
        if activated_reason not in all_items:
            # if it's a new reason, add to the reason list
            self.objReasonList.addItem(activated_reason)
            print("Add a new reason for current object: ", activated_reason)
            self.setStatusTip(
                "Add a new reason for current object: " + activated_reason)
        else:
            print("The reason exists in the reason list for current object.")
            self.setStatusTip(
                "The reason exists in the reason list for current object.")

    # Handle by key_event
    # def delObjReason(self):
    #     # if there is selected reason in the reason list
    #     if self.objReasonList.selectedItems():
    #         # remove the reason from the list
    #         selected_reason = self.objReasonList.row(
    #             self.objReasonList.selectedItems()[0])
    #         self.objReasonList.takeItem(selected_reason)
    #         print("Delete reason: ", selected_reason)

    # Bounding Box =====================================================================

    def create_box(self):
        if not self.savedBasicInfo:
            self.emsg.showMessage(
                "Please finish the basic info first.")
            return
        
        self.scrollArea.viewport().setProperty(
            "cursor", QCursor(Qt.CrossCursor))
        # self.setStatusTip(
        #     "Drag on the frame to create a bounding box...")
        self.canvas.drawing = True

    def add_bbox(self, coordinates):
        frame_num = self.fileListWidget.currentItem().text().split(".")[0]
        pattern = "^0\d{5}$"
        frame_match = re.match(pattern, frame_num)
        if not frame_match:
            self.emsg.showMessage(
                "Please check the frame name.")
            return

        rowCount = self.bbox_tableWidget.rowCount()

        frame_list = []
        for i in range(0, rowCount):
            frame_list.append(self.bbox_tableWidget.item(i, 0).text())

        if frame_num in frame_list:
            self.bbox_tableWidget.setItem(
                frame_list.index(frame_num), 1,
                QTableWidgetItem(str(coordinates)))
            print("Update bounding box of current object for frame " + frame_num)
            self.setStatusTip(
                "Update bounding box of current object for frame " + frame_num)
        else:
            self.bbox_tableWidget.insertRow(rowCount)
            self.bbox_tableWidget.setItem(
                rowCount, 0, QTableWidgetItem(frame_num))
            self.bbox_tableWidget.setItem(
                rowCount, 1, QTableWidgetItem(str(coordinates)))
            print("Created a bounding box of current object for frame " + frame_num)
            self.setStatusTip(
                "Created a bounding box of current object for frame " + frame_num)

    def load_bbox(self):
        frame_num = self.fileListWidget.currentItem().text().split(".")[0]
        print(frame_num)
        rowCount = self.bbox_tableWidget.rowCount()

        # if the frame is labelled, load the bounding box of current object
        for i in range(0, rowCount):
            if frame_num == self.bbox_tableWidget.item(i, 0).text():
                bbox = eval(self.bbox_tableWidget.item(i, 1).text())
                self.canvas.top_left = QPoint(bbox[0], bbox[1])
                self.canvas.bottom_right = QPoint(bbox[2], bbox[3])
                print(self.canvas.top_left, self.canvas.bottom_right)
                self.canvas.transformToShowPoints()
                print(self.canvas.show_top_left, self.canvas.show_bottom_right)
                self.canvas.load = True
                return

        # otherwise, no bounding box to show
        print("YES")
        self.canvas.show_top_left = QPoint()
        self.canvas.show_bottom_right = QPoint()
        self.canvas.load = True


    # Objects-related buttons ============================================================

    def addObjToList(self):
        if not self.savedBasicInfo:
            self.emsg.showMessage(
                "Please finish the basic info first.")
            return

        _type = self.objTypes_comboBox.currentText()
        _ifobj = self.ifObj_comboBox.currentText()

        all_reasons = []
        for idx in range(self.objReasonList.count()):
            all_reasons.append(self.objReasonList.item(idx).text())

        if len(all_reasons) == 0:
            self.emsg.showMessage(
                "Please select at least one reason for this object.")
            return

        # get bouding boxes in sort
        bboxes, mydict = {}, {}
        rowCount = self.bbox_tableWidget.rowCount()
        for row in range(rowCount):
            frame_num = self.bbox_tableWidget.item(row, 0).text()
            bbox = self.bbox_tableWidget.item(row, 1).text()
            mydict[frame_num] = bbox
        for key in sorted(mydict):
            bboxes[key] = mydict[key]

        crash = int(self.crashStartFrame_lineEdit.text())
        valid_frame_list = []
        for i in range(9, -1, -1):
            valid_frame_list.append(str("%06d" % (crash - i * 5)))
        print(valid_frame_list)
        
        if _ifobj == "Yes":
            if len(bboxes) < 6:
                self.emsg.showMessage(
                    "Please label at least 6 frames for this objects.")
                return
            elif set(bboxes.keys()) - set(valid_frame_list) != set():
                self.emsg.showMessage(
                    "The labelled frames are not the required ones based on car crash start frame, please check.")
                return
            elif self.crashStartFrame_lineEdit.text() not in bboxes.keys():
                self.emsg.showMessage(
                    "The labelled frame doesn't include crash start frame.")
                return
            elif np.count_nonzero(np.diff(sorted(np.asarray(list(bboxes.keys()), dtype=int))) == 5) != len(bboxes) - 1:
                self.emsg.showMessage(
                    "Please check the interval of the frames")
                return
        else:
            if set(bboxes.keys()) - set(valid_frame_list) != set():
                self.emsg.showMessage(
                    "The labelled frames are not the required ones based on car crash start frame, please check.")
                return

        rowPos = self.obj_tableWidget.rowCount()
        self.obj_tableWidget.insertRow(rowPos)
        self.obj_tableWidget.setItem(
            rowPos, 0, QTableWidgetItem(_type))
        self.obj_tableWidget.setItem(
            rowPos, 1, QTableWidgetItem(_ifobj))
        self.obj_tableWidget.setItem(
            rowPos, 2, QTableWidgetItem(str(all_reasons)))
        self.obj_tableWidget.setItem(
            rowPos, 3, QTableWidgetItem(str(bboxes)))

        print("Successfully add an object to object list!")
        self.setStatusTip("Successfully add an object to object list!")
        self.resetObj()

    def editObjInList(self):
        if len(self.obj_tableWidget.selectedItems()) == 0:
            return
        else:
            self.resetObj()
                
            # object type
            _type = self.obj_tableWidget.item(
                self.row(self.selectedItems()[0]), 0).text()
            type_idx = self.objTypes_comboBox.findText(
                _type, Qt.MatchFixedString)
            if type_idx >= 0:
                self.objTypes_comboBox.setCurrentIndex(type_idx)

            # if invovled
            _ifobj = self.obj_tableWidget.item(
                self.row(self.selectedItems()[0]), 1).text()
            if_idx = self.ifObj_comboBox.findText(
                _ifobj, Qt.MatchFixedString)
            if if_idx >= 0:
                self.ifObj_comboBox.setCurrentIndex(if_idx)
            
            # reasons
            _reasons = eval(self.obj_tableWidget.item(
                self.row(self.selectedItems()[0]), 2).text())
            for reason in _reasons:
                self.objReasonList.addItem(reason)

            # bounding box
            _bboxes = eval(self.obj_tableWidget.item(
                self.row(self.selectedItems()[0]), 3).text())

            for frame in _bboxes:
                rowCount = self.bbox_tableWidget.rowCount()
                self.bbox_tableWidget.insertRow(rowCount)
                self.bbox_tableWidget.setItem(
                    rowCount, 0, QTableWidgetItem(frame))
                self.bbox_tableWidget.setItem(
                    rowCount, 1, QTableWidgetItem(_bboxes[frame]))

            self.removeRow(self.row(self.selectedItems()[0]))

            print("[Edit Item]")

    def saveObj(self):
        if not self.savedBasicInfo:
            self.emsg.showMessage(
                "Please finish the basic info first.")
            return

        rowCount = self.obj_tableWidget.rowCount()
        # print(rowCount)

        # check num of objects
        if rowCount == 0:
            self.emsg.showMessage(
                "You need to at least label one object.")
            return

        # check if contains objects involved
        if_list = []
        for i in range(rowCount):
            if_list.append(self.obj_tableWidget.item(i, 1).text())
        # print(if_list)

        if if_list.count("Yes") == 0:
            self.emsg.showMessage(
                "You need to at least label one object involved in the car accident.")
            return
        elif self.ifEgo_comboBox.currentText() == "No" and if_list.count("Yes") < 2:
            self.emsg.showMessage(
                "If ego car is not involved, you need to label at least two other involved objects.")
            return

        for row in range(rowCount):
            with open(self.save_path, 'a') as f:
                one_obj = ",".join((self.obj_tableWidget.item(row, 0).text(),
                                    self.obj_tableWidget.item(row, 1).text(),
                                    self.obj_tableWidget.item(row, 2).text(),
                                    self.obj_tableWidget.item(row, 3).text(),
                                    ))
                f.write(one_obj)
                f.write("\n")
                print("[Success] Saved objects!")
                self.savedObjects = True

        if self.savedObjects:
            self.resetAll()

    # reset ================================================================================

    def resetAll(self):
        self.resetBasicInfo()
        self.resetObj()
        self.resetObjList()
        self.savedObjects = False
        print("[Success] Reset Objects List!")

    def resetBasicInfo(self):
        # clear all
        self.startFrame_lineEdit.clear()
        self.crashStartFrame_lineEdit.clear()
        self.endFrame_lineEdit.clear()
        self.ifDay_comboBox.setCurrentIndex(0)
        self.weather_comboBox.setCurrentIndex(0)
        self.ifEgo_comboBox.setCurrentIndex(0)
        self.EgoReasonList.clear()
        # enable editing
        self.setEnabledBasicInfo(True)
        # boolean var
        self.saveBasicInfo = False

    def resetObj(self):
        self.objTypes_comboBox.setCurrentIndex(0)
        self.ifObj_comboBox.setCurrentIndex(0)
        self.objReason_comboBox.setCurrentIndex(0)
        self.objReasonList.clear()
        for i in range(1, self.bbox_tableWidget.rowCount()):
            self.bbox_tableWidget.removeRow(i)
        self.bbox_tableWidget.setRowCount(0)
        print("[Success] Reset Object Form.")

    def resetObjList(self):
        for i in range(1, self.obj_tableWidget.rowCount()):
            self.obj_tableWidget.removeRow(i)
        self.obj_tableWidget.setRowCount(0)

    # events ==============================================================================

    def mouseReleaseEvent(self, event):
        coordinates = [self.canvas.top_left.x(), 
                       self.canvas.top_left.y(),
                       self.canvas.bottom_right.x(),
                       self.canvas.bottom_right.y()]

        if coordinates[0] != coordinates[2] and \
            coordinates[1] != coordinates[3]:
            self.add_bbox(coordinates)
            print("Add bouding box: ", coordinates)
            self.setStatusTip("Add bounding box: " + str(coordinates))
            self.canvas.top_left = QPoint()
            self.canvas.bottom_right = QPoint()
            self.scrollArea.viewport().setProperty(
            "cursor", QCursor(Qt.ArrowCursor))
        else:
            self.scrollArea.viewport().setProperty(
            "cursor", QCursor(Qt.ArrowCursor))
            pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
