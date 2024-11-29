from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(312, 416)
        Menu.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.book = QtWidgets.QPushButton(self.centralwidget)
        self.book.setGeometry(QtCore.QRect(40, 20, 231, 51))
        self.book.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 229, 255), stop:1 rgba(255, 250, 240, 255));\n"
"    color: #5a5a5a;\n"
"    border: 2px solid #ffb3c5;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 204, 214, 255), stop:1 rgba(255, 243, 230, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 187, 255), stop:1 rgba(255, 233, 214, 255));\n"
"}")
        self.book.setObjectName("book")
        self.readers = QtWidgets.QPushButton(self.centralwidget)
        self.readers.setGeometry(QtCore.QRect(40, 100, 231, 51))
        self.readers.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 229, 255), stop:1 rgba(255, 250, 240, 255));\n"
"    color: #5a5a5a;\n"
"    border: 2px solid #ffb3c5;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 204, 214, 255), stop:1 rgba(255, 243, 230, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 187, 255), stop:1 rgba(255, 233, 214, 255));\n"
"}")
        self.readers.setObjectName("readers")
        self.statistics = QtWidgets.QPushButton(self.centralwidget)
        self.statistics.setGeometry(QtCore.QRect(40, 260, 231, 51))
        self.statistics.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 229, 255), stop:1 rgba(255, 250, 240, 255));\n"
"    color: #5a5a5a;\n"
"    border: 2px solid #ffb3c5;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 204, 214, 255), stop:1 rgba(255, 243, 230, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 187, 255), stop:1 rgba(255, 233, 214, 255));\n"
"}")
        self.statistics.setObjectName("statistics")
        self.extradition = QtWidgets.QPushButton(self.centralwidget)
        self.extradition.setGeometry(QtCore.QRect(40, 180, 231, 51))
        self.extradition.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 229, 255), stop:1 rgba(255, 250, 240, 255));\n"
"    color: #5a5a5a;\n"
"    border: 2px solid #ffb3c5;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 204, 214, 255), stop:1 rgba(255, 243, 230, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 187, 255), stop:1 rgba(255, 233, 214, 255));\n"
"}")
        self.extradition.setObjectName("extradition")
        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(40, 340, 231, 51))
        self.history.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 229, 255), stop:1 rgba(255, 250, 240, 255));\n"
"    color: #5a5a5a;\n"
"    border: 2px solid #ffb3c5;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 204, 214, 255), stop:1 rgba(255, 243, 230, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 187, 255), stop:1 rgba(255, 233, 214, 255));\n"
"}")
        self.history.setObjectName("history")
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 26))
        self.menubar.setObjectName("menubar")
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Меню"))
        self.book.setText(_translate("Menu", "Книги"))
        self.readers.setText(_translate("Menu", "Читатели"))
        self.statistics.setText(_translate("Menu", "Статистика"))
        self.extradition.setText(_translate("Menu", "Выдача"))
        self.history.setText(_translate("Menu", "История выдачи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
