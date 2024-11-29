from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecordReader(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 445)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.phone = QtWidgets.QTextEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(0, 170, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phone.setFont(font)
        self.phone.setStyleSheet("QTextEdit {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 153, 173, 255), stop:1 rgba(255, 245, 204, 255));\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QTextEdit > QWidget > QWidget {\n"
"    background: transparent;\n"
"}")
        self.phone.setObjectName("phone")
        self.fio = QtWidgets.QTextEdit(self.centralwidget)
        self.fio.setGeometry(QtCore.QRect(0, 50, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fio.setFont(font)
        self.fio.setStyleSheet("QTextEdit {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 153, 173, 255), stop:1 rgba(255, 245, 204, 255));\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QTextEdit > QWidget > QWidget {\n"
"    background: transparent;\n"
"}")
        self.fio.setObjectName("fio")
        self.record_button = QtWidgets.QPushButton(self.centralwidget)
        self.record_button.setGeometry(QtCore.QRect(40, 370, 331, 51))
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
        self.adress = QtWidgets.QTextEdit(self.centralwidget)
        self.adress.setGeometry(QtCore.QRect(0, 290, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adress.setFont(font)
        self.adress.setStyleSheet("QTextEdit {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 153, 173, 255), stop:1 rgba(255, 245, 204, 255));\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QTextEdit > QWidget > QWidget {\n"
"    background: transparent;\n"
"}")
        self.adress.setObjectName("adress")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Запись читателя"))
        self.label.setText(_translate("MainWindow", "ФИО:"))
        self.label_2.setText(_translate("MainWindow", "Телефон:"))
        self.phone.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.fio.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.record_button.setText(_translate("MainWindow", "Записать"))
        self.adress.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Адрес:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RecordReader()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
