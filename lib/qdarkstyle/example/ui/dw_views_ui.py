# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_views.ui'
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
        DockWidget.resize(266, 387)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_70 = QLabel(self.dockWidgetContents)
        self.label_70.setObjectName(u"label_70")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)

        self.gridLayout.addWidget(self.label_70, 0, 1, 1, 1)

        self.label_80 = QLabel(self.dockWidgetContents)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font)

        self.gridLayout.addWidget(self.label_80, 0, 2, 1, 1)

        self.label_27 = QLabel(self.dockWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.gridLayout.addWidget(self.label_27, 1, 0, 1, 1)

        self.listView = QListView(self.dockWidgetContents)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 1, 1, 1)

        self.listViewDis = QListView(self.dockWidgetContents)
        self.listViewDis.setObjectName(u"listViewDis")
        self.listViewDis.setEnabled(False)

        self.gridLayout.addWidget(self.listViewDis, 1, 2, 1, 1)

        self.label_59 = QLabel(self.dockWidgetContents)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)

        self.gridLayout.addWidget(self.label_59, 2, 0, 1, 1)

        self.treeView = QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout.addWidget(self.treeView, 2, 1, 1, 1)

        self.treeViewDis = QTreeView(self.dockWidgetContents)
        self.treeViewDis.setObjectName(u"treeViewDis")
        self.treeViewDis.setEnabled(False)

        self.gridLayout.addWidget(self.treeViewDis, 2, 2, 1, 1)

        self.label_60 = QLabel(self.dockWidgetContents)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.gridLayout.addWidget(self.label_60, 3, 0, 1, 1)

        self.tableView = QTableView(self.dockWidgetContents)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 3, 1, 1, 1)

        self.tableViewDis = QTableView(self.dockWidgetContents)
        self.tableViewDis.setObjectName(u"tableViewDis")
        self.tableViewDis.setEnabled(False)

        self.gridLayout.addWidget(self.tableViewDis, 3, 2, 1, 1)

        self.label_61 = QLabel(self.dockWidgetContents)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font)

        self.gridLayout.addWidget(self.label_61, 4, 0, 1, 1)

        self.columnView = QColumnView(self.dockWidgetContents)
        self.columnView.setObjectName(u"columnView")

        self.gridLayout.addWidget(self.columnView, 4, 1, 1, 1)

        self.columnViewDis = QColumnView(self.dockWidgetContents)
        self.columnViewDis.setObjectName(u"columnViewDis")
        self.columnViewDis.setEnabled(False)

        self.gridLayout.addWidget(self.columnViewDis, 4, 2, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Views", None))
        self.label_70.setText(QCoreApplication.translate("DockWidget", u"Enabled", None))
        self.label_80.setText(QCoreApplication.translate("DockWidget", u"Disabled", None))
        self.label_27.setText(QCoreApplication.translate("DockWidget", u"ListView", None))
        self.label_59.setText(QCoreApplication.translate("DockWidget", u"TreeView", None))
        self.label_60.setText(QCoreApplication.translate("DockWidget", u"TableView", None))
        self.label_61.setText(QCoreApplication.translate("DockWidget", u"ColunmView", None))
    # retranslateUi

