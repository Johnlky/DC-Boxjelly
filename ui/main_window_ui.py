# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 710)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(247, 247, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_menu = QtWidgets.QFrame(self.main_frame)
        self.top_menu.setMaximumSize(QtCore.QSize(16777215, 70))
        self.top_menu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(255, 90, 255, 255), stop:0.477833 rgba(255, 255, 255, 255), stop:0.970443 rgba(57, 224, 55, 255));")
        self.top_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu.setObjectName("top_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.top_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top_menu_buttons = QtWidgets.QFrame(self.top_menu)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 90, 255))
        gradient.setColorAt(0.477833, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.970443, QtGui.QColor(57, 224, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.top_menu_buttons.setPalette(palette)
        self.top_menu_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menu_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_buttons.setObjectName("top_menu_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_menu_buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homeButton = QtWidgets.QPushButton(self.top_menu_buttons)
        self.homeButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.homeButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 255, 199);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)
        self.constantButton = QtWidgets.QPushButton(self.top_menu_buttons)
        self.constantButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 255, 199);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.constantButton.setObjectName("constantButton")
        self.horizontalLayout.addWidget(self.constantButton)
        self.verticalLayout_3.addWidget(self.top_menu_buttons)
        self.verticalLayout_2.addWidget(self.top_menu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.main_body = QtWidgets.QFrame(self.main_frame)
        self.main_body.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.home_page)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.home_page)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.home_page)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_13.addWidget(self.lineEdit_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.addButton = QtWidgets.QPushButton(self.home_page)
        self.addButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_14.addWidget(self.addButton)
        self.viewButton = QtWidgets.QPushButton(self.home_page)
        self.viewButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_14.addWidget(self.viewButton)
        self.deleteButton = QtWidgets.QPushButton(self.home_page)
        self.deleteButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_14.addWidget(self.deleteButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.homeTable = QtWidgets.QTableWidget(self.home_page)
        self.homeTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.homeTable.setFont(font)
        self.homeTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.homeTable.setObjectName("homeTable")
        self.homeTable.setColumnCount(3)
        self.homeTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.homeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.homeTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.homeTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.homeTable)
        self.stackedWidget.addWidget(self.home_page)
        self.viewclientinfo_page = QtWidgets.QWidget()
        self.viewclientinfo_page.setObjectName("viewclientinfo_page")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.viewclientinfo_page)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.viewclientinfo_page)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_18.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.horizontalFrame_6 = QtWidgets.QFrame(self.viewclientinfo_page)
        self.horizontalFrame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalFrame_6.setObjectName("horizontalFrame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.label_13 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.label_11 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.label_9 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_17.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_17.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalFrame_6)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_17.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalFrame_6)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_17.addWidget(self.lineEdit_9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_17)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalFrame_6)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_18.addWidget(self.horizontalFrame_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.compareButton = QtWidgets.QPushButton(self.viewclientinfo_page)
        self.compareButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.compareButton.setObjectName("compareButton")
        self.horizontalLayout_15.addWidget(self.compareButton)
        self.addnewequipmentButton = QtWidgets.QPushButton(self.viewclientinfo_page)
        self.addnewequipmentButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.addnewequipmentButton.setObjectName("addnewequipmentButton")
        self.horizontalLayout_15.addWidget(self.addnewequipmentButton)
        self.deleteequipmentButton = QtWidgets.QPushButton(self.viewclientinfo_page)
        self.deleteequipmentButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.deleteequipmentButton.setObjectName("deleteequipmentButton")
        self.horizontalLayout_15.addWidget(self.deleteequipmentButton)
        self.returnButton = QtWidgets.QPushButton(self.viewclientinfo_page)
        self.returnButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout_15.addWidget(self.returnButton)
        self.verticalLayout_18.addLayout(self.horizontalLayout_15)
        self.clientTable = QtWidgets.QTableWidget(self.viewclientinfo_page)
        self.clientTable.setObjectName("clientTable")
        self.clientTable.setColumnCount(3)
        self.clientTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.clientTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.clientTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.clientTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_18.addWidget(self.clientTable)
        self.stackedWidget.addWidget(self.viewclientinfo_page)
        self.compare_page = QtWidgets.QWidget()
        self.compare_page.setObjectName("compare_page")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.compare_page)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_47 = QtWidgets.QLabel(self.compare_page)
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_34.addWidget(self.label_47, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem1)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_39 = QtWidgets.QLabel(self.compare_page)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_32.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.compare_page)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_32.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.compare_page)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_32.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.compare_page)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_32.addWidget(self.label_42)
        self.horizontalLayout_33.addLayout(self.verticalLayout_32)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_43 = QtWidgets.QLabel(self.compare_page)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_33.addWidget(self.label_43, 0, QtCore.Qt.AlignHCenter)
        self.label_45 = QtWidgets.QLabel(self.compare_page)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_33.addWidget(self.label_45, 0, QtCore.Qt.AlignHCenter)
        self.label_46 = QtWidgets.QLabel(self.compare_page)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_33.addWidget(self.label_46, 0, QtCore.Qt.AlignHCenter)
        self.label_44 = QtWidgets.QLabel(self.compare_page)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_33.addWidget(self.label_44, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_33.addLayout(self.verticalLayout_33)
        spacerItem2 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem2)
        self.verticalLayout_34.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.importButton = QtWidgets.QPushButton(self.compare_page)
        self.importButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_34.addWidget(self.importButton)
        self.analyseButton = QtWidgets.QPushButton(self.compare_page)
        self.analyseButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.analyseButton.setObjectName("analyseButton")
        self.horizontalLayout_34.addWidget(self.analyseButton)
        self.viewequipmentButton_3 = QtWidgets.QPushButton(self.compare_page)
        self.viewequipmentButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.viewequipmentButton_3.setObjectName("viewequipmentButton_3")
        self.horizontalLayout_34.addWidget(self.viewequipmentButton_3)
        self.returnButton_2 = QtWidgets.QPushButton(self.compare_page)
        self.returnButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 16px;\n"
"padding: 6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(83, 82, 82);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"}\n"
"")
        self.returnButton_2.setObjectName("returnButton_2")
        self.horizontalLayout_34.addWidget(self.returnButton_2)
        self.verticalLayout_34.addLayout(self.horizontalLayout_34)
        self.compareTable = QtWidgets.QTableWidget(self.compare_page)
        self.compareTable.setObjectName("compareTable")
        self.compareTable.setColumnCount(4)
        self.compareTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.compareTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.compareTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.compareTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.compareTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_34.addWidget(self.compareTable)
        self.stackedWidget.addWidget(self.compare_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.main_body)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.constantButton.clicked.connect(MainWindow.openConstantsWindow)
        self.addButton.clicked.connect(MainWindow.openAddClientWindow)
        self.addnewequipmentButton.clicked.connect(MainWindow.openAddEquipmentWindow)
        self.importButton.clicked.connect(MainWindow.openImportWindow)
        self.analyseButton.clicked.connect(MainWindow.openAnalysisWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.constantButton.setText(_translate("MainWindow", "CONSTANTS"))
        self.label_4.setText(_translate("MainWindow", "HOME"))
        self.label_12.setText(_translate("MainWindow", "Search: "))
        self.addButton.setText(_translate("MainWindow", "Add New Client"))
        self.viewButton.setText(_translate("MainWindow", "View/Edit Client Information"))
        self.deleteButton.setText(_translate("MainWindow", "Delete Client"))
        item = self.homeTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SELECT"))
        item = self.homeTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CAL NUMBER"))
        item = self.homeTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CLIENT NAME"))
        self.label_16.setText(_translate("MainWindow", "CLIENT INFORMATION"))
        self.label_10.setText(_translate("MainWindow", "CAL Number"))
        self.label_13.setText(_translate("MainWindow", "Client Name"))
        self.label_11.setText(_translate("MainWindow", "Address 1"))
        self.label_9.setText(_translate("MainWindow", "Address 2"))
        self.label_14.setText(_translate("MainWindow", "CAL00001"))
        self.label_15.setText(_translate("MainWindow", "Winnie"))
        self.pushButton_5.setText(_translate("MainWindow", "Update"))
        self.compareButton.setText(_translate("MainWindow", "Compare/Analysis"))
        self.addnewequipmentButton.setText(_translate("MainWindow", "Add New Equipment"))
        self.deleteequipmentButton.setText(_translate("MainWindow", "Delete Equipment"))
        self.returnButton.setText(_translate("MainWindow", "Return"))
        item = self.clientTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SELECT"))
        item = self.clientTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SERIAL NUMBER"))
        item = self.clientTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MAKE/MODEL"))
        self.label_47.setText(_translate("MainWindow", "Compare/Analysis"))
        self.label_39.setText(_translate("MainWindow", "CAL Number"))
        self.label_40.setText(_translate("MainWindow", "Client Name"))
        self.label_41.setText(_translate("MainWindow", "Serial Number"))
        self.label_42.setText(_translate("MainWindow", "Make/Model Number"))
        self.label_43.setText(_translate("MainWindow", "CAL00001"))
        self.label_45.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "TextLabel"))
        self.label_44.setText(_translate("MainWindow", "Winnie"))
        self.importButton.setText(_translate("MainWindow", "Import Raw Files"))
        self.analyseButton.setText(_translate("MainWindow", "Analyse Run"))
        self.viewequipmentButton_3.setText(_translate("MainWindow", "Delete Run"))
        self.returnButton_2.setText(_translate("MainWindow", "Return"))
        item = self.compareTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RUN NUMBER"))
        item = self.compareTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CLIENT RAW FILE"))
        item = self.compareTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LAB RAW FILE"))
        item = self.compareTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UPLOADED DATETIME"))