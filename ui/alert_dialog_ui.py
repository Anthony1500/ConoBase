# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert_dialog.ui'
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
        Dialog.resize(277, 55)
        self.dialog_image = QLabel(Dialog)
        self.dialog_image.setObjectName(u"dialog_image")
        self.dialog_image.setGeometry(QRect(-4, 0, 71, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_image.sizePolicy().hasHeightForWidth())
        self.dialog_image.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(1)
        self.dialog_image.setFont(font)
        self.dialog_image.setAutoFillBackground(False)
        self.dialog_image.setStyleSheet(u"QLabel {\n"
"    \n"
"  \n"
"    border: 0px;\n"
"}")
        self.dialog_image.setScaledContents(False)
        self.dialog_image.setAlignment(Qt.AlignCenter)
        self.dialog_image.setWordWrap(False)
        self.dialog_image.setMargin(0)
        self.dialog_text = QLabel(Dialog)
        self.dialog_text.setObjectName(u"dialog_text")
        self.dialog_text.setGeometry(QRect(50, 0, 221, 51))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.dialog_text.setPalette(palette)
        font1 = QFont()
        self.dialog_text.setFont(font1)
        self.dialog_text.setLayoutDirection(Qt.LeftToRight)
        self.dialog_text.setAutoFillBackground(False)
        self.dialog_text.setStyleSheet(u"QLabel {\n"
"    \n"
"    color: black;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"    border: 0px;\n"
"}\n"
"\n"
"")
        self.dialog_text.setInputMethodHints(Qt.ImhNone)
        self.dialog_text.setLineWidth(0)
        self.dialog_text.setTextFormat(Qt.PlainText)
        self.dialog_text.setScaledContents(False)
        self.dialog_text.setWordWrap(False)
        self.dialog_text.setMargin(-1)
        self.dialog_text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_image.setText("")
        self.dialog_text.setText("")
    # retranslateUi

