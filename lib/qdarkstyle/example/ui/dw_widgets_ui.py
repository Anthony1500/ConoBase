# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_widgets.ui'
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
        DockWidget.resize(879, 548)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_81 = QLabel(self.dockWidgetContents)
        self.label_81.setObjectName(u"label_81")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)

        self.gridLayout.addWidget(self.label_81, 0, 1, 1, 1)

        self.label_82 = QLabel(self.dockWidgetContents)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font)

        self.gridLayout.addWidget(self.label_82, 0, 2, 1, 1)

        self.label_56 = QLabel(self.dockWidgetContents)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 0))
        self.label_56.setMaximumSize(QSize(16777215, 16777215))
        self.label_56.setFont(font)

        self.gridLayout.addWidget(self.label_56, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)

        self.listWidgetDis = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.listWidgetDis)
        QListWidgetItem(self.listWidgetDis)
        QListWidgetItem(self.listWidgetDis)
        QListWidgetItem(self.listWidgetDis)
        self.listWidgetDis.setObjectName(u"listWidgetDis")
        self.listWidgetDis.setEnabled(False)

        self.gridLayout.addWidget(self.listWidgetDis, 1, 2, 1, 1)

        self.label_57 = QLabel(self.dockWidgetContents)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 0))
        self.label_57.setMaximumSize(QSize(16777215, 16777215))
        self.label_57.setFont(font)

        self.gridLayout.addWidget(self.label_57, 2, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem6)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(0, 0))
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.treeWidget.setSortingEnabled(True)

        self.gridLayout.addWidget(self.treeWidget, 2, 1, 1, 1)

        self.treeWidgetDis = QTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem7 = QTreeWidgetItem(self.treeWidgetDis)
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9 = QTreeWidgetItem(self.treeWidgetDis)
        QTreeWidgetItem(__qtreewidgetitem9)
        self.treeWidgetDis.setObjectName(u"treeWidgetDis")
        self.treeWidgetDis.setEnabled(False)
        self.treeWidgetDis.setSortingEnabled(True)

        self.gridLayout.addWidget(self.treeWidgetDis, 2, 2, 1, 1)

        self.label_58 = QLabel(self.dockWidgetContents)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 0))
        self.label_58.setMaximumSize(QSize(16777215, 16777215))
        self.label_58.setFont(font)

        self.gridLayout.addWidget(self.label_58, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(self.dockWidgetContents)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 1)

        self.tableWidgetDis = QTableWidget(self.dockWidgetContents)
        if (self.tableWidgetDis.columnCount() < 2):
            self.tableWidgetDis.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.tableWidgetDis.rowCount() < 3):
            self.tableWidgetDis.setRowCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 1, __qtablewidgetitem21)
        self.tableWidgetDis.setObjectName(u"tableWidgetDis")
        self.tableWidgetDis.setEnabled(False)

        self.gridLayout.addWidget(self.tableWidgetDis, 3, 2, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Widgets", None))
        self.label_81.setText(QCoreApplication.translate("DockWidget", u"Enabled", None))
        self.label_82.setText(QCoreApplication.translate("DockWidget", u"Disabled", None))
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_56.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_56.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_56.setText(QCoreApplication.translate("DockWidget", u"ListWidget", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.listWidget.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.listWidget.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)

        __sortingEnabled1 = self.listWidgetDis.isSortingEnabled()
        self.listWidgetDis.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.listWidgetDis.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidgetDis.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidgetDis.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidgetDis.item(3)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("DockWidget", u"New Item", None));
        self.listWidgetDis.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_57.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_57.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_57.setText(QCoreApplication.translate("DockWidget", u"TreeWidget", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"New Column", None));

        __sortingEnabled2 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("DockWidget", u"Test", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem2.child(3)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem2.child(4)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem9 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem9.child(2)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem9.child(3)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem17 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem18 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem19 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled2)

#if QT_CONFIG(tooltip)
        self.treeWidget.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.treeWidget.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.treeWidget.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem21 = self.treeWidgetDis.headerItem()
        ___qtreewidgetitem21.setText(1, QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("DockWidget", u"New Column", None));

        __sortingEnabled3 = self.treeWidgetDis.isSortingEnabled()
        self.treeWidgetDis.setSortingEnabled(False)
        ___qtreewidgetitem22 = self.treeWidgetDis.topLevelItem(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(1, QCoreApplication.translate("DockWidget", u"Test", None));
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem23.child(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        ___qtreewidgetitem25 = self.treeWidgetDis.topLevelItem(1)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("DockWidget", u"New Item", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("DockWidget", u"New Subitem", None));
        self.treeWidgetDis.setSortingEnabled(__sortingEnabled3)

#if QT_CONFIG(tooltip)
        self.label_58.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_58.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_58.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_58.setText(QCoreApplication.translate("DockWidget", u"TableWidget", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"New Row", None));

        __sortingEnabled4 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"1.23", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DockWidget", u"Hello", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DockWidget", u"1,45", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DockWidget", u"Ol\u00e1", None));
        ___qtablewidgetitem9 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DockWidget", u"12/12/2012", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DockWidget", u"Oui", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled4)

#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem11 = self.tableWidgetDis.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtablewidgetitem12 = self.tableWidgetDis.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DockWidget", u"New Column", None));
        ___qtablewidgetitem13 = self.tableWidgetDis.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidgetDis.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidgetDis.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DockWidget", u"New Row", None));

        __sortingEnabled5 = self.tableWidgetDis.isSortingEnabled()
        self.tableWidgetDis.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.tableWidgetDis.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DockWidget", u"1.23", None));
        ___qtablewidgetitem17 = self.tableWidgetDis.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DockWidget", u"Hello", None));
        ___qtablewidgetitem18 = self.tableWidgetDis.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DockWidget", u"1,45", None));
        ___qtablewidgetitem19 = self.tableWidgetDis.item(1, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DockWidget", u"Ol\u00e1", None));
        ___qtablewidgetitem20 = self.tableWidgetDis.item(2, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DockWidget", u"12/12/2012", None));
        ___qtablewidgetitem21 = self.tableWidgetDis.item(2, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DockWidget", u"Oui", None));
        self.tableWidgetDis.setSortingEnabled(__sortingEnabled5)

    # retranslateUi

