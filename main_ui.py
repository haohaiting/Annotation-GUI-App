# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class MyQListWidget(QtWidgets.QListWidget):

    def __init__(self, parent):
        super(QtWidgets.QListWidget, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete or event.key() == QtCore.Qt.Key_Backspace:
            self._del_item()

    def _del_item(self):
        # for item in self.selectedItems():
        print("[Delete Reason] " + str(self.selectedItems()[0].text()))
        self.takeItem(self.row(self.selectedItems()[0]))
            

class MyQTableWidget(QtWidgets.QTableWidget):

    def __init__(self, parent):
        super(QtWidgets.QTableWidget, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete or event.key() == QtCore.Qt.Key_Backspace:
            self._del_item()

    def _del_item(self):
        self.removeRow(self.row(self.selectedItems()[0]))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)

        # central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 1, 1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setContentsMargins(0,0,0,0)
        
        # central widget layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # ============================================
        # Left Part
        # ============================================

        self.Left = QtWidgets.QGroupBox(self.centralwidget)
        self.Left.setTitle("")
        self.Left.setObjectName("Left")
        self.Left.setMaximumWidth(300)
        self.leftPart_verticalLayout = QtWidgets.QVBoxLayout(self.Left)
        self.leftPart_verticalLayout.setObjectName("leftPart_verticalLayout")

        # FUNCTIONS
        # open dir, change save dir, create new boxes
        self.Funcitons = QtWidgets.QGroupBox(self.Left)
        self.Funcitons.setTitle("")
        self.Funcitons.setObjectName("Funcitons")

        # set vertival layout
        self.functionBtns_verticalLayout = QtWidgets.QVBoxLayout(self.Funcitons)
        self.functionBtns_verticalLayout.setObjectName(
            "functionBtns_verticalLayout")
        
        # open dir button
        self.OpenDirBtn = QtWidgets.QPushButton(self.Funcitons)
        self.OpenDirBtn.setObjectName("OpenDirBtn")
        self.functionBtns_verticalLayout.addWidget(self.OpenDirBtn)

        # change save dir button
        # self.SaveDirBtn = QtWidgets.QPushButton(self.Funcitons)
        # self.SaveDirBtn.setObjectName("SaveDirBtn")
        # self.verticalLayout.addWidget(self.SaveDirBtn)

        # create new bbox button
        self.NewBoxBtn = QtWidgets.QPushButton(self.Funcitons)
        self.NewBoxBtn.setObjectName("NewBoxBtn")
        self.functionBtns_verticalLayout.addWidget(self.NewBoxBtn)

        # BASIC INFO
        # open dir, change save dir, create new boxes
        self.basicInfoGroup = QtWidgets.QGroupBox(self.Left)
        self.basicInfoGroup.setObjectName("basicInfoGroup")
        self.basicInfo_formLayout = QtWidgets.QFormLayout(self.basicInfoGroup)
        self.basicInfo_formLayout.setObjectName("basicInfo_formLayout")

        # start frame
        self.startFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.startFrame_label.setObjectName("startFrame_label")
        self.basicInfo_formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.startFrame_label)
        self.startFrame_lineEdit = QtWidgets.QLineEdit(self.basicInfoGroup)
        self.startFrame_lineEdit.setObjectName("startFrame_lineEdit")
        self.basicInfo_formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.startFrame_lineEdit)

        # crash start frame
        self.crashStartFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.crashStartFrame_label.setObjectName("crashStartFrame_label")
        self.basicInfo_formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.crashStartFrame_label)
        self.crashStartFrame_lineEdit = QtWidgets.QLineEdit(
            self.basicInfoGroup)
        self.crashStartFrame_lineEdit.setObjectName("crashStartFrame_lineEdit")
        self.basicInfo_formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.crashStartFrame_lineEdit)

        # end frame
        self.endFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.endFrame_label .setObjectName("endFrame_label ")
        self.basicInfo_formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.endFrame_label)
        self.endFrame_lineEdit = QtWidgets.QLineEdit(self.basicInfoGroup)
        self.endFrame_lineEdit.setObjectName("endFrame_lineEdit")
        self.basicInfo_formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.endFrame_lineEdit)

        # horizontal line
        self.line_2 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.basicInfo_formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_2)

        # day or night
        self.ifDay_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifDay_label.setObjectName("ifDay_label")
        self.basicInfo_formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.ifDay_label)
        self.ifDay_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifDay_comboBox.setMinimumWidth(120)
        self.ifDay_comboBox.setObjectName("ifDay_comboBox")
        self.ifDay_comboBox.addItem("")
        self.ifDay_comboBox.addItem("")
        self.basicInfo_formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.ifDay_comboBox)

        # weather
        self.weather_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.weather_label.setObjectName("weather_label")
        self.basicInfo_formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.weather_label)
        self.weather_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.weather_comboBox.setMinimumWidth(120)
        self.weather_comboBox.setObjectName("weather_comboBox")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.basicInfo_formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.weather_comboBox)

        # horizontal line
        self.line_3 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.basicInfo_formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.line_3)

        # if ego involved
        self.ifEgo_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifEgo_label.setObjectName("ifEgo_label")
        self.basicInfo_formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.ifEgo_label)
        self.ifEgo_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifEgo_comboBox.setMinimumWidth(120)
        self.ifEgo_comboBox.setObjectName("ifEgo_comboBox")
        self.ifEgo_comboBox.addItem("")
        self.ifEgo_comboBox.addItem("")
        self.basicInfo_formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.ifEgo_comboBox)

        # ego reason
        self.egoReason_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.egoReason_label.setObjectName("egoReason_label")
        self.basicInfo_formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.egoReason_label)

        self.egoReason_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.egoReason_comboBox.setMinimumWidth(120)
        self.egoReason_comboBox.setObjectName("egoReason_comboBox")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.egoReason_comboBox.addItem("")
        self.basicInfo_formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.egoReason_comboBox)

        # Handle by key_event
        # self.delEgoReasonBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        # self.delEgoReasonBtn.setObjectName("delEgoReasonBtn")
        # self.basicInfo_formLayout.setWidget(
        #     9, QtWidgets.QFormLayout.LabelRole, self.delEgoReasonBtn)


        # The appearance is not good
        # self.reason_note = QtWidgets.QLabel(self.basicInfoGroup)
        # self.reason_note.setObjectName("reasonNote")
        # self.basicInfo_formLayout.setWidget(
        #     9, QtWidgets.QFormLayout.LabelRole, self.reason_note
        # )
        
        self.EgoReasonList = MyQListWidget(self.basicInfoGroup)
        self.EgoReasonList.setObjectName("EgoReasonList")
        self.basicInfo_formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.EgoReasonList)
        
        # basic information related buttons
        # reset button
        self.basicEditBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicEditBtn.setObjectName("basicEditBtn")
        self.basicInfo_formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.basicEditBtn)
        # save button
        self.basicSaveBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicSaveBtn.setEnabled(True)
        self.basicSaveBtn.setObjectName("basicSaveBtn")
        self.basicInfo_formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.basicSaveBtn)
        
        # file list
        self.fileListWidget = QtWidgets.QListWidget()

        # handle layout issue
        self.leftPart_verticalLayout.addWidget(self.Funcitons)
        self.leftPart_verticalLayout.addWidget(self.basicInfoGroup)
        self.leftPart_verticalLayout.addWidget(self.fileListWidget)

        self.horizontalLayout.addWidget(self.Left)

        # ============================================
        # Middle Part
        # ============================================
        self.Middle = QtWidgets.QGroupBox(self.centralwidget)
        # self.Middle.setMinimumSize(QtCore.QSize(800, 0))

        self.Middle.setTitle("")
        self.Middle.setObjectName("Middle")

        self.middle_verticalLayout = QtWidgets.QVBoxLayout(self.Middle)
        self.middle_verticalLayout.setObjectName("middle_verticalLayout")

        # Scroll Area to show images
        self.scrollArea = QtWidgets.QScrollArea(self.Middle)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)

        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 868, 932))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # try to load image using QLabel
        # maybe need canvas here
        # self.imageLabel = QtWidgets.QLabel()
        # self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.scrollArea.setWidget(self.imageLabel)
        self.middle_verticalLayout.addWidget(self.scrollArea)
        
        # control image flow
        self.playImage_groupBox = QtWidgets.QGroupBox(self.Middle)
        self.playImage_groupBox.setTitle("")
        self.playImage_groupBox.setObjectName("playImage_groupBox")
        self.playImageBtns_horizontalLayout = QtWidgets.QHBoxLayout(self.playImage_groupBox)
        self.playImageBtns_horizontalLayout.setObjectName("playImageBtns_horizontalLayout")

        self.prev5Btn = QtWidgets.QPushButton(self.playImage_groupBox)
        self.prev5Btn.setObjectName("prev5Btn")
        self.playImageBtns_horizontalLayout.addWidget(self.prev5Btn)
        self.prevBtn = QtWidgets.QPushButton(self.playImage_groupBox)
        self.prevBtn.setObjectName("prevBtn")
        self.playImageBtns_horizontalLayout.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(self.playImage_groupBox)
        self.nextBtn.setObjectName("nextBtn")
        self.playImageBtns_horizontalLayout.addWidget(self.nextBtn)
        self.next5Btn = QtWidgets.QPushButton(self.playImage_groupBox)
        self.next5Btn.setObjectName("next5Btn")
        self.playImageBtns_horizontalLayout.addWidget(self.next5Btn)

        self.middle_verticalLayout.addWidget(self.playImage_groupBox)
        self.horizontalLayout.addWidget(self.Middle)

        # set image as ...
        self.set_groupBox = QtWidgets.QGroupBox(self.Middle)
        self.set_groupBox.setTitle("")
        self.set_groupBox.setObjectName("set_groupBox")
        self.set_horizontalLayout = QtWidgets.QHBoxLayout(self.set_groupBox)
        self.set_horizontalLayout.setObjectName("set_horizontalLayout")

        self.setStartBtn = QtWidgets.QPushButton(self.set_groupBox)
        self.setStartBtn.setObjectName("setStartBtn")
        self.set_horizontalLayout.addWidget(self.setStartBtn)
        self.setCrashStartBtn = QtWidgets.QPushButton(self.set_groupBox)
        self.setCrashStartBtn.setObjectName("setCrashStartBtn")
        self.set_horizontalLayout.addWidget(self.setCrashStartBtn)
        self.setEndBtn = QtWidgets.QPushButton(self.set_groupBox)
        self.setEndBtn.setObjectName("setEndBtn")
        self.set_horizontalLayout.addWidget(self.setEndBtn)

        self.middle_verticalLayout.addWidget(self.set_groupBox)
        self.horizontalLayout.addWidget(self.Middle)

        # ============================================
        # Right Part
        # ============================================

        self.Right = QtWidgets.QGroupBox(self.centralwidget)
        self.Right.setTitle("")
        self.Right.setObjectName("Right")
        self.Right.setMaximumWidth(300)

        # right part layout
        self.rightPart_verticalLayout = QtWidgets.QVBoxLayout(self.Right)
        self.rightPart_verticalLayout.setObjectName("rightPart_verticalLayout")

        # objects information groupbox
        self.objInfo_groupBox = QtWidgets.QGroupBox(self.Right)
        self.objInfo_groupBox.setObjectName("objInfo_groupBox")
        self.objInfo_formLayout = QtWidgets.QFormLayout(self.objInfo_groupBox)
        self.objInfo_formLayout.setObjectName("objInfo_formLayout")

        self.objType_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.objType_label.setObjectName("objType_label")
        self.objInfo_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.objType_label)

        self.objTypes_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.objTypes_comboBox.setObjectName("objTypes_comboBox")
        self.objTypes_comboBox.setMinimumWidth(120)
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objInfo_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.objTypes_comboBox)

        self.ifObj_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.ifObj_label.setObjectName("ifObj_label")
        self.objInfo_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ifObj_label)

        self.ifObj_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.ifObj_comboBox.setObjectName("ifObj_comboBox")
        self.ifObj_comboBox.setMinimumWidth(120)
        self.ifObj_comboBox.addItem("")
        self.ifObj_comboBox.addItem("")
        self.objInfo_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ifObj_comboBox)

        self.objReason_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.objReason_label.setObjectName("objReason_label")
        self.objInfo_formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.objReason_label)

        self.objReason_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.objReason_comboBox.setObjectName("objReason_comboBox")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objInfo_formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.objReason_comboBox)

        # self.delObjReasonBtn = QtWidgets.QPushButton(self.objInfo_groupBox)
        # self.delObjReasonBtn.setObjectName("delObjReasonBtn")
        # self.objInfo_formLayout.setWidget(
        #     4, QtWidgets.QFormLayout.LabelRole, self.delObjReasonBtn)

        self.objReasonList = MyQListWidget(self.objInfo_groupBox)
        self.objReasonList.setObjectName("objReasonList")
        self.objInfo_formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.objReasonList)
        self.rightPart_verticalLayout.addWidget(self.objInfo_groupBox)
        
        # bounding box

        self.BBox = QtWidgets.QGroupBox(self.objInfo_groupBox)
        self.BBox.setObjectName("BBox")
        self.BBox.setMaximumWidth(250)

        self.bbox_verticalLayout = QtWidgets.QVBoxLayout(self.BBox)
        self.bbox_verticalLayout.setObjectName("verticalLayout")

        self.bbox_label = QtWidgets.QLabel("Bounding Boxes")

        self.bbox_tableWidget = MyQTableWidget(self.objInfo_groupBox)
        self.bbox_tableWidget.setGeometry(QtCore.QRect(30, 200, 256, 192))
        self.bbox_tableWidget.setObjectName("bboxtableWidget")
        self.bbox_tableWidget.setColumnCount(2)
        self.bbox_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bbox_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bbox_tableWidget.setHorizontalHeaderItem(1, item)

        bbox_header = self.bbox_tableWidget.horizontalHeader()
        bbox_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        bbox_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.bbox_verticalLayout.addWidget(self.bbox_label)
        self.bbox_verticalLayout.addWidget(self.bbox_tableWidget)

        self.objInfo_formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.BBox)

        # reset, delete, save button for single object
        self.objBtns_groupBox1 = QtWidgets.QGroupBox(self.Right)
        self.objBtns_groupBox1.setTitle("")
        self.objBtns_groupBox1.setObjectName("objBtns_groupBox1")

        self.objBtns_horizontalLayout1 = QtWidgets.QHBoxLayout(
            self.objBtns_groupBox1)
        self.objBtns_horizontalLayout1.setObjectName("objBtns_horizontalLayout1")

        # self.resetObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox1)
        # self.resetObjBtn.setObjectName("resetObjBtn")
        # self.objBtns_horizontalLayout1.addWidget(self.resetObjBtn)

        # self.delBoxBtn = QtWidgets.QPushButton(self.objBtns_groupBox1)
        # self.delBoxBtn.setObjectName("delBoxBtn")
        # self.objBtns_horizontalLayout1.addWidget(self.delBoxBtn)

        self.addObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox1)
        self.addObjBtn.setObjectName("addObjBtn")
        self.objBtns_horizontalLayout1.addWidget(self.addObjBtn)

        self.rightPart_verticalLayout.addWidget(self.objBtns_groupBox1)
        self.horizontalLayout.addWidget(self.Right)

        # objects list

        self.obj_tableWidget = MyQTableWidget(self.Right)
        self.obj_tableWidget.setGeometry(QtCore.QRect(10, 0, 351, 192))
        self.obj_tableWidget.setObjectName("obj_tableWidget")
        self.obj_tableWidget.setColumnCount(4)
        self.obj_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.obj_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.obj_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.obj_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.obj_tableWidget.setHorizontalHeaderItem(3, item)
        self.rightPart_verticalLayout.addWidget(self.obj_tableWidget)

        obj_header = self.obj_tableWidget.horizontalHeader()
        obj_header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        obj_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        
        # del, edit, save buttons for objects list
        self.objBtns_groupBox2 = QtWidgets.QGroupBox(self.Right)
        self.objBtns_groupBox2.setTitle("")
        self.objBtns_groupBox2.setObjectName("objBtns_groupBox2")

        self.objBtns_horizontalLayout2 = QtWidgets.QHBoxLayout(self.objBtns_groupBox2)
        self.objBtns_horizontalLayout2.setObjectName("objBtns_horizontalLayout2")

        # self.delObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox2)
        # self.delObjBtn.setObjectName("delObjBtn")
        # self.objBtns_horizontalLayout2.addWidget(self.delObjBtn)

        self.editObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox2)
        self.editObjBtn.setObjectName("editObjBtn")
        self.objBtns_horizontalLayout2.addWidget(self.editObjBtn)

        self.saveObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox2)
        self.saveObjBtn.setObjectName("saveObjBtn")
        self.objBtns_horizontalLayout2.addWidget(self.saveObjBtn)

        self.rightPart_verticalLayout.addWidget(self.objBtns_groupBox2)
        self.horizontalLayout.addWidget(self.Right)

        # central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        # self.actionOpen_Directory.triggered.connect(
        #     lambda: self.clicked("Open Dir"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # function buttons
        self.OpenDirBtn.setText(_translate("MainWindow", "Open Dir"))
        self.OpenDirBtn.setStatusTip(
            "Open a frame directory to load all the frames in it. Shortcut [Ctrl+O]")
        # self.actionOpen_Directory.setText(_translate("MainWindow", "Open"))
        # self.actionOpen_Directory.setStatusTip(_translate(
        #     "MainWindow", "Open directory"))
        self.OpenDirBtn.setShortcut(_translate("MainWindow", "Ctrl+O"))

        # self.SaveDirBtn.setText(_translate("MainWindow", "Change Save Dir"))
        self.NewBoxBtn.setText(_translate("MainWindow", "Create New RectBox"))
        self.NewBoxBtn.setStatusTip(
            "Create a bounding box on this image. Shortcut [Ctrl+B]")
        self.NewBoxBtn.setShortcut(_translate("MainWindow", "Ctrl+B"))

        # basic information group
        self.basicInfoGroup.setTitle(_translate("MainWindow", "Basic Information"))
        self.basicInfoGroup.setStyleSheet('QGroupBox:title {'
                                          'border: 1px solid lightgray;'
                                          'border-radius: 5px;'
                                          'subcontrol-position: top center;'
                                          'margin-top: 5px;'
                                          'padding-left: 10px;'
                                          'padding-right: 10px; }')
        self.startFrame_label.setText(_translate("MainWindow", "Start Frame"))
        self.startFrame_label.setStatusTip(
            "Clip start frame, NOT the crash start frame. Format: 6-digit number starts with 0, e.g. 000045.")
        self.endFrame_label.setText(_translate("MainWindow", "End Frame"))
        self.endFrame_label.setStatusTip(
            "Clip end frame. Format: 6-digit number starts with 0, e.g. 000055.")
        self.crashStartFrame_label.setText(_translate("MainWindow", "Crash Start Frame"))
        self.crashStartFrame_label.setStatusTip(
            "The frame you think the car crash is evitable. Format: 6-digit number starts with 0, e.g. 000050.")

        self.ifDay_label.setText(_translate("MainWindow", "Day or Night"))
        self.ifDay_comboBox.setItemText(0, _translate("MainWindow", "Day"))
        self.ifDay_comboBox.setItemText(1, _translate("MainWindow", "Night"))

        self.weather_label.setText(_translate("MainWindow", "Weather"))
        self.weather_label.setStatusTip(
            "Rainy: If it's rainy; Snowy: if the road is covered by snow; Normal: others.")
        self.weather_comboBox.setItemText(0, _translate("MainWindow", "Normal"))
        self.weather_comboBox.setItemText(1, _translate("MainWindow", "Rainy"))
        self.weather_comboBox.setItemText(2, _translate("MainWindow", "Snowy"))

        self.ifEgo_label.setText(_translate("MainWindow", "If Ego Involved"))
        self.ifEgo_label.setStatusTip(
            "If ego car is involved in the car accident.")
        self.ifEgo_comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.ifEgo_comboBox.setItemText(1, _translate("MainWindow", "No"))

        # self.delEgoReasonBtn.setText(_translate("MainWindow", "Delete"))

        self.egoReason_label.setText(_translate("MainWindow", "Ego Car Reason"))
        self.egoReason_comboBox.setItemText(
            0, _translate("MainWindow", "none"))
        self.egoReason_comboBox.setItemText(
            1, _translate("MainWindow", "no fault"))
        self.egoReason_comboBox.setItemText(
            2, _translate("MainWindow", "hard to define"))
        self.egoReason_comboBox.setItemText(
            3, _translate("MainWindow", "unclear view"))
        self.egoReason_comboBox.setItemText(
            4, _translate("MainWindow", "speedy"))
        self.egoReason_comboBox.setItemText(
            5, _translate("MainWindow", "poor judgement"))
        self.egoReason_comboBox.setItemText(
            6, _translate("MainWindow", "traffic violation"))
        self.egoReason_comboBox.setItemText(
            7, _translate("MainWindow", "negligence"))
        self.egoReason_comboBox.setItemText(
            8, _translate("MainWindow", "change lane"))
        self.egoReason_comboBox.setItemText(
            9, _translate("MainWindow", "sudden move"))
        self.egoReason_comboBox.setItemText(
            10, _translate("MainWindow", "slippery road"))
        self.egoReason_comboBox.setItemText(
            11, _translate("MainWindow", "uneven road"))
        self.egoReason_comboBox.setItemText(
            12, _translate("MainWindow", "obstacles on the road"))


        # self.reason_note.setText("If ego car is not involved, choose 'None'; 
        # If you choose 'Hard to define' or 'No fault', 
        # do not choose other reason. Multiple choice except the above situation.")

        self.basicEditBtn.setText(_translate("MainWindow", "Edit"))
        self.basicSaveBtn.setText(_translate("MainWindow", "Save"))

        # buttons to play images
        self.prev5Btn.setText(_translate("MainWindow", "<< Prev 5"))
        self.prev5Btn.setShortcut(_translate("MainWindow", 'A'))
        self.prev5Btn.setStatusTip(
            "Check the frame which is 5 frames before current frame. Shortcut [A]")
        
        self.prevBtn.setText(_translate("MainWindow", "< Prev"))
        self.prevBtn.setShortcut(_translate("MainWindow", 'S'))
        self.prevBtn.setStatusTip(
            "Check previous frame. Shortcut [S]")

        self.nextBtn.setText(_translate("MainWindow", "Next >"))
        self.nextBtn.setShortcut(_translate("MainWindow", 'D'))
        self.nextBtn.setStatusTip(
            "Check next frame. Shortcut [D]")

        self.next5Btn.setText(_translate("MainWindow", "Next 5 >>"))
        self.next5Btn.setShortcut(_translate("MainWindow", 'F'))
        self.next5Btn.setStatusTip(
            "Check the frame which is 5 frames after current frame. Shortcut [F]")

        self.setStartBtn.setText(_translate("MainWindow", "set as Start Frame"))
        self.setStartBtn.setStatusTip(
            "Set current frame as the clip start frame.")
        self.setEndBtn.setText(_translate("MainWindow", "set as End Frame"))
        self.setEndBtn.setStatusTip(
            "Set current frame as the clip end frame.")
        self.setCrashStartBtn.setText(_translate("MainWindow", "set as Crash Start Frame"))
        self.setCrashStartBtn.setStatusTip(
            "Set current frame as the crash start frame, which means the accident is about to happed.")

        self.objInfo_groupBox.setTitle(_translate("MainWindow", "Objects Information"))
        self.objInfo_groupBox.setStyleSheet('QGroupBox:title {'
                      'border: 1px solid lightgray;'
                      'border-radius: 5px;'
                      'subcontrol-position: top center;'
                      'margin-top: 5px;'
                      'padding-left: 10px;'
                      'padding-right: 10px; }')

        self.objType_label.setText(_translate("MainWindow", "Object Type"))
        self.objTypes_comboBox.setItemText(0, _translate("MainWindow", "Car"))
        self.objTypes_comboBox.setItemText(1, _translate("MainWindow", "Truck"))
        self.objTypes_comboBox.setItemText(2, _translate("MainWindow", "Bike"))
        self.objTypes_comboBox.setItemText(3, _translate("MainWindow", "Pedestrian"))
        self.objTypes_comboBox.setItemText(4, _translate("MainWindow", "Animal"))

        self.ifObj_label.setText(_translate("MainWindow", "If Involved"))
        self.ifObj_comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.ifObj_comboBox.setItemText(1, _translate("MainWindow", "No"))

        # self.delObjReasonBtn.setText(_translate("MainWindow", "Delete"))

        self.objReason_label.setText(_translate("MainWindow", "Reason"))
        self.objReason_comboBox.setItemText(
            0, _translate("MainWindow", "none"))
        self.objReason_comboBox.setItemText(
            1, _translate("MainWindow", "no fault"))
        self.objReason_comboBox.setItemText(
            2, _translate("MainWindow", "hard to define"))
        self.objReason_comboBox.setItemText(
            3, _translate("MainWindow", "unclear view"))
        self.objReason_comboBox.setItemText(
            4, _translate("MainWindow", "speedy"))
        self.objReason_comboBox.setItemText(
            5, _translate("MainWindow", "poor judgement"))
        self.objReason_comboBox.setItemText(
            6, _translate("MainWindow", "traffic violation"))
        self.objReason_comboBox.setItemText(
            7, _translate("MainWindow", "negligence"))
        self.objReason_comboBox.setItemText(
            8, _translate("MainWindow", "change lane"))
        self.objReason_comboBox.setItemText(
            9, _translate("MainWindow", "sudden move"))
        self.objReason_comboBox.setItemText(
            10, _translate("MainWindow", "slippery road"))
        self.objReason_comboBox.setItemText(
            11, _translate("MainWindow", "uneven road"))
        self.objReason_comboBox.setItemText(
            12, _translate("MainWindow", "obstacles on the road"))

        # self.bbox_label.setText(_translate("MainWindow", "Bounding Box"))

        item = self.bbox_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Frame #"))
        item = self.bbox_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Coordinates"))

        item = self.obj_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.obj_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "If"))
        item = self.obj_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reason"))
        item = self.obj_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "B-Boxes"))

        # self.resetObjBtn.setText(_translate("MainWindow", "Reset"))
        # self.delBoxBtn.setText(_translate("MainWindow", "Delete"))
        self.addObjBtn.setText(_translate("MainWindow", "Add"))
        self.addObjBtn.setStatusTip(
            "Add the current object to object list.")

        # self.delObjBtn.setText(_translate("MainWindow", "Delete"))
        self.editObjBtn.setText(_translate("MainWindow", "Edit"))
        self.editObjBtn.setStatusTip(
            "Edit select object in the list.")
        self.saveObjBtn.setText(_translate("MainWindow", "Save and Reset"))
        self.saveObjBtn.setStatusTip(
            "Save all the objects in the list and reset all the forms including basic information.")

        style = '''
                QGroupBox {
                    border: None;
                    padding: 0px;
                    margin: 0px;
                }
                '''

        self.BBox.setStyleSheet(style)
        self.playImage_groupBox.setStyleSheet(style)
        self.set_groupBox.setStyleSheet(style)
        self.objBtns_groupBox1.setStyleSheet(style)
        self.objBtns_groupBox2.setStyleSheet(style)

        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
