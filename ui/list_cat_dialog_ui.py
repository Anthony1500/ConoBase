# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_cat_dialog.ui'
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
        Dialog.resize(339, 69)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(1)
        font.setStrikeOut(False)
        font.setKerning(True)
        Dialog.setFont(font)
        Dialog.setFocusPolicy(Qt.TabFocus)
        Dialog.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"../images/logo_app.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 341, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(5, 5))
        self.label_2.setPixmap(QPixmap(u"../images/background_collection_1.png"))
        self.cat_title = QLabel(Dialog)
        self.cat_title.setObjectName(u"cat_title")
        self.cat_title.setGeometry(QRect(20, 0, 91, 21))
        self.cat_title.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}")
        self.cat_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.textname_2 = QLabel(Dialog)
        self.textname_2.setObjectName(u"textname_2")
        self.textname_2.setGeometry(QRect(20, 30, 131, 21))
        self.textname_2.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}")
        self.cat_data = QLabel(Dialog)
        self.cat_data.setObjectName(u"cat_data")
        self.cat_data.setGeometry(QRect(100, 0, 231, 21))
        self.cat_data.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}")
        self.cat_number = QLabel(Dialog)
        self.cat_number.setObjectName(u"cat_number")
        self.cat_number.setGeometry(QRect(140, 30, 111, 21))
        self.cat_number.setStyleSheet(u"QLabel {\n"
"    background-color: #6527BE;\n"
"    color: white;\n"
"    font-size: 12px; /* Tama\u00f1o del texto */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.cat_title.setText("")
        self.textname_2.setText(QCoreApplication.translate("Dialog", u"Esta categor\u00eda tiene:", None))
        self.cat_data.setText("")
        self.cat_number.setText("")
    # retranslateUi

