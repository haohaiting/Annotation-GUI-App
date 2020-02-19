# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.leftPart_groupBox = QtWidgets.QGroupBox(self.Left)
        self.leftPart_groupBox.setTitle("")
        self.leftPart_groupBox.setObjectName("leftPart_groupBox")

        # FUNCTIONS
        # open dir, change save dir, create new boxes
        self.Funcitons = QtWidgets.QGroupBox(self.leftPart_groupBox)
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

        # add group to left part
        self.leftPart_verticalLayout.addWidget(self.Funcitons)

        # BASIC INFO
        # open dir, change save dir, create new boxes
        self.basicInfoGroup = QtWidgets.QGroupBox(self.leftPart_groupBox)
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

        # end frame
        self.endFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.endFrame_label .setObjectName("endFrame_label ")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.endFrame_label)
        self.endFrame_lineEdit = QtWidgets.QLineEdit(self.basicInfoGroup)
        self.endFrame_lineEdit.setObjectName("endFrame_lineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.endFrame_lineEdit)

        # horizontal line
        self.line = QtWidgets.QFrame(self.basicInfoGroup)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line)

        # crash start frame
        self.crashStartFrame_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.crashStartFrame_label.setObjectName("crashStartFrame_label")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.crashStartFrame_label)
        self.crashStartFrame_lineEdit = QtWidgets.QLineEdit(
            self.basicInfoGroup)
        self.crashStartFrame_lineEdit.setObjectName("crashStartFrame_lineEdit")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.crashStartFrame_lineEdit)

        # horizontal line
        self.line_2 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.line_2)

        # day or night
        self.ifDay_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifDay_label.setObjectName("ifDay_label")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.ifDay_label)
        self.ifDay_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifDay_comboBox.setMinimumWidth(120)
        self.ifDay_comboBox.setObjectName("ifDay_comboBox")
        self.ifDay_comboBox.addItem("")
        self.ifDay_comboBox.addItem("")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.ifDay_comboBox)

        # weather
        self.weather_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.weather_label.setObjectName("weather_label")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.weather_label)
        self.weather_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.weather_comboBox.setMinimumWidth(120)
        self.weather_comboBox.setObjectName("weather_comboBox")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.weather_comboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.weather_comboBox)

        # horizontal line
        self.line_3 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.line_3)

        # if ego involved
        self.ifEgo_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.ifEgo_label.setObjectName("ifEgo_label")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.ifEgo_label)
        self.ifEgo_comboBox = QtWidgets.QComboBox(self.basicInfoGroup)
        self.ifEgo_comboBox.setMinimumWidth(120)
        self.ifEgo_comboBox.setObjectName("ifEgo_comboBox")
        self.ifEgo_comboBox.addItem("")
        self.ifEgo_comboBox.addItem("")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.ifEgo_comboBox)

        # ego reason
        self.egoReason_label = QtWidgets.QLabel(self.basicInfoGroup)
        self.egoReason_label.setObjectName("egoReason_label")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.egoReason_label)

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
            9, QtWidgets.QFormLayout.FieldRole, self.egoReason_comboBox)
        
        self.EgoReasonList = QtWidgets.QListView(self.basicInfoGroup)
        self.EgoReasonList.setObjectName("EgoReasonList")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.EgoReasonList)
        
        # horizontal line
        self.line_4 = QtWidgets.QFrame(self.basicInfoGroup)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.line_4)

        # basic information related buttons
        # reset button
        self.basicResetBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicResetBtn.setObjectName("basicResetBtn")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.LabelRole, self.basicResetBtn)
        # save button
        self.basicSaveBtn = QtWidgets.QPushButton(self.basicInfoGroup)
        self.basicSaveBtn.setEnabled(True)
        self.basicSaveBtn.setObjectName("basicSaveBtn")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.basicSaveBtn)

        # handle layout issue
        self.leftPart_verticalLayout.addWidget(self.basicInfoGroup)
        self.leftPart_verticalLayout.addWidget(self.leftPart_groupBox)
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

        # ============================================
        # Right Part
        # ============================================

        self.Right = QtWidgets.QGroupBox(self.centralwidget)
        self.Right.setTitle("")
        self.Right.setObjectName("Right")
        self.Right.setMaximumWidth(300)

        self.rightPart_verticalLayout = QtWidgets.QVBoxLayout(self.Right)
        self.rightPart_verticalLayout.setObjectName("rightPart_verticalLayout")

        self.Funcitons_3 = QtWidgets.QGroupBox(self.Right)
        self.Funcitons_3.setObjectName("Funcitons_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Funcitons_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.Funcitons_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Funcitons_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_9 = QtWidgets.QLabel(self.Funcitons_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox_9 = QtWidgets.QComboBox(self.Funcitons_3)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_9)
        self.label_13 = QtWidgets.QLabel(self.Funcitons_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.comboBox_7 = QtWidgets.QComboBox(self.Funcitons_3)
        self.comboBox_7.setEnabled(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_7)
        self.label_14 = QtWidgets.QLabel(self.Funcitons_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.pushButton_7 = QtWidgets.QPushButton(self.Funcitons_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.Funcitons_3)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMouseTracking(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        self.comboBox_8 = QtWidgets.QComboBox(self.Funcitons_3)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_8)
        self.label_15 = QtWidgets.QLabel(self.Funcitons_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.BBoxList = QtWidgets.QListView(self.Funcitons_3)
        self.BBoxList.setObjectName("BBoxList")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.BBoxList)
        self.ObjectReasonList = QtWidgets.QListView(self.Funcitons_3)
        self.ObjectReasonList.setObjectName("ObjectReasonList")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ObjectReasonList)
        self.rightPart_verticalLayout.addWidget(self.Funcitons_3)
        self.ObjectList = QtWidgets.QListView(self.Right)
        self.ObjectList.setObjectName("ObjectList")
        self.rightPart_verticalLayout.addWidget(self.ObjectList)

        # prev, next buttons
        self.groupBox_7 = QtWidgets.QGroupBox(self.Right)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.rightPart_verticalLayout.addWidget(self.groupBox_7)
        self.horizontalLayout.addWidget(self.Right)

        # file list
        self.fileListWidget = QtWidgets.QListWidget()
        self.rightPart_verticalLayout.addWidget(self.fileListWidget)



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # remove docker widget
        # self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        # self.dockWidget.setObjectName("dockWidget")
        # self.dockWidgetContents = QtWidgets.QWidget()
        # self.dockWidgetContents.setObjectName("dockWidgetContents")
        # self.dockWidget.setWidget(self.dockWidgetContents)
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

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
        # self.actionOpen_Directory.setText(_translate("MainWindow", "Open"))
        # self.actionOpen_Directory.setStatusTip(_translate(
        #     "MainWindow", "Open directory"))
        self.actionOpen_Directory.setShortcut(_translate("MainWindow", "Ctrl+O"))

        # self.SaveDirBtn.setText(_translate("MainWindow", "Change Save Dir"))
        self.NewBoxBtn.setText(_translate("MainWindow", "Create New RectBox"))

        # basic information group
        self.basicInfoGroup.setTitle(_translate("MainWindow", "Basic Information"))
        self.startFrame_label.setText(_translate("MainWindow", "Start Frame"))
        self.endFrame_label.setText(_translate("MainWindow", "End Frame"))
        self.crashStartFrame_label.setText(_translate("MainWindow", "Crash Start Frame"))

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

        self.Funcitons_3.setTitle(_translate("MainWindow", "Objects Information"))
        self.label_8.setText(_translate("MainWindow", "Object Num"))
        self.label_9.setText(_translate("MainWindow", "Object Type"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Car"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Truck"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Bike"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Person"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "Animal"))
        self.label_13.setText(_translate("MainWindow", "If Involved"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "No"))
        self.label_14.setText(_translate("MainWindow", "Reason"))
        self.pushButton_7.setText(_translate("MainWindow", "Reset"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "No Fault"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Hard to define"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "None"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Speedy"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "Poor Judgement"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "Slippery Road"))
        self.label_15.setText(_translate("MainWindow", "Bounding Box"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_13.setText(_translate("MainWindow", "Edit"))
        self.pushButton_14.setText(_translate("MainWindow", "Save"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))


# def clicked(self, text):
#         self.label.setText(text)
#         self.label.adjustSize()
