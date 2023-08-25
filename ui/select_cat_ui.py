# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_cat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 160, 241, 51))
        font = QFont()
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #b127be;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 16px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A7EDE7;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        self.myButton = QPushButton(Dialog)
        self.myButton.setObjectName(u"myButton")
        self.myButton.setGeometry(QRect(90, 100, 241, 51))
        self.myButton.setFont(font)
        self.myButton.setMouseTracking(True)
        self.myButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #b127be;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 16px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A7EDE7;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 100, 71, 51))
        font1 = QFont()
        font1.setFamily(u"Arial")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"}")
        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 411, 401))
        self.label.setPixmap(QPixmap(u"../images/background.png"))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 241, 51))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 220, 241, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #b127be;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 16px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A7EDE7;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 160, 71, 51))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"}")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 220, 71, 51))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"}")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 100, 91, 51))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"color: white\n"
"}")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 160, 91, 51))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"color: white\n"
"}")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 220, 91, 51))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"color: white\n"
"}")
        self.label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.pushButton_2.raise_()
        self.myButton.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.pushButton_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Buscar categor\u00eda", None))
        self.myButton.setText(QCoreApplication.translate("Dialog", u"Crear nueva categor\u00eda", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Selecciona una opci\u00f3n :", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"En desarrollo", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"------------------------------------------", None))
    # retranslateUi

