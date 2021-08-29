# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\import_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_import_page(object):
    def setupUi(self, import_page):
        import_page.setObjectName("import_page")
        import_page.resize(519, 273)
        self.centralwidget = QtWidgets.QWidget(import_page)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.client_file_button = QtWidgets.QPushButton(self.widget)
        self.client_file_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 20px;\n"
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
        self.client_file_button.setObjectName("client_file_button")
        self.verticalLayout_2.addWidget(self.client_file_button)
        self.lab_file_button = QtWidgets.QPushButton(self.widget)
        self.lab_file_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 20px;\n"
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
        self.lab_file_button.setObjectName("lab_file_button")
        self.verticalLayout_2.addWidget(self.lab_file_button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.client_file_path_line = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.client_file_path_line.sizePolicy().hasHeightForWidth())
        self.client_file_path_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.client_file_path_line.setFont(font)
        self.client_file_path_line.setObjectName("client_file_path_line")
        self.verticalLayout.addWidget(self.client_file_path_line)
        self.lab_file_path_line = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_file_path_line.sizePolicy().hasHeightForWidth())
        self.lab_file_path_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.lab_file_path_line.setFont(font)
        self.lab_file_path_line.setObjectName("lab_file_path_line")
        self.verticalLayout.addWidget(self.lab_file_path_line)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.submit_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(211, 213, 213);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font:bold 20px;\n"
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
        self.submit_button.setObjectName("submit_button")
        self.verticalLayout_3.addWidget(self.submit_button, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        import_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(import_page)
        QtCore.QMetaObject.connectSlotsByName(import_page)

    def retranslateUi(self, import_page):
        _translate = QtCore.QCoreApplication.translate
        import_page.setWindowTitle(_translate("import_page", "Import files"))
        self.label_3.setText(_translate("import_page", "Import Files"))
        self.client_file_button.setText(_translate("import_page", "Client File"))
        self.lab_file_button.setText(_translate("import_page", "Lab File"))
        self.submit_button.setText(_translate("import_page", "Submit"))