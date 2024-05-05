# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnaEkran(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -21, 851, 611))
        self.widget.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.widget.setObjectName("widget")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(200, 40, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 20px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(110, 250, 141, 31))
        self.label_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(280, 130, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_okuma = QtWidgets.QLabel(self.widget)
        self.label_okuma.setGeometry(QtCore.QRect(550, 120, 271, 151))
        self.label_okuma.setStyleSheet("border: 2px solid #000000;")
        self.label_okuma.setText("")
        self.label_okuma.setObjectName("label_okuma")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.lineEdit_tansiyonB = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_tansiyonB.setGeometry(QtCore.QRect(280, 170, 191, 31))
        self.lineEdit_tansiyonB.setObjectName("lineEdit_tansiyonB")
        self.lineEdit_tansiyonK = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_tansiyonK.setGeometry(QtCore.QRect(280, 210, 191, 31))
        self.lineEdit_tansiyonK.setObjectName("lineEdit_tansiyonK")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 141, 31))
        self.label_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(110, 170, 141, 31))
        self.label_4.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_kansekeri = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_kansekeri.setGeometry(QtCore.QRect(280, 250, 191, 31))
        self.lineEdit_kansekeri.setObjectName("lineEdit_kansekeri")
        self.pushButton_kaydet = QtWidgets.QPushButton(self.widget)
        self.pushButton_kaydet.setGeometry(QtCore.QRect(200, 330, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kaydet.setFont(font)
        self.pushButton_kaydet.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.pushButton_rapor = QtWidgets.QPushButton(self.widget)
        self.pushButton_rapor.setGeometry(QtCore.QRect(60, 460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rapor.setFont(font)
        self.pushButton_rapor.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.pushButton_rapor.setObjectName("pushButton_rapor")
        self.pushButton_egzersiz = QtWidgets.QPushButton(self.widget)
        self.pushButton_egzersiz.setGeometry(QtCore.QRect(540, 460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_egzersiz.setFont(font)
        self.pushButton_egzersiz.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.pushButton_egzersiz.setObjectName("pushButton_egzersiz")
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
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">i - NABIZ </span></p><p><span style=\" font-size:10pt;\">Kişisel Sağlık Sistemi</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Kan Şekeri           :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "100-160"))
        self.comboBox.setItemText(1, _translate("MainWindow", "70-120"))
        self.comboBox.setItemText(2, _translate("MainWindow", "60-100"))
        self.comboBox.setItemText(3, _translate("MainWindow", "40-60"))
        self.label.setText(_translate("MainWindow", "Nabız                  :"))
        self.lineEdit_tansiyonB.setPlaceholderText(_translate("MainWindow", "Lütfen mmHg cinsinden giriniz."))
        self.lineEdit_tansiyonK.setPlaceholderText(_translate("MainWindow", "Lütfen mmHg cinsinden giriniz."))
        self.label_2.setText(_translate("MainWindow", "Tansiyon (Küçük)  :"))
        self.label_4.setText(_translate("MainWindow", "Tansiyon (Büyük)  :"))
        self.lineEdit_kansekeri.setPlaceholderText(_translate("MainWindow", "Lütfen mg/dl cinsinden giriniz."))
        self.pushButton_kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.pushButton_rapor.setText(_translate("MainWindow", "Rapor Almak İçin Tıklayınız"))
        self.pushButton_egzersiz.setText(_translate("MainWindow", "Egzersiz Sayfasına Gitmek İçin Tıklayınız"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AnaEkran()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
