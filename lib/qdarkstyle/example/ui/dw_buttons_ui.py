# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_buttons.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import style_rc

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(580, 522)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_72 = QLabel(self.dockWidgetContents)
        self.label_72.setObjectName(u"label_72")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)

        self.gridLayout.addWidget(self.label_72, 0, 1, 1, 1)

        self.label_73 = QLabel(self.dockWidgetContents)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font)

        self.gridLayout.addWidget(self.label_73, 0, 4, 1, 1)

        self.label_26 = QLabel(self.dockWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setMaximumSize(QSize(16777215, 16777215))
        self.label_26.setFont(font)

        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 3)

        self.pushButtonDis = QPushButton(self.dockWidgetContents)
        self.pushButtonDis.setObjectName(u"pushButtonDis")
        self.pushButtonDis.setEnabled(False)
        self.pushButtonDis.setMinimumSize(QSize(0, 0))
        self.pushButtonDis.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.pushButtonDis, 1, 4, 1, 3)

        self.label_74 = QLabel(self.dockWidgetContents)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font)

        self.gridLayout.addWidget(self.label_74, 2, 0, 1, 1)

        self.pushButtonChecked = QPushButton(self.dockWidgetContents)
        self.pushButtonChecked.setObjectName(u"pushButtonChecked")
        self.pushButtonChecked.setMaximumSize(QSize(16777215, 16777215))
        self.pushButtonChecked.setCheckable(True)
        self.pushButtonChecked.setChecked(True)

        self.gridLayout.addWidget(self.pushButtonChecked, 2, 1, 1, 3)

        self.pushButtonCheckedDis = QPushButton(self.dockWidgetContents)
        self.pushButtonCheckedDis.setObjectName(u"pushButtonCheckedDis")
        self.pushButtonCheckedDis.setEnabled(False)
        self.pushButtonCheckedDis.setCheckable(True)
        self.pushButtonCheckedDis.setChecked(True)

        self.gridLayout.addWidget(self.pushButtonCheckedDis, 2, 4, 1, 3)

        self.label_76 = QLabel(self.dockWidgetContents)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font)

        self.gridLayout.addWidget(self.label_76, 3, 0, 1, 1)

        self.pushButtonUnchecked = QPushButton(self.dockWidgetContents)
        self.pushButtonUnchecked.setObjectName(u"pushButtonUnchecked")
        self.pushButtonUnchecked.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonUnchecked, 3, 1, 1, 3)

        self.pushButtonUncheckedDis = QPushButton(self.dockWidgetContents)
        self.pushButtonUncheckedDis.setObjectName(u"pushButtonUncheckedDis")
        self.pushButtonUncheckedDis.setEnabled(False)
        self.pushButtonUncheckedDis.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonUncheckedDis, 3, 4, 1, 3)

        self.label_33 = QLabel(self.dockWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setFont(font)

        self.gridLayout.addWidget(self.label_33, 4, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.dockWidgetContents)
        self.toolButton_4.setObjectName(u"toolButton_4")
        icon = QIcon()
        icon.addFile(u":/qss_icons/rc/window_undock_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_4, 4, 1, 1, 1)

        self.toolButton = QToolButton(self.dockWidgetContents)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 0))
        self.toolButton.setMaximumSize(QSize(16777215, 16777215))
        self.toolButton.setIcon(icon)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButton, 4, 2, 1, 1)

        self.toolButtonIcon = QToolButton(self.dockWidgetContents)
        self.toolButtonIcon.setObjectName(u"toolButtonIcon")
        icon1 = QIcon()
        icon1.addFile(u":/qss_icons/dark/rc/window_undock_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonIcon.setIcon(icon1)

        self.gridLayout.addWidget(self.toolButtonIcon, 4, 3, 1, 1)

        self.toolButton_9 = QToolButton(self.dockWidgetContents)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setEnabled(False)
        self.toolButton_9.setIcon(icon)
        self.toolButton_9.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_9, 4, 4, 1, 1)

        self.toolButton_8 = QToolButton(self.dockWidgetContents)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(False)
        self.toolButton_8.setMinimumSize(QSize(0, 0))
        self.toolButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.toolButton_8.setIcon(icon)
        self.toolButton_8.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButton_8, 4, 5, 1, 1)

        self.toolButtonIcon_2 = QToolButton(self.dockWidgetContents)
        self.toolButtonIcon_2.setObjectName(u"toolButtonIcon_2")
        self.toolButtonIcon_2.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/qss_icons/${ID}/rc/window_undock_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonIcon_2.setIcon(icon2)

        self.gridLayout.addWidget(self.toolButtonIcon_2, 4, 6, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.dockWidgetContents)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setIcon(icon)
        self.toolButton_5.setCheckable(True)
        self.toolButton_5.setChecked(True)
        self.toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_5, 5, 1, 1, 1)

        self.toolButtonChecked = QToolButton(self.dockWidgetContents)
        self.toolButtonChecked.setObjectName(u"toolButtonChecked")
        self.toolButtonChecked.setIcon(icon)
        self.toolButtonChecked.setCheckable(True)
        self.toolButtonChecked.setChecked(True)
        self.toolButtonChecked.setPopupMode(QToolButton.DelayedPopup)
        self.toolButtonChecked.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButtonChecked, 5, 2, 1, 1)

        self.toolButtonCheckedIcon = QToolButton(self.dockWidgetContents)
        self.toolButtonCheckedIcon.setObjectName(u"toolButtonCheckedIcon")
        self.toolButtonCheckedIcon.setIcon(icon1)
        self.toolButtonCheckedIcon.setCheckable(True)
        self.toolButtonCheckedIcon.setChecked(True)

        self.gridLayout.addWidget(self.toolButtonCheckedIcon, 5, 3, 1, 1)

        self.toolButton_10 = QToolButton(self.dockWidgetContents)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(False)
        self.toolButton_10.setIcon(icon)
        self.toolButton_10.setCheckable(True)
        self.toolButton_10.setChecked(True)
        self.toolButton_10.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_10, 5, 4, 1, 1)

        self.toolButtonChecked_2 = QToolButton(self.dockWidgetContents)
        self.toolButtonChecked_2.setObjectName(u"toolButtonChecked_2")
        self.toolButtonChecked_2.setEnabled(False)
        self.toolButtonChecked_2.setIcon(icon)
        self.toolButtonChecked_2.setCheckable(True)
        self.toolButtonChecked_2.setChecked(True)
        self.toolButtonChecked_2.setPopupMode(QToolButton.DelayedPopup)
        self.toolButtonChecked_2.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButtonChecked_2, 5, 5, 1, 1)

        self.toolButtonCheckedIcon_2 = QToolButton(self.dockWidgetContents)
        self.toolButtonCheckedIcon_2.setObjectName(u"toolButtonCheckedIcon_2")
        self.toolButtonCheckedIcon_2.setEnabled(False)
        self.toolButtonCheckedIcon_2.setIcon(icon2)
        self.toolButtonCheckedIcon_2.setCheckable(True)
        self.toolButtonCheckedIcon_2.setChecked(True)

        self.gridLayout.addWidget(self.toolButtonCheckedIcon_2, 5, 6, 1, 1)

        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.dockWidgetContents)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_6, 6, 1, 1, 1)

        self.toolButton_2 = QToolButton(self.dockWidgetContents)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_2, 6, 2, 1, 1)

        self.toolButton_3 = QToolButton(self.dockWidgetContents)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_3, 6, 3, 1, 1)

        self.toolButton_12 = QToolButton(self.dockWidgetContents)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(False)
        self.toolButton_12.setIcon(icon)
        self.toolButton_12.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_12, 6, 4, 1, 1)

        self.toolButton_7 = QToolButton(self.dockWidgetContents)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_7, 6, 5, 1, 1)

        self.toolButton_11 = QToolButton(self.dockWidgetContents)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(False)
        self.toolButton_11.setIcon(icon)
        self.toolButton_11.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.gridLayout.addWidget(self.toolButton_11, 6, 6, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.toolButtonArrowUp = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowUp.setObjectName(u"toolButtonArrowUp")
        self.toolButtonArrowUp.setArrowType(Qt.UpArrow)

        self.gridLayout_3.addWidget(self.toolButtonArrowUp, 0, 1, 1, 1)

        self.toolButtonArrowLeft = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowLeft.setObjectName(u"toolButtonArrowLeft")
        self.toolButtonArrowLeft.setArrowType(Qt.LeftArrow)

        self.gridLayout_3.addWidget(self.toolButtonArrowLeft, 0, 3, 1, 1)

        self.toolButtonArrowRight = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowRight.setObjectName(u"toolButtonArrowRight")
        self.toolButtonArrowRight.setArrowType(Qt.RightArrow)

        self.gridLayout_3.addWidget(self.toolButtonArrowRight, 0, 2, 1, 1)

        self.toolButtonArrowDown = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowDown.setObjectName(u"toolButtonArrowDown")
        self.toolButtonArrowDown.setArrowType(Qt.DownArrow)

        self.gridLayout_3.addWidget(self.toolButtonArrowDown, 0, 0, 1, 1)

        self.toolButtonDots = QToolButton(self.dockWidgetContents)
        self.toolButtonDots.setObjectName(u"toolButtonDots")

        self.gridLayout_3.addWidget(self.toolButtonDots, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 7, 1, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolButtonArrowUpDis = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowUpDis.setObjectName(u"toolButtonArrowUpDis")
        self.toolButtonArrowUpDis.setEnabled(False)
        self.toolButtonArrowUpDis.setArrowType(Qt.UpArrow)

        self.gridLayout_2.addWidget(self.toolButtonArrowUpDis, 0, 1, 1, 1)

        self.toolButtonArrowDownDis = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowDownDis.setObjectName(u"toolButtonArrowDownDis")
        self.toolButtonArrowDownDis.setEnabled(False)
        self.toolButtonArrowDownDis.setArrowType(Qt.DownArrow)

        self.gridLayout_2.addWidget(self.toolButtonArrowDownDis, 0, 0, 1, 1)

        self.toolButtonArrowRightDis = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowRightDis.setObjectName(u"toolButtonArrowRightDis")
        self.toolButtonArrowRightDis.setEnabled(False)
        self.toolButtonArrowRightDis.setArrowType(Qt.RightArrow)

        self.gridLayout_2.addWidget(self.toolButtonArrowRightDis, 0, 2, 1, 1)

        self.toolButtonArrowLeftDis = QToolButton(self.dockWidgetContents)
        self.toolButtonArrowLeftDis.setObjectName(u"toolButtonArrowLeftDis")
        self.toolButtonArrowLeftDis.setEnabled(False)
        self.toolButtonArrowLeftDis.setArrowType(Qt.LeftArrow)

        self.gridLayout_2.addWidget(self.toolButtonArrowLeftDis, 0, 3, 1, 1)

        self.toolButtonDotsDis = QToolButton(self.dockWidgetContents)
        self.toolButtonDotsDis.setObjectName(u"toolButtonDotsDis")
        self.toolButtonDotsDis.setEnabled(False)

        self.gridLayout_2.addWidget(self.toolButtonDotsDis, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 7, 4, 1, 2)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButtonDelayedPopup = QToolButton(self.dockWidgetContents)
        self.toolButtonDelayedPopup.setObjectName(u"toolButtonDelayedPopup")
        self.toolButtonDelayedPopup.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.toolButtonDelayedPopup)

        self.toolButtonMenuButtonPopup = QToolButton(self.dockWidgetContents)
        self.toolButtonMenuButtonPopup.setObjectName(u"toolButtonMenuButtonPopup")
        self.toolButtonMenuButtonPopup.setPopupMode(QToolButton.MenuButtonPopup)

        self.horizontalLayout.addWidget(self.toolButtonMenuButtonPopup)

        self.toolButtonInstantPopup = QToolButton(self.dockWidgetContents)
        self.toolButtonInstantPopup.setObjectName(u"toolButtonInstantPopup")
        self.toolButtonInstantPopup.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout.addWidget(self.toolButtonInstantPopup)


        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButtonDelayedPopupDis = QToolButton(self.dockWidgetContents)
        self.toolButtonDelayedPopupDis.setObjectName(u"toolButtonDelayedPopupDis")
        self.toolButtonDelayedPopupDis.setEnabled(False)
        self.toolButtonDelayedPopupDis.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.toolButtonDelayedPopupDis)

        self.toolButtonMenuButtonPopupDis = QToolButton(self.dockWidgetContents)
        self.toolButtonMenuButtonPopupDis.setObjectName(u"toolButtonMenuButtonPopupDis")
        self.toolButtonMenuButtonPopupDis.setEnabled(False)
        self.toolButtonMenuButtonPopupDis.setPopupMode(QToolButton.MenuButtonPopup)

        self.horizontalLayout_2.addWidget(self.toolButtonMenuButtonPopupDis)

        self.toolButtonInstantPopupDis = QToolButton(self.dockWidgetContents)
        self.toolButtonInstantPopupDis.setObjectName(u"toolButtonInstantPopupDis")
        self.toolButtonInstantPopupDis.setEnabled(False)
        self.toolButtonInstantPopupDis.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout_2.addWidget(self.toolButtonInstantPopupDis)


        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 4, 1, 3)

        self.label_75 = QLabel(self.dockWidgetContents)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font)

        self.gridLayout.addWidget(self.label_75, 9, 0, 1, 1)

        self.radioButtonChecked = QRadioButton(self.dockWidgetContents)
        self.radioButtonChecked.setObjectName(u"radioButtonChecked")
        self.radioButtonChecked.setChecked(True)
        self.radioButtonChecked.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButtonChecked, 9, 1, 1, 1)

        self.radioButtonCheckedDis = QRadioButton(self.dockWidgetContents)
        self.radioButtonCheckedDis.setObjectName(u"radioButtonCheckedDis")
        self.radioButtonCheckedDis.setEnabled(False)
        self.radioButtonCheckedDis.setChecked(True)
        self.radioButtonCheckedDis.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButtonCheckedDis, 9, 4, 1, 1)

        self.label_29 = QLabel(self.dockWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))
        self.label_29.setMaximumSize(QSize(16777215, 16777215))
        self.label_29.setFont(font)

        self.gridLayout.addWidget(self.label_29, 10, 0, 1, 1)

        self.radioButtonUnchecked = QRadioButton(self.dockWidgetContents)
        self.radioButtonUnchecked.setObjectName(u"radioButtonUnchecked")
        self.radioButtonUnchecked.setMinimumSize(QSize(0, 0))
        self.radioButtonUnchecked.setMaximumSize(QSize(16777215, 16777215))
        self.radioButtonUnchecked.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButtonUnchecked, 10, 1, 1, 1)

        self.radioButtonUncheckedDis = QRadioButton(self.dockWidgetContents)
        self.radioButtonUncheckedDis.setObjectName(u"radioButtonUncheckedDis")
        self.radioButtonUncheckedDis.setEnabled(False)
        self.radioButtonUncheckedDis.setMinimumSize(QSize(0, 0))
        self.radioButtonUncheckedDis.setMaximumSize(QSize(16777215, 16777215))
        self.radioButtonUncheckedDis.setChecked(False)
        self.radioButtonUncheckedDis.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButtonUncheckedDis, 10, 4, 1, 1)

        self.label_53 = QLabel(self.dockWidgetContents)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.gridLayout.addWidget(self.label_53, 11, 0, 1, 1)

        self.checkBoxChecked = QCheckBox(self.dockWidgetContents)
        self.checkBoxChecked.setObjectName(u"checkBoxChecked")
        self.checkBoxChecked.setChecked(True)

        self.gridLayout.addWidget(self.checkBoxChecked, 11, 1, 1, 1)

        self.checkBoxCheckedDis = QCheckBox(self.dockWidgetContents)
        self.checkBoxCheckedDis.setObjectName(u"checkBoxCheckedDis")
        self.checkBoxCheckedDis.setEnabled(False)
        self.checkBoxCheckedDis.setChecked(True)

        self.gridLayout.addWidget(self.checkBoxCheckedDis, 11, 4, 1, 1)

        self.label_30 = QLabel(self.dockWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setMaximumSize(QSize(16777215, 16777215))
        self.label_30.setFont(font)

        self.gridLayout.addWidget(self.label_30, 12, 0, 1, 1)

        self.checkBoxEnabled = QCheckBox(self.dockWidgetContents)
        self.checkBoxEnabled.setObjectName(u"checkBoxEnabled")
        self.checkBoxEnabled.setMinimumSize(QSize(0, 0))
        self.checkBoxEnabled.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxEnabled.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxEnabled, 12, 1, 1, 1)

        self.checkBoxUncheckedDis = QCheckBox(self.dockWidgetContents)
        self.checkBoxUncheckedDis.setObjectName(u"checkBoxUncheckedDis")
        self.checkBoxUncheckedDis.setEnabled(False)
        self.checkBoxUncheckedDis.setMinimumSize(QSize(0, 0))
        self.checkBoxUncheckedDis.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxUncheckedDis.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxUncheckedDis, 12, 4, 1, 1)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)

        self.checkBoxTristate = QCheckBox(self.dockWidgetContents)
        self.checkBoxTristate.setObjectName(u"checkBoxTristate")
        self.checkBoxTristate.setCheckable(True)
        self.checkBoxTristate.setChecked(False)
        self.checkBoxTristate.setTristate(True)

        self.gridLayout.addWidget(self.checkBoxTristate, 13, 1, 1, 1)

        self.checkBoxTristateDis = QCheckBox(self.dockWidgetContents)
        self.checkBoxTristateDis.setObjectName(u"checkBoxTristateDis")
        self.checkBoxTristateDis.setEnabled(False)
        self.checkBoxTristateDis.setChecked(False)
        self.checkBoxTristateDis.setTristate(True)

        self.gridLayout.addWidget(self.checkBoxTristateDis, 13, 4, 1, 1)

        self.label_31 = QLabel(self.dockWidgetContents)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setMaximumSize(QSize(16777215, 16777215))
        self.label_31.setFont(font)

        self.gridLayout.addWidget(self.label_31, 14, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.dockWidgetContents)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setMinimumSize(QSize(0, 0))
        self.commandLinkButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.commandLinkButton, 14, 1, 1, 3)

        self.commandLinkButtonDIs = QCommandLinkButton(self.dockWidgetContents)
        self.commandLinkButtonDIs.setObjectName(u"commandLinkButtonDIs")
        self.commandLinkButtonDIs.setEnabled(False)
        self.commandLinkButtonDIs.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.commandLinkButtonDIs, 14, 4, 1, 3)

        self.label_32 = QLabel(self.dockWidgetContents)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setFont(font)

        self.gridLayout.addWidget(self.label_32, 15, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.dockWidgetContents)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 15, 1, 1, 3)

        self.buttonBoxDis = QDialogButtonBox(self.dockWidgetContents)
        self.buttonBoxDis.setObjectName(u"buttonBoxDis")
        self.buttonBoxDis.setEnabled(False)
        self.buttonBoxDis.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBoxDis, 15, 4, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 4, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 16, 0, 1, 1)

        self.label_36 = QLabel(self.dockWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_36, 17, 0, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.radioButtonChecked.clicked.connect(self.radioButtonCheckedDis.setChecked)
        self.radioButtonUnchecked.clicked.connect(self.radioButtonUncheckedDis.setChecked)
        self.checkBoxChecked.clicked.connect(self.checkBoxCheckedDis.setChecked)
        self.checkBoxEnabled.clicked.connect(self.checkBoxUncheckedDis.setChecked)
        self.commandLinkButton.clicked.connect(self.commandLinkButtonDIs.setChecked)
        self.pushButtonChecked.clicked.connect(self.pushButtonCheckedDis.setChecked)
        self.pushButtonUnchecked.clicked.connect(self.pushButtonUncheckedDis.setChecked)
        self.pushButton.clicked.connect(self.pushButtonDis.click)

        self.pushButtonDis.setDefault(False)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Buttons", None))
        self.label_72.setText(QCoreApplication.translate("DockWidget", u"Enabled", None))
        self.label_73.setText(QCoreApplication.translate("DockWidget", u"Disabled", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_26.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_26.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_26.setText(QCoreApplication.translate("DockWidget", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"OK", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDis.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonDis.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButtonDis.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButtonDis.setText(QCoreApplication.translate("DockWidget", u"OK", None))
        self.label_74.setText(QCoreApplication.translate("DockWidget", u"PushButton", None))
        self.pushButtonChecked.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.pushButtonCheckedDis.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.label_76.setText(QCoreApplication.translate("DockWidget", u"PushButton", None))
        self.pushButtonUnchecked.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
        self.pushButtonUncheckedDis.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_33.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_33.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_33.setText(QCoreApplication.translate("DockWidget", u"ToolButton (Both/Text/Icon)", None))
        self.toolButton_4.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButtonIcon.setText(QCoreApplication.translate("DockWidget", u"Icon", None))
        self.toolButton_9.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
#if QT_CONFIG(tooltip)
        self.toolButton_8.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton_8.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton_8.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton_8.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButtonIcon_2.setText(QCoreApplication.translate("DockWidget", u"Icon", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-weight:600;\">ToolButton (Both/Text/Icon)</span></p></body></html>", None))
        self.toolButton_5.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.toolButtonChecked.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.toolButtonCheckedIcon.setText(QCoreApplication.translate("DockWidget", u"Icon Checked", None))
        self.toolButton_10.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.toolButtonChecked_2.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.toolButtonCheckedIcon_2.setText(QCoreApplication.translate("DockWidget", u"Icon Checked", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-weight:600;\">ToolButton (FollowStyle)</span></p></body></html>", None))
        self.toolButton_6.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButton_2.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButton_3.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButton_12.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButton_7.setText(QCoreApplication.translate("DockWidget", u"Tool", None))
        self.toolButton_11.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-weight:600;\">ToolButton (Arrows)</span></p></body></html>", None))
        self.toolButtonArrowUp.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowLeft.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowRight.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowDown.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonDots.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowUpDis.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowDownDis.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowRightDis.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonArrowLeftDis.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.toolButtonDotsDis.setText(QCoreApplication.translate("DockWidget", u"...", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-weight:600;\">ToolButton (Menus)</span></p></body></html>", None))
        self.toolButtonDelayedPopup.setText(QCoreApplication.translate("DockWidget", u"Delayed", None))
        self.toolButtonMenuButtonPopup.setText(QCoreApplication.translate("DockWidget", u"Menu", None))
        self.toolButtonInstantPopup.setText(QCoreApplication.translate("DockWidget", u"Instant", None))
        self.toolButtonDelayedPopupDis.setText(QCoreApplication.translate("DockWidget", u"Delayed", None))
        self.toolButtonMenuButtonPopupDis.setText(QCoreApplication.translate("DockWidget", u"Menu", None))
        self.toolButtonInstantPopupDis.setText(QCoreApplication.translate("DockWidget", u"Instant", None))
        self.label_75.setText(QCoreApplication.translate("DockWidget", u"RadioButton", None))
        self.radioButtonChecked.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.radioButtonCheckedDis.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_29.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_29.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_29.setText(QCoreApplication.translate("DockWidget", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.radioButtonUnchecked.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.radioButtonUnchecked.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.radioButtonUnchecked.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButtonUnchecked.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
#if QT_CONFIG(tooltip)
        self.radioButtonUncheckedDis.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.radioButtonUncheckedDis.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.radioButtonUncheckedDis.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButtonUncheckedDis.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
        self.label_53.setText(QCoreApplication.translate("DockWidget", u"CheckBox", None))
        self.checkBoxChecked.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
        self.checkBoxCheckedDis.setText(QCoreApplication.translate("DockWidget", u"Checked", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_30.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_30.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_30.setText(QCoreApplication.translate("DockWidget", u"CheckBox", None))
#if QT_CONFIG(tooltip)
        self.checkBoxEnabled.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBoxEnabled.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.checkBoxEnabled.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxEnabled.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUncheckedDis.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBoxUncheckedDis.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.checkBoxUncheckedDis.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxUncheckedDis.setText(QCoreApplication.translate("DockWidget", u"Unchecked", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"CheckBox", None))
        self.checkBoxTristate.setText(QCoreApplication.translate("DockWidget", u"Tristate", None))
        self.checkBoxTristateDis.setText(QCoreApplication.translate("DockWidget", u"Tristate", None))
#if QT_CONFIG(tooltip)
        self.label_31.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_31.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_31.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_31.setText(QCoreApplication.translate("DockWidget", u"CommandLinkButton", None))
#if QT_CONFIG(tooltip)
        self.commandLinkButton.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.commandLinkButton.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.commandLinkButton.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.commandLinkButton.setText(QCoreApplication.translate("DockWidget", u"Command", None))
        self.commandLinkButtonDIs.setText(QCoreApplication.translate("DockWidget", u"Command", None))
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_32.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_32.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_32.setText(QCoreApplication.translate("DockWidget", u"ButtonBox", None))
#if QT_CONFIG(tooltip)
        self.buttonBox.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.buttonBox.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.buttonBox.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_36.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_36.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_36.setText(QCoreApplication.translate("DockWidget", u"Inside DockWidget", None))
    # retranslateUi

