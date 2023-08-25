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

from main import MyTextEdit


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
        self.lista_cat.setGeometry(QRect(20, 90, 361, 261))
        self.lista_cat.setLayoutDirection(Qt.LeftToRight)
        self.lista_cat.setStyleSheet(u"QListView::item {\n"
"    /* No funcionar\u00e1 sin establecer los bordes */\n"
"    border: 0px;\n"
"    margin-left: 10px; /* Ajusta este valor para el margen deseado */\n"
"}")
        self.lista_cat.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.lista_cat.setAlternatingRowColors(True)
        self.lista_cat.setTextElideMode(Qt.ElideRight)
        self.lista_cat.setModelColumn(0)
        self.lista_cat.setUniformItemSizes(False)
        self.lista_cat.setSelectionRectVisible(False)
        self.textname_1 = QLabel(Dialog)
        self.textname_1.setObjectName(u"textname_1")
        self.textname_1.setGeometry(QRect(10, 0, 191, 41))
        self.textname_1.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
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
        self.inputtext_search_cat = MyTextEdit(Dialog)
        self.inputtext_search_cat.setObjectName(u"inputtext_search_cat")
        self.inputtext_search_cat.setGeometry(QRect(70, 40, 271, 41))
        self.inputtext_search_cat.setStyleSheet(u"QTextEdit {\n"
"    font-size: 14pt;\n"
"    font-family: Helvetica;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid blue;\n"
"    border-radius: 9px;\n"
"    margin-bottom: 0px;\n"
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
        self.inputtext_search_cat.setAcceptRichText(True)
        self.buscar = QPushButton(Dialog)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setEnabled(True)
        self.buscar.setGeometry(QRect(298, 42, 41, 37))
        self.buscar.setAutoFillBackground(False)
        self.buscar.setStyleSheet(u"QPushButton {\n"
"   \n"
"    font-size: 14pt; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton {\n"
"                border-radius: 10px;\n"
"                background-clip: border;\n"
"                background-color: rgb(220, 220,220);\n"
"                color: rgb(0, 0, 0);\n"
"                font: 13pt Vazir;\n"
"                border:0.5px solid;\n"
"                border-color: rgb(220, 220,220);\n"
"                font-family: Helvetica;\n"
"                font-size: 14pt;\n"
"            }")
        icon = QIcon()
        icon.addFile(u"../images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar.setIcon(icon)
        self.buscar.setIconSize(QSize(25, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.textname_1.setText(QCoreApplication.translate("Dialog", u"Lista categor\u00edas: ", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.buscar.setText("")
    # retranslateUi

