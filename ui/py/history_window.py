from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History(object):
    def setupUi(self, menu_book):
        menu_book.setObjectName("menu_book")
        menu_book.resize(960, 705)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 938, 632))
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
        menu_book.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_book)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        menu_book.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_book)
        self.statusbar.setObjectName("statusbar")
        menu_book.setStatusBar(self.statusbar)

        self.retranslateUi(menu_book)
        QtCore.QMetaObject.connectSlotsByName(menu_book)

    def retranslateUi(self, menu_book):
        _translate = QtCore.QCoreApplication.translate
        menu_book.setWindowTitle(_translate("menu_book", "История"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_book = QtWidgets.QMainWindow()
    ui = Ui_History()
    ui.setupUi(menu_book)
    menu_book.show()
    sys.exit(app.exec_())
