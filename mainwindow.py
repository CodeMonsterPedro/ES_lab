# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Wed Jan 15 21:53:53 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbw_test = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_test.setGeometry(QtCore.QRect(10, 30, 471, 611))
        self.tbw_test.setObjectName("tbw_test")
        self.tbw_test.setColumnCount(0)
        self.tbw_test.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 6, 121, 20))
        self.label_4.setObjectName("label_4")
        self.tbw_structure = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_structure.setGeometry(QtCore.QRect(490, 30, 301, 611))
        self.tbw_structure.setObjectName("tbw_structure")
        self.tbw_structure.setColumnCount(0)
        self.tbw_structure.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 10, 111, 16))
        self.label_5.setObjectName("label_5")
        self.btn_nodereset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nodereset.setGeometry(QtCore.QRect(940, 30, 80, 24))
        self.btn_nodereset.setObjectName("btn_nodereset")
        self.ln_nodereset = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_nodereset.setGeometry(QtCore.QRect(800, 30, 131, 24))
        self.ln_nodereset.setObjectName("ln_nodereset")
        self.ln_answerreset = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_answerreset.setGeometry(QtCore.QRect(800, 70, 131, 24))
        self.ln_answerreset.setObjectName("ln_answerreset")
        self.btn_answerreset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_answerreset.setGeometry(QtCore.QRect(940, 70, 80, 24))
        self.btn_answerreset.setObjectName("btn_answerreset")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(800, 620, 80, 24))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(800, 590, 80, 24))
        self.btn_save.setObjectName("btn_save")
        self.btn_upload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_upload.setGeometry(QtCore.QRect(800, 560, 80, 24))
        self.btn_upload.setObjectName("btn_upload")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(800, 130, 80, 24))
        self.btn_run.setObjectName("btn_run")
        self.btn_makefile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_makefile.setGeometry(QtCore.QRect(940, 130, 80, 24))
        self.btn_makefile.setObjectName("btn_makefile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Test result", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Node structure", None, -1))
        self.btn_nodereset.setText(QtWidgets.QApplication.translate("MainWindow", "Reset this", None, -1))
        self.ln_nodereset.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Node id", None, -1))
        self.ln_answerreset.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Answer id", None, -1))
        self.btn_answerreset.setText(QtWidgets.QApplication.translate("MainWindow", "Reset this", None, -1))
        self.btn_clear.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.btn_save.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.btn_upload.setText(QtWidgets.QApplication.translate("MainWindow", "Upload", None, -1))
        self.btn_run.setText(QtWidgets.QApplication.translate("MainWindow", "Run", None, -1))
        self.btn_makefile.setText(QtWidgets.QApplication.translate("MainWindow", "Make file", None, -1))

