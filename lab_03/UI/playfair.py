# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/playfair.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(110, 210, 631, 31))
        self.txt_key.setObjectName("txt_key")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 61, 16))
        self.label_4.setObjectName("label_4")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(110, 480, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(110, 280, 631, 87))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(110, 100, 631, 87))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(640, 480, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 55, 16))
        self.label_3.setObjectName("label_3")
        self.txt_matrix = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_matrix.setGeometry(QtCore.QRect(110, 380, 631, 87))
        self.txt_matrix.setObjectName("txt_matrix")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(350, 480, 93, 28))
        self.btn_generate.setObjectName("btn_generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Ciphertext:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label.setText(_translate("MainWindow", "PLAYFAIR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plaintext:"))
        self.label_5.setText(_translate("MainWindow", "Matrix:"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_3.setText(_translate("MainWindow", "Key:"))
        self.btn_generate.setText(_translate("MainWindow", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
