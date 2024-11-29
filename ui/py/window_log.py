
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor

class Ui_window_logs(object):
    def setupUi(self, window_logs):
        window_logs.setObjectName("window_logs")
        window_logs.resize(452, 319)
        window_logs.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 183, 197, 255), stop:1 rgba(255, 255, 204, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(window_logs)
        self.centralwidget.setObjectName("centralwidget")
        self.text_log = QtWidgets.QTextEdit(self.centralwidget)
        self.text_log.setEnabled(False)
        self.text_log.setGeometry(QtCore.QRect(10, 10, 431, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_log.setFont(font)
        self.text_log.setStyleSheet("QTextEdit {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 153, 173, 255), stop:1 rgba(255, 245, 204, 255));\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QTextEdit > QWidget > QWidget {\n"
"    background: transparent;\n"
"}")
        self.text_log.setObjectName("text_log")
        self.text_log.setTextColor(QColor(0, 0, 0))
        window_logs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_logs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))
        self.menubar.setObjectName("menubar")
        window_logs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_logs)
        self.statusbar.setObjectName("statusbar")
        window_logs.setStatusBar(self.statusbar)

        self.retranslateUi(window_logs)
        QtCore.QMetaObject.connectSlotsByName(window_logs)

    def retranslateUi(self, window_logs):
        _translate = QtCore.QCoreApplication.translate
        window_logs.setWindowTitle(_translate("window_logs", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_logs = QtWidgets.QMainWindow()
    ui = Ui_window_logs()
    ui.setupUi(window_logs)
    window_logs.show()
    sys.exit(app.exec_())
