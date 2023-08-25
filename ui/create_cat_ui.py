# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_cat.ui'
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
        Dialog.resize(399, 400)
        self.textname_1 = QLabel(Dialog)
        self.textname_1.setObjectName(u"textname_1")
        self.textname_1.setGeometry(QRect(0, 0, 191, 51))
        self.textname_1.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.inputtext_create_cat = QTextEdit(Dialog)
        self.inputtext_create_cat.setObjectName(u"inputtext_create_cat")
        self.inputtext_create_cat.setGeometry(QRect(30, 160, 321, 41))
        self.inputtext_create_cat.setStyleSheet(u"QTextEdit:hover {\n"
"    border: 2px solid blue;\n"
"}\n"
"QTextEdit {\n"
"    font-size: 14pt;\n"
"    font-family: Helvetica;\n"
"\n"
"}\n"
"QTextEdit {\n"
"      \n"
"}\n"
"")
        self.guardar = QPushButton(Dialog)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setGeometry(QRect(210, 210, 141, 31))
        font = QFont()
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
        self.background = QLabel(Dialog)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 401, 401))
        self.background.setPixmap(QPixmap(u"../images/background.png"))
        self.cancelar = QPushButton(Dialog)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(50, 210, 141, 31))
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
        self.textname_2 = QLabel(Dialog)
        self.textname_2.setObjectName(u"textname_2")
        self.textname_2.setGeometry(QRect(0, 30, 171, 61))
        self.textname_2.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.borrar = QPushButton(Dialog)
        self.borrar.setObjectName(u"borrar")
        self.borrar.setGeometry(QRect(350, 160, 41, 41))
        self.borrar.setStyleSheet(u"QPushButton {\n"
"   \n"
"    font-size: 14pt; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}")
        icon = QIcon()
        icon.addFile(u"../images/borrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.borrar.setIcon(icon)
        self.borrar.setIconSize(QSize(25, 25))
        self.background.raise_()
        self.cancelar.raise_()
        self.textname_2.raise_()
        self.textname_1.raise_()
        self.inputtext_create_cat.raise_()
        self.guardar.raise_()
        self.borrar.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textname_1.setText(QCoreApplication.translate("Dialog", u"Ingresa el nombre", None))
        self.guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.background.setText("")
        self.cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.textname_2.setText(QCoreApplication.translate("Dialog", u"de la categor\u00eda :", None))
        self.borrar.setText("")
    # retranslateUi

