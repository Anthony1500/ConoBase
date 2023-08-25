# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_containers_tabs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(578, 515)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)

        self.tabWidgetNorth = QTabWidget(self.dockWidgetContents)
        self.tabWidgetNorth.setObjectName(u"tabWidgetNorth")
        self.tabWidgetNorth.setDocumentMode(False)
        self.tabWidgetNorth.setTabsClosable(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_8 = QGridLayout(self.tab_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_52 = QLabel(self.tab_7)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_8.addWidget(self.label_52, 0, 0, 1, 1)

        self.tabWidgetNorth.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_4 = QGridLayout(self.tab_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 0, 0, 1, 1)

        self.tabWidgetNorth.addTab(self.tab_8, "")

        self.gridLayout_5.addWidget(self.tabWidgetNorth, 1, 0, 1, 1)

        self.tabWidgetNorth_2 = QTabWidget(self.dockWidgetContents)
        self.tabWidgetNorth_2.setObjectName(u"tabWidgetNorth_2")
        self.tabWidgetNorth_2.setEnabled(False)
        self.tabWidgetNorth_2.setDocumentMode(False)
        self.tabWidgetNorth_2.setTabsClosable(True)
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_10 = QGridLayout(self.tab_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_53 = QLabel(self.tab_9)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_10.addWidget(self.label_53, 0, 0, 1, 1)

        self.tabWidgetNorth_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_19 = QGridLayout(self.tab_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_49 = QLabel(self.tab_10)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_19.addWidget(self.label_49, 0, 0, 1, 1)

        self.tabWidgetNorth_2.addTab(self.tab_10, "")

        self.gridLayout_5.addWidget(self.tabWidgetNorth_2, 1, 1, 1, 1)

        self.tabWidgetWest = QTabWidget(self.dockWidgetContents)
        self.tabWidgetWest.setObjectName(u"tabWidgetWest")
        self.tabWidgetWest.setTabPosition(QTabWidget.West)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_3 = QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_39 = QLabel(self.tab_5)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 0, 0, 1, 1)

        self.tabWidgetWest.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_54 = QLabel(self.tab_6)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_9.addWidget(self.label_54, 0, 0, 1, 1)

        self.tabWidgetWest.addTab(self.tab_6, "")

        self.gridLayout_5.addWidget(self.tabWidgetWest, 2, 0, 1, 1)

        self.tabWidgetWest_2 = QTabWidget(self.dockWidgetContents)
        self.tabWidgetWest_2.setObjectName(u"tabWidgetWest_2")
        self.tabWidgetWest_2.setEnabled(False)
        self.tabWidgetWest_2.setTabPosition(QTabWidget.West)
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_20 = QGridLayout(self.tab_11)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_50 = QLabel(self.tab_11)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_20.addWidget(self.label_50, 0, 0, 1, 1)

        self.tabWidgetWest_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_21 = QGridLayout(self.tab_12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_72 = QLabel(self.tab_12)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_21.addWidget(self.label_72, 0, 0, 1, 1)

        self.tabWidgetWest_2.addTab(self.tab_12, "")

        self.gridLayout_5.addWidget(self.tabWidgetWest_2, 2, 1, 1, 1)

        self.tabWidgetEast = QTabWidget(self.dockWidgetContents)
        self.tabWidgetEast.setObjectName(u"tabWidgetEast")
        self.tabWidgetEast.setTabPosition(QTabWidget.East)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_38 = QLabel(self.tab_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 0, 0, 1, 1)

        self.tabWidgetEast.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_11 = QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_55 = QLabel(self.tab_4)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_11.addWidget(self.label_55, 0, 0, 1, 1)

        self.tabWidgetEast.addTab(self.tab_4, "")

        self.gridLayout_5.addWidget(self.tabWidgetEast, 3, 0, 1, 1)

        self.tabWidgetEast_2 = QTabWidget(self.dockWidgetContents)
        self.tabWidgetEast_2.setObjectName(u"tabWidgetEast_2")
        self.tabWidgetEast_2.setEnabled(False)
        self.tabWidgetEast_2.setTabPosition(QTabWidget.East)
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_22 = QGridLayout(self.tab_13)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_51 = QLabel(self.tab_13)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_22.addWidget(self.label_51, 0, 0, 1, 1)

        self.tabWidgetEast_2.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_30 = QGridLayout(self.tab_14)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_73 = QLabel(self.tab_14)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_30.addWidget(self.label_73, 0, 0, 1, 1)

        self.tabWidgetEast_2.addTab(self.tab_14, "")

        self.gridLayout_5.addWidget(self.tabWidgetEast_2, 3, 1, 1, 1)

        self.tabWidgetSouth = QTabWidget(self.dockWidgetContents)
        self.tabWidgetSouth.setObjectName(u"tabWidgetSouth")
        self.tabWidgetSouth.setTabPosition(QTabWidget.South)
        self.tabWidgetSouth.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_34 = QLabel(self.tab)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)

        self.tabWidgetSouth.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_18 = QGridLayout(self.tab_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_62 = QLabel(self.tab_2)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_18.addWidget(self.label_62, 0, 0, 1, 1)

        self.tabWidgetSouth.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidgetSouth, 4, 0, 1, 1)

        self.tabWidgetSouth_2 = QTabWidget(self.dockWidgetContents)
        self.tabWidgetSouth_2.setObjectName(u"tabWidgetSouth_2")
        self.tabWidgetSouth_2.setEnabled(False)
        self.tabWidgetSouth_2.setTabPosition(QTabWidget.South)
        self.tabWidgetSouth_2.setTabsClosable(True)
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_31 = QGridLayout(self.tab_15)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_35 = QLabel(self.tab_15)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_31.addWidget(self.label_35, 0, 0, 1, 1)

        self.tabWidgetSouth_2.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_32 = QGridLayout(self.tab_16)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_74 = QLabel(self.tab_16)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_32.addWidget(self.label_74, 0, 0, 1, 1)

        self.tabWidgetSouth_2.addTab(self.tab_16, "")

        self.gridLayout_5.addWidget(self.tabWidgetSouth_2, 4, 1, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidgetNorth.setCurrentIndex(0)
        self.tabWidgetNorth_2.setCurrentIndex(1)
        self.tabWidgetWest.setCurrentIndex(0)
        self.tabWidgetWest_2.setCurrentIndex(0)
        self.tabWidgetEast.setCurrentIndex(0)
        self.tabWidgetEast_2.setCurrentIndex(0)
        self.tabWidgetSouth.setCurrentIndex(0)
        self.tabWidgetSouth_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Containers - Tabs", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Enabled", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"Disabled", None))
        self.label_52.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget North Closable Tab 1", None))
        self.tabWidgetNorth.setTabText(self.tabWidgetNorth.indexOf(self.tab_7), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_48.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget North Closable Tab 2", None))
        self.tabWidgetNorth.setTabText(self.tabWidgetNorth.indexOf(self.tab_8), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_53.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget North Closable Tab 1", None))
        self.tabWidgetNorth_2.setTabText(self.tabWidgetNorth_2.indexOf(self.tab_9), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_49.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget North Closable Tab 2", None))
        self.tabWidgetNorth_2.setTabText(self.tabWidgetNorth_2.indexOf(self.tab_10), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_39.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget West Tab 1", None))
        self.tabWidgetWest.setTabText(self.tabWidgetWest.indexOf(self.tab_5), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_54.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget West Tab 2", None))
        self.tabWidgetWest.setTabText(self.tabWidgetWest.indexOf(self.tab_6), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_50.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget West Tab 1", None))
        self.tabWidgetWest_2.setTabText(self.tabWidgetWest_2.indexOf(self.tab_11), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_72.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget West Tab 2", None))
        self.tabWidgetWest_2.setTabText(self.tabWidgetWest_2.indexOf(self.tab_12), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_38.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget East Tab 1", None))
        self.tabWidgetEast.setTabText(self.tabWidgetEast.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_55.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget East Tab 2", None))
        self.tabWidgetEast.setTabText(self.tabWidgetEast.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_51.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget East Tab 1", None))
        self.tabWidgetEast_2.setTabText(self.tabWidgetEast_2.indexOf(self.tab_13), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_73.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget East Tab 2", None))
        self.tabWidgetEast_2.setTabText(self.tabWidgetEast_2.indexOf(self.tab_14), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_34.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget South Closable Tab 1", None))
        self.tabWidgetSouth.setTabText(self.tabWidgetSouth.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_62.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget South Closable Tab 2", None))
        self.tabWidgetSouth.setTabText(self.tabWidgetSouth.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Tab 2", None))
        self.label_35.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget South Closable Tab 1", None))
        self.tabWidgetSouth_2.setTabText(self.tabWidgetSouth_2.indexOf(self.tab_15), QCoreApplication.translate("DockWidget", u"Tab 1", None))
        self.label_74.setText(QCoreApplication.translate("DockWidget", u"Inside TabWidget South Closable Tab 2", None))
        self.tabWidgetSouth_2.setTabText(self.tabWidgetSouth_2.indexOf(self.tab_16), QCoreApplication.translate("DockWidget", u"Tab 2", None))
    # retranslateUi

