from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecordExtradition(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 497)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.record_button = QtWidgets.QPushButton(self.centralwidget)
        self.record_button.setGeometry(QtCore.QRect(110, 410, 331, 51))
        self.record_button.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(173, 216, 230, 255), stop:1 rgba(224, 255, 255, 255));\n"
"    color: #4a4a4a;\n"
"    border: 2px solid #8BACC9;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(209, 249, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 149, 237, 255), stop:1 rgba(173, 216, 230, 255));\n"
"}")
        self.record_button.setObjectName("record_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 330, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.date_extradition = QtWidgets.QDateEdit(self.centralwidget)
        self.date_extradition.setGeometry(QtCore.QRect(90, 370, 110, 22))
        self.date_extradition.setObjectName("date_extradition")
        self.date_return = QtWidgets.QDateEdit(self.centralwidget)
        self.date_return.setGeometry(QtCore.QRect(340, 370, 110, 22))
        self.date_return.setObjectName("date_return")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 251, 261))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(280, 60, 251, 261))
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выдача книг"))
        self.label.setText(_translate("MainWindow", "Книга"))
        self.record_button.setText(_translate("MainWindow", "Записать"))
        self.label_2.setText(_translate("MainWindow", "Читатель"))
        self.label_3.setText(_translate("MainWindow", "Дата выдачи:"))
        self.label_4.setText(_translate("MainWindow", "Дата возврата:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RecordExtradition()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
