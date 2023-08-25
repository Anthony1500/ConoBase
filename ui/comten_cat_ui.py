# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comten_cat.ui'
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 401))
        self.label.setPixmap(QPixmap(u"../images/background_collection_1.png"))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 391, 51))
        font = QFont()
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 361, 331))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background: #ffffff;\n"
"    \n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.label_2.setPixmap(QPixmap(u"../images/background_collection_2.png"))
        self.inputtext_create_cat_2 = QTextEdit(Dialog)
        self.inputtext_create_cat_2.setObjectName(u"inputtext_create_cat_2")
        self.inputtext_create_cat_2.setGeometry(QRect(50, 90, 301, 41))
        self.inputtext_create_cat_2.setStyleSheet(u"QTextEdit {\n"
"    font-size: 14pt;\n"
"    font-family: Helvetica;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid blue;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"                border-radius: 10px;\n"
"                background-clip: border;\n"
"                background-color: rgb(220, 220,220);\n"
"                color: rgb(0, 0, 0);\n"
"                font: 13pt Vazir;\n"
"                border:0.5px solid;\n"
"                border-color: rgb(220, 220,220);\n"
"                font-family: Helvetica;\n"
"                font-size: 14pt;\n"
"            }\n"
"\n"
"")
        self.guardar = QPushButton(Dialog)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setGeometry(QRect(210, 330, 141, 31))
        self.guardar.setFont(font)
        self.guardar.setMouseTracking(True)
        self.guardar.setStyleSheet(u"QPushButton {\n"
"    background-color: #55d940;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 16px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        self.cancelar = QPushButton(Dialog)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(50, 330, 141, 31))
        self.cancelar.setFont(font)
        self.cancelar.setMouseTracking(True)
        self.cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #d94040;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 16px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        self.inputtext_create_cat_3 = QTextEdit(Dialog)
        self.inputtext_create_cat_3.setObjectName(u"inputtext_create_cat_3")
        self.inputtext_create_cat_3.setGeometry(QRect(50, 170, 301, 151))
        self.inputtext_create_cat_3.setStyleSheet(u"QTextEdit {\n"
"    font-size: 13pt;\n"
"   \n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid blue;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"                border-radius: 10px;\n"
"                background-clip: border;\n"
"                background-color: rgb(220, 220,220);\n"
"                color: rgb(0, 0, 0);\n"
"                font: 12pt Vazir;\n"
"                border:0.5px solid;\n"
"                border-color: rgb(220, 220,220);\n"
"                font-family: Swiss;\n"
"                font-size: 12pt;\n"
"            }\n"
"\n"
"")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 50, 71, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 15px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 130, 111, 41))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 15px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 50, 81, 41))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.data_category = QLabel(Dialog)
        self.data_category.setObjectName(u"data_category")
        self.data_category.setGeometry(QRect(290, 50, 81, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.data_category.setFont(font1)
        self.data_category.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 11px; /* Tama\u00f1o del texto */\n"
"    font-weight: bold;\n"
"   \n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Ingresa contenido a la nueva categor\u00eda :", None))
        self.label_2.setText("")
        self.guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Tema:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Categor\u00eda:", None))
        self.data_category.setText("")
    # retranslateUi

