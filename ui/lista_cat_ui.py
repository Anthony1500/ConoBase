# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_cat.ui'
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
        self.label.setPixmap(QPixmap(u"../images/background_2.png"))
        self.lista_cat = QListView(Dialog)
        self.lista_cat.setObjectName(u"lista_cat")
        self.lista_cat.setGeometry(QRect(20, 60, 361, 291))
        self.textname_1 = QLabel(Dialog)
        self.textname_1.setObjectName(u"textname_1")
        self.textname_1.setGeometry(QRect(10, 0, 191, 51))
        self.textname_1.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(130, 360, 141, 31))
        font = QFont()
        self.back.setFont(font)
        self.back.setMouseTracking(True)
        self.back.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.textname_1.setText(QCoreApplication.translate("Dialog", u"Lista categor\u00edas: ", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

