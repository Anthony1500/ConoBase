# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_subcat_dialog.ui'
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
        Dialog.resize(450, 431)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 481, 481))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(5, 5))
        self.label_3.setPixmap(QPixmap(u"../images/background_collection_3.png"))
        self.textname_2 = QLabel(Dialog)
        self.textname_2.setObjectName(u"textname_2")
        self.textname_2.setGeometry(QRect(10, 60, 51, 21))
        self.textname_2.setStyleSheet(u"QLabel {\n"
"   color: black;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"     border: 0px;\n"
"}")
        self.textname_2.setScaledContents(False)
        self.textname_3 = QLabel(Dialog)
        self.textname_3.setObjectName(u"textname_3")
        self.textname_3.setGeometry(QRect(10, 10, 81, 21))
        self.textname_3.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: black;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"    font-weight: bold;\n"
"     border: 0px;\n"
"}")
        self.cat_name = QLabel(Dialog)
        self.cat_name.setObjectName(u"cat_name")
        self.cat_name.setGeometry(QRect(80, 10, 311, 21))
        self.cat_name.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: black;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"    text-transform: uppercase;\n"
"     border: 0px;\n"
"}")
        self.cat_name.setAlignment(Qt.AlignCenter)
        self.text_title_sub = QLabel(Dialog)
        self.text_title_sub.setObjectName(u"text_title_sub")
        self.text_title_sub.setGeometry(QRect(70, 60, 341, 21))
        self.text_title_sub.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: black;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"     border: 0px;\n"
"}")
        self.textname_5 = QLabel(Dialog)
        self.textname_5.setObjectName(u"textname_5")
        self.textname_5.setGeometry(QRect(10, 80, 111, 23))
        self.textname_5.setStyleSheet(u"QLabel {\n"
"   color: black;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border: 0px;\n"
"}")
        self.textname_5.setScaledContents(False)
        self.text_date_hour = QLabel(Dialog)
        self.text_date_hour.setObjectName(u"text_date_hour")
        self.text_date_hour.setGeometry(QRect(110, 80, 171, 23))
        self.text_date_hour.setStyleSheet(u"QLabel {\n"
"   \n"
"    color: black;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"     border: 0px;\n"
"}")
        self.textname_7 = QLabel(Dialog)
        self.textname_7.setObjectName(u"textname_7")
        self.textname_7.setGeometry(QRect(10, 120, 91, 21))
        self.textname_7.setStyleSheet(u"QLabel {\n"
"   color: black;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"     border: 0px;\n"
"}")
        self.textname_7.setScaledContents(False)
        self.text_contem = QTextEdit(Dialog)
        self.text_contem.setObjectName(u"text_contem")
        self.text_contem.setGeometry(QRect(10, 150, 431, 271))
        self.text_contem.setStyleSheet(u"QTextEdit {\n"
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
"")
        self.text_contem.setReadOnly(True)
        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(405, 5, 41, 31))
        font = QFont()
        self.back.setFont(font)
        self.back.setMouseTracking(True)
        self.back.setStyleSheet(u"QPushButton {\n"
"    background-color: #d94040;\n"
"    border-radius: 10px;\n"
"    border: 0px;\n"
"    color: white;\n"
"    font-size: 19px; /* Tama\u00f1o del texto */\n"
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
        self.label_3.setText("")
        self.textname_2.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo :", None))
        self.textname_3.setText(QCoreApplication.translate("Dialog", u"Categor\u00eda :", None))
        self.cat_name.setText("")
        self.text_title_sub.setText("")
        self.textname_5.setText(QCoreApplication.translate("Dialog", u"Fecha y Hora : ", None))
        self.text_date_hour.setText("")
        self.textname_7.setText(QCoreApplication.translate("Dialog", u" Contenido :", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"X", None))
    # retranslateUi

