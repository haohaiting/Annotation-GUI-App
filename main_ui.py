# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


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
        self.formLayout = QtWidgets.QFormLayout(self.basicInfoGroup)
        self.formLayout.setObjectName("formLayout")

        # start frame
        self.startFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.startFrame_label.setObjectName("startFrame_label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.startFrame_label)
        self.startFrame_lineEdit = QtWidgets.QLineEdit(self.basicInfoGroup)
        self.startFrame_lineEdit.setObjectName("startFrame_lineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.startFrame_lineEdit)

        # crash start frame
        self.crashStartFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.crashStartFrame_label.setObjectName("crashStartFrame_label")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.crashStartFrame_label)
        self.crashStartFrame_lineEdit = QtWidgets.QLineEdit(
            self.basicInfoGroup)
        self.crashStartFrame_lineEdit.setObjectName("crashStartFrame_lineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.crashStartFrame_lineEdit)

        # end frame
        self.endFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.endFrame_label .setObjectName("endFrame_label ")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.endFrame_label)
        self.endFrame_lineEdit = QtWidgets.QLineEdit(self.basicInfoGroup)
        self.endFrame_lineEdit.setObjectName("endFrame_lineEdit")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.endFrame_lineEdit)

        # horizontal line
        self.line_2 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_2)

        # day or night
        self.ifDay_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifDay_label.setObjectName("ifDay_label")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.ifDay_label)
        self.ifDay_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifDay_comboBox.setMinimumWidth(120)
        self.ifDay_comboBox.setObjectName("ifDay_comboBox")
        self.ifDay_comboBox.addItem("")
        self.ifDay_comboBox.addItem("")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.ifDay_comboBox)

        # weather
        self.weather_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.weather_label.setObjectName("weather_label")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.weather_label)
        self.weather_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.weather_comboBox.setMinimumWidth(120)
        self.weather_comboBox.setObjectName("weather_comboBox")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.weather_comboBox)

        # horizontal line
        self.line_3 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.line_3)

        # if ego involved
        self.ifEgo_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifEgo_label.setObjectName("ifEgo_label")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.ifEgo_label)
        self.ifEgo_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifEgo_comboBox.setMinimumWidth(120)
        self.ifEgo_comboBox.setObjectName("ifEgo_comboBox")
        self.ifEgo_comboBox.addItem("")
        self.ifEgo_comboBox.addItem("")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.ifEgo_comboBox)

        # ego reason
        self.egoReason_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.egoReason_label.setObjectName("egoReason_label")
        self.formLayout.setWidget(
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
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.egoReason_comboBox)

        self.delEgoReasonBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.delEgoReasonBtn.setObjectName("delEgoReasonBtn")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.delEgoReasonBtn)
        
        self.EgoReasonList = QtWidgets.QListWidget(self.basicInfoGroup)
        self.EgoReasonList.setObjectName("EgoReasonList")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.EgoReasonList)
        
        # basic information related buttons
        # reset button
        self.basicResetBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicResetBtn.setObjectName("basicResetBtn")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.basicResetBtn)
        # save button
        self.basicSaveBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicSaveBtn.setEnabled(True)
        self.basicSaveBtn.setObjectName("basicSaveBtn")
        self.formLayout.setWidget(
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
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 868, 932))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # try to load image using QLabel
        # maybe need canvas here
        self.imageLabel = QtWidgets.QLabel()
        self.scrollArea.setWidget(self.imageLabel)
        self.middle_verticalLayout.addWidget(self.scrollArea)
        

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

        # 
        self.objInfo_groupBox = QtWidgets.QGroupBox(self.Right)
        self.objInfo_groupBox.setObjectName("objInfo_groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.objInfo_groupBox)
        self.formLayout_2.setObjectName("formLayout_2")

        self.objType_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.objType_label.setObjectName("objType_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.objType_label)
        self.objTypes_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.objTypes_comboBox.setObjectName("objTypes_comboBox")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.objTypes_comboBox.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.objTypes_comboBox)

        self.ifObj_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.ifObj_label.setObjectName("ifObj_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ifObj_label)

        self.ifObj_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.ifObj_comboBox.setObjectName("ifObj_comboBox")
        self.ifObj_comboBox.addItem("")
        self.ifObj_comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ifObj_comboBox)

        self.objReason_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.objReason_label.setObjectName("objReason_label")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.objReason_label)

        self.objReason_comboBox = QtWidgets.QComboBox(self.objInfo_groupBox)
        self.objReason_comboBox.setObjectName("objReason_comboBox")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.objReason_comboBox.addItem("")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.objReason_comboBox)

        self.delObjReasonBtn = QtWidgets.QPushButton(self.objInfo_groupBox)
        self.delObjReasonBtn.setObjectName("delObjReasonBtn")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.delObjReasonBtn)

        self.objReasonList = QtWidgets.QListWidget(self.objInfo_groupBox)
        self.objReasonList.setObjectName("objReasonList")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.objReasonList)
        self.rightPart_verticalLayout.addWidget(self.objInfo_groupBox)
        
        self.bbox_label = QtWidgets.QLabel(self.objInfo_groupBox)
        self.bbox_label.setObjectName("bbox_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.bbox_label)

        self.BBoxList = QtWidgets.QListWidget(self.objInfo_groupBox)
        self.BBoxList.setObjectName("BBoxList")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.BBoxList)

        self.resetObjBtn = QtWidgets.QPushButton(self.objInfo_groupBox)
        self.resetObjBtn.setObjectName("resetObjBtn")
        self.formLayout_2.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.resetObjBtn)

        self.addObjBtn = QtWidgets.QPushButton(self.objInfo_groupBox)
        self.addObjBtn.setEnabled(True)
        self.addObjBtn.setMouseTracking(True)
        self.addObjBtn.setObjectName("addObjBtn")
        self.formLayout_2.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.addObjBtn)

        self.ObjectList = QtWidgets.QListWidget(self.Right)
        self.ObjectList.setObjectName("ObjectList")
        self.rightPart_verticalLayout.addWidget(self.ObjectList)

        # object del, edit, save buttons
        self.objBtns_groupBox = QtWidgets.QGroupBox(self.Right)
        self.objBtns_groupBox.setTitle("")
        self.objBtns_groupBox.setObjectName("objBtns_groupBox")

        self.objBtns_horizontalLayout = QtWidgets.QHBoxLayout(self.objBtns_groupBox)
        self.objBtns_horizontalLayout.setObjectName("objBtns_horizontalLayout")

        self.delObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox)
        self.delObjBtn.setObjectName("delObjBtn")
        self.objBtns_horizontalLayout.addWidget(self.delObjBtn)

        self.editObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox)
        self.editObjBtn.setObjectName("editObjBtn")
        self.objBtns_horizontalLayout.addWidget(self.editObjBtn)

        self.saveObjBtn = QtWidgets.QPushButton(self.objBtns_groupBox)
        self.saveObjBtn.setObjectName("saveObjBtn")
        self.objBtns_horizontalLayout.addWidget(self.saveObjBtn)

        self.rightPart_verticalLayout.addWidget(self.objBtns_groupBox)
        self.horizontalLayout.addWidget(self.Right)

        # status bar
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.OpenDirBtn.setStatusTip("Open a frame directory to load all the frames in it")
        # self.actionOpen_Directory.setText(_translate("MainWindow", "Open"))
        # self.actionOpen_Directory.setStatusTip(_translate(
        #     "MainWindow", "Open directory"))
        self.actionOpen_Directory.setShortcut(_translate("MainWindow", "Ctrl+O"))

        # self.SaveDirBtn.setText(_translate("MainWindow", "Change Save Dir"))
        self.NewBoxBtn.setText(_translate("MainWindow", "Create New RectBox"))
        self.NewBoxBtn.setStatusTip(
            "Create a bounding box on this image")

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
        self.weather_comboBox.setItemText(0, _translate("MainWindow", "Normal"))
        self.weather_comboBox.setItemText(1, _translate("MainWindow", "Rainy"))
        self.weather_comboBox.setItemText(2, _translate("MainWindow", "Snowy"))

        self.ifEgo_label.setText(_translate("MainWindow", "If Ego Involved"))
        self.ifEgo_comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.ifEgo_comboBox.setItemText(1, _translate("MainWindow", "No"))

        self.delEgoReasonBtn.setText(_translate("MainWindow", "Delete"))

        self.egoReason_label.setText(_translate("MainWindow", "Ego Car Reason"))
        self.egoReason_comboBox.setItemText(0, _translate("MainWindow", "No Fault"))
        self.egoReason_comboBox.setItemText(1, _translate("MainWindow", "Hard to define"))
        self.egoReason_comboBox.setItemText(2, _translate("MainWindow", "None"))
        self.egoReason_comboBox.setItemText(3, _translate("MainWindow", "Speedy"))
        self.egoReason_comboBox.setItemText(4, _translate("MainWindow", "Poor Judgement"))
        self.egoReason_comboBox.setItemText(5, _translate("MainWindow", "Slippery Road"))

        self.basicResetBtn.setText(_translate("MainWindow", "Reset"))
        self.basicSaveBtn.setText(_translate("MainWindow", "Save"))

        # buttons to play images
        self.prev5Btn.setText(_translate("MainWindow", "<< Prev 5"))
        self.prevBtn.setText(_translate("MainWindow", "< Prev"))
        self.nextBtn.setText(_translate("MainWindow", "Next >"))
        self.next5Btn.setText(_translate("MainWindow", "Next 5 >>"))

        self.setStartBtn.setText(_translate("MainWindow", "set as Start Frame"))
        self.setEndBtn.setText(_translate("MainWindow", "set as End Frame"))
        self.setCrashStartBtn.setText(_translate("MainWindow", "set as Crash Start Frame"))

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
        self.objTypes_comboBox.setItemText(3, _translate("MainWindow", "Person"))
        self.objTypes_comboBox.setItemText(4, _translate("MainWindow", "Animal"))

        self.ifObj_label.setText(_translate("MainWindow", "If Involved"))
        self.ifObj_comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.ifObj_comboBox.setItemText(1, _translate("MainWindow", "No"))

        self.delObjReasonBtn.setText(_translate("MainWindow", "Delete"))
        self.objReason_label.setText(_translate("MainWindow", "Reason"))
        self.objReason_comboBox.setItemText(0, _translate("MainWindow", "No Fault"))
        self.objReason_comboBox.setItemText(1, _translate("MainWindow", "Hard to define"))
        self.objReason_comboBox.setItemText(2, _translate("MainWindow", "None"))
        self.objReason_comboBox.setItemText(3, _translate("MainWindow", "Speedy"))
        self.objReason_comboBox.setItemText(4, _translate("MainWindow", "Poor Judgement"))
        self.objReason_comboBox.setItemText(5, _translate("MainWindow", "Slippery Road"))

        self.bbox_label.setText(_translate("MainWindow", "Bounding Box"))

        self.resetObjBtn.setText(_translate("MainWindow", "Reset"))
        self.addObjBtn.setText(_translate("MainWindow", "Add"))

        self.delObjBtn.setText(_translate("MainWindow", "Delete"))
        self.editObjBtn.setText(_translate("MainWindow", "Edit"))
        self.saveObjBtn.setText(_translate("MainWindow", "Save"))

        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
