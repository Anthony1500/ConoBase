# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_subcat.ui'
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
        Dialog.resize(400, 399)
        self.lista_subcat = QListView(Dialog)
        self.lista_subcat.setObjectName(u"lista_subcat")
        self.lista_subcat.setGeometry(QRect(20, 120, 361, 261))
        self.lista_subcat.setLayoutDirection(Qt.LeftToRight)
        self.lista_subcat.setStyleSheet(u"QListView::item {\n"
"    /* No funcionar\u00e1 sin establecer los bordes */\n"
"    border: 0px;\n"
"    margin-left: 10px; /* Ajusta este valor para el margen deseado */\n"
"}")
        self.lista_subcat.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.lista_subcat.setAlternatingRowColors(True)
        self.lista_subcat.setTextElideMode(Qt.ElideRight)
        self.lista_subcat.setModelColumn(0)
        self.lista_subcat.setUniformItemSizes(False)
        self.lista_subcat.setSelectionRectVisible(False)
        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(10, 10, 41, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QFont()
        self.back.setFont(font)
        self.back.setMouseTracking(True)
        self.back.setStyleSheet(u"QPushButton {\n"
"   \n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-size: 20px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QSize(25, 25))
        self.buscar = QPushButton(Dialog)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setEnabled(True)
        self.buscar.setGeometry(QRect(298, 72, 41, 37))
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
        icon1 = QIcon()
        icon1.addFile(u"../images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar.setIcon(icon1)
        self.buscar.setIconSize(QSize(25, 30))
        self.textname_1 = QLabel(Dialog)
        self.textname_1.setObjectName(u"textname_1")
        self.textname_1.setGeometry(QRect(90, 20, 211, 51))
        self.textname_1.setStyleSheet(u"QLabel {\n"
"    \n"
"    color: white;\n"
"    font-size: 21px; /* Tama\u00f1o del texto */\n"
"    padding: 9px; /* Espaciado interno */\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 401))
        self.label.setPixmap(QPixmap(u"../images/background_2.png"))
        self.inputtext_search_subcat = MyTextEdit(Dialog)
        self.inputtext_search_subcat.setObjectName(u"inputtext_search_subcat")
        self.inputtext_search_subcat.setGeometry(QRect(70, 70, 271, 41))
        self.inputtext_search_subcat.setStyleSheet(u"QTextEdit {\n"
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
        self.inputtext_search_subcat.setAcceptRichText(True)
        self.textname_2 = QLabel(Dialog)
        self.textname_2.setObjectName(u"textname_2")
        self.textname_2.setGeometry(QRect(210, 0, 61, 21))
        self.textname_2.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 2px; /* Espaciado interno */\n"
"}")
        self.subcat_cat_text = QLabel(Dialog)
        self.subcat_cat_text.setObjectName(u"subcat_cat_text")
        self.subcat_cat_text.setGeometry(QRect(270, 0, 131, 21))
        self.subcat_cat_text.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}")
        self.back_2 = QPushButton(Dialog)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setGeometry(QRect(20, 70, 41, 41))
        self.back_2.setStyleSheet(u"QPushButton {\n"
"\n"
"    border-radius: 20px;\n"
"    border: 0px;\n"
"    color: white;\n"
"    font-size: 19px; /* Tama\u00f1o del texto */\n"
"    padding: 8px; /* Espaciado interno */\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9681EB;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"   border: 1px solid blue;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../images/addmore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_2.setIcon(icon2)
        self.back_2.setIconSize(QSize(48, 48))
        self.label.raise_()
        self.lista_subcat.raise_()
        self.back.raise_()
        self.textname_1.raise_()
        self.inputtext_search_subcat.raise_()
        self.buscar.raise_()
        self.textname_2.raise_()
        self.subcat_cat_text.raise_()
        self.back_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.back.setText("")
        self.buscar.setText("")
        self.textname_1.setText(QCoreApplication.translate("Dialog", u"Lista subcategor\u00edas:", None))
        self.label.setText("")
        self.textname_2.setText(QCoreApplication.translate("Dialog", u"Categor\u00eda:", None))
        self.subcat_cat_text.setText("")
        self.back_2.setText("")
    # retranslateUi

