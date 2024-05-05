# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 559)
        Form.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 351, 461))
        self.label.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_Kadi = QtWidgets.QLineEdit(Form)
        self.lineEdit_Kadi.setGeometry(QtCore.QRect(90, 160, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Kadi.setFont(font)
        self.lineEdit_Kadi.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_Kadi.setText("")
        self.lineEdit_Kadi.setObjectName("lineEdit_Kadi")
        self.lineEdit_Sifre = QtWidgets.QLineEdit(Form)
        self.lineEdit_Sifre.setGeometry(QtCore.QRect(90, 260, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Sifre.setFont(font)
        self.lineEdit_Sifre.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_Sifre.setText("")
        self.lineEdit_Sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Sifre.setObjectName("lineEdit_Sifre")
        self.pushButton_Kayit = QtWidgets.QPushButton(Form)
        self.pushButton_Kayit.setGeometry(QtCore.QRect(110, 370, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Kayit.setFont(font)
        self.pushButton_Kayit.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_Kayit.setObjectName("pushButton_Kayit")
        self.pushButton_iptal = QtWidgets.QPushButton(Form)
        self.pushButton_iptal.setGeometry(QtCore.QRect(150, 420, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_iptal.setFont(font)
        self.pushButton_iptal.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_iptal.setObjectName("pushButton_iptal")
        self.label_catflix = QtWidgets.QLabel(Form)
        self.label_catflix.setGeometry(QtCore.QRect(90, 60, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_catflix.setFont(font)
        self.label_catflix.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_catflix.setAlignment(QtCore.Qt.AlignCenter)
        self.label_catflix.setObjectName("label_catflix")
        self.label_kayit = QtWidgets.QLabel(Form)
        self.label_kayit.setGeometry(QtCore.QRect(80, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_kayit.setFont(font)
        self.label_kayit.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.label_kayit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kayit.setObjectName("label_kayit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_Kadi.setPlaceholderText(_translate("Form", "Kullanıcı Adı"))
        self.lineEdit_Sifre.setPlaceholderText(_translate("Form", "Şifre"))
        self.pushButton_Kayit.setText(_translate("Form", "Kayıt Ol"))
        self.pushButton_iptal.setText(_translate("Form", "İptal"))
        self.label_catflix.setText(_translate("Form", "CATFLIX"))
        self.label_kayit.setText(_translate("Form", "Kayıt Ol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())