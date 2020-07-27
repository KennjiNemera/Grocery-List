# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtWidgets 


class Ui_MainWindow(object):

    item_list = []
    price_list = []
    item_counter = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont('Nirmala UI', 14))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 160, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QtGui.QFont('Nirmala UI', 14))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 320, 331, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grocery App"))
        self.pushButton.setText(_translate("MainWindow", "Add To List "))
        self.label.setText(_translate("MainWindow", "Price:"))
        self.label_2.setText(_translate("MainWindow", "Name Of The Item:"))

        # event listeners
        self.pushButton.clicked.connect(self.createList)

    def createList(self):

        # gets values from the input fields
        nameOfItem = str(self.lineEdit.text())
        costOfItem = 'R' + self.lineEdit_2.text()
        print(nameOfItem)
        print(costOfItem)

        # adds the values to the lists
        self.item_list.append(nameOfItem)
        self.price_list.append(costOfItem)

        # increment counter
        self.item_counter += 1

        # update the table
        self.tableWidget.setRowCount(self.item_counter)
        self.tableWidget.setColumnCount(3)

        # column headers
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Item"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Item num:"))

        # row items - prints the values into the table based on the size of the list
        for i in range(len(self.item_list)):
            self.tableWidget.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(self.item_list[i]))
            self.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(self.price_list[i]))
            self.tableWidget.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(str(i + 1)))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
