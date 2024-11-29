from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Extradition(object):
    def setupUi(self, menu_book):
        menu_book.setObjectName("menu_book")
        menu_book.resize(1030, 595)
        menu_book.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(menu_book)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 153, 173, 255), stop:1 rgba(255, 245, 204, 255));\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget {\n"
"    background: transparent;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1008, 446))
        self.scrollAreaWidgetContents.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        menu_book.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_book)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 26))
        self.menubar.setObjectName("menubar")
        menu_book.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_book)
        self.statusbar.setObjectName("statusbar")
        menu_book.setStatusBar(self.statusbar)

        self.retranslateUi(menu_book)
        QtCore.QMetaObject.connectSlotsByName(menu_book)

    def retranslateUi(self, menu_book):
        _translate = QtCore.QCoreApplication.translate
        menu_book.setWindowTitle(_translate("menu_book", "Выдача"))
        self.pushButton.setText(_translate("menu_book", "Добавить запись"))
        self.pushButton_2.setText(_translate("menu_book", "Обновить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_book = QtWidgets.QMainWindow()
    ui = Ui_Extradition()
    ui.setupUi(menu_book)
    menu_book.show()
    sys.exit(app.exec_())
