# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'six.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1055, 817)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 817)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    border-image: url(:/beijing1/icons/no6.png);\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("border-image: url(:/beijing1/icons/back.png);")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(10, 20))
        self.pushButton.setObjectName("pushButton")
        self.game_id = QtWidgets.QLineEdit(self.centralwidget)
        self.game_id.setGeometry(QtCore.QRect(440, 60, 171, 41))
        self.game_id.setStyleSheet("font: 25 14pt \"微软雅黑 Light\";\n"
"background-color: rgb(255,255,255);")
        self.game_id.setText("")
        self.game_id.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.game_id.setObjectName("game_id")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(640, 60, 111, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt bold \"黑体\";\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("next.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.user_id1 = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id1.setGeometry(QtCore.QRect(110, 260, 101, 41))
        self.user_id1.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt bold \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.user_id1.setText("")
        self.user_id1.setFrame(False)
        self.user_id1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id1.setReadOnly(True)
        self.user_id1.setObjectName("user_id1")
        self.username1 = QtWidgets.QLineEdit(self.centralwidget)
        self.username1.setGeometry(QtCore.QRect(260, 260, 161, 41))
        self.username1.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 10pt bold \"宋体\";\n"
"color: rgb(170, 0, 0);")
        self.username1.setText("")
        self.username1.setFrame(False)
        self.username1.setAlignment(QtCore.Qt.AlignCenter)
        self.username1.setReadOnly(True)
        self.username1.setObjectName("username1")
        self.username2 = QtWidgets.QLineEdit(self.centralwidget)
        self.username2.setGeometry(QtCore.QRect(260, 390, 161, 41))
        self.username2.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 10pt \"方正姚体\";\n"
"color: rgb(170, 0, 0);")
        self.username2.setText("")
        self.username2.setFrame(False)
        self.username2.setAlignment(QtCore.Qt.AlignCenter)
        self.username2.setReadOnly(True)
        self.username2.setObjectName("username2")
        self.username3 = QtWidgets.QLineEdit(self.centralwidget)
        self.username3.setGeometry(QtCore.QRect(260, 520, 161, 41))
        self.username3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 10pt \"方正姚体\";\n"
"color: rgb(170, 0, 0);")
        self.username3.setText("")
        self.username3.setFrame(False)
        self.username3.setAlignment(QtCore.Qt.AlignCenter)
        self.username3.setReadOnly(True)
        self.username3.setObjectName("username3")
        self.username4 = QtWidgets.QLineEdit(self.centralwidget)
        self.username4.setGeometry(QtCore.QRect(260, 650, 161, 41))
        self.username4.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 10pt \"方正姚体\";\n"
"color: rgb(170, 0, 0);")
        self.username4.setText("")
        self.username4.setFrame(False)
        self.username4.setAlignment(QtCore.Qt.AlignCenter)
        self.username4.setReadOnly(True)
        self.username4.setObjectName("username4")
        self.user_id2 = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id2.setGeometry(QtCore.QRect(110, 390, 101, 41))
        self.user_id2.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt bold \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.user_id2.setText("")
        self.user_id2.setFrame(False)
        self.user_id2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id2.setReadOnly(True)
        self.user_id2.setObjectName("user_id2")
        self.user_id3 = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id3.setGeometry(QtCore.QRect(110, 520, 101, 41))
        self.user_id3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt bold \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.user_id3.setText("")
        self.user_id3.setFrame(False)
        self.user_id3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id3.setReadOnly(True)
        self.user_id3.setObjectName("user_id3")
        self.user_id4 = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id4.setGeometry(QtCore.QRect(110, 650, 101, 41))
        self.user_id4.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt bold \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.user_id4.setText("")
        self.user_id4.setFrame(False)
        self.user_id4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id4.setReadOnly(True)
        self.user_id4.setObjectName("user_id4")
        self.score1 = QtWidgets.QLineEdit(self.centralwidget)
        self.score1.setGeometry(QtCore.QRect(460, 260, 91, 41))
        self.score1.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 12pt bold \"宋体\";\n"
"color: rgb(0, 0, 127);")
        self.score1.setText("")
        self.score1.setFrame(False)
        self.score1.setAlignment(QtCore.Qt.AlignCenter)
        self.score1.setReadOnly(True)
        self.score1.setObjectName("score1")
        self.score2 = QtWidgets.QLineEdit(self.centralwidget)
        self.score2.setGeometry(QtCore.QRect(460, 390, 91, 41))
        self.score2.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 12pt bold \"宋体\";\n"
"color: rgb(0, 0, 127);")
        self.score2.setText("")
        self.score2.setFrame(False)
        self.score2.setAlignment(QtCore.Qt.AlignCenter)
        self.score2.setReadOnly(True)
        self.score2.setObjectName("score2")
        self.score3 = QtWidgets.QLineEdit(self.centralwidget)
        self.score3.setGeometry(QtCore.QRect(460, 520, 91, 41))
        self.score3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 12pt bold \"宋体\";\n"
"color: rgb(0, 0, 127);")
        self.score3.setText("")
        self.score3.setFrame(False)
        self.score3.setAlignment(QtCore.Qt.AlignCenter)
        self.score3.setReadOnly(True)
        self.score3.setObjectName("score3")
        self.score4 = QtWidgets.QLineEdit(self.centralwidget)
        self.score4.setGeometry(QtCore.QRect(460, 650, 91, 41))
        self.score4.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 12pt bold \"宋体\";\n"
"color: rgb(0, 0, 127);")
        self.score4.setText("")
        self.score4.setFrame(False)
        self.score4.setAlignment(QtCore.Qt.AlignCenter)
        self.score4.setReadOnly(True)
        self.score4.setObjectName("score4")
        self.cards_type1 = QtWidgets.QTextEdit(self.centralwidget)
        self.cards_type1.setGeometry(QtCore.QRect(620, 210, 301, 111))
        self.cards_type1.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt \"微软雅黑\";")
        self.cards_type1.setReadOnly(True)
        self.cards_type1.setPlaceholderText("")
        self.cards_type1.setObjectName("cards_type1")
        self.cards_type2 = QtWidgets.QTextEdit(self.centralwidget)
        self.cards_type2.setGeometry(QtCore.QRect(620, 340, 301, 111))
        self.cards_type2.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt \"微软雅黑\";")
        self.cards_type2.setReadOnly(True)
        self.cards_type2.setPlaceholderText("")
        self.cards_type2.setObjectName("cards_type2")
        self.cards_type3 = QtWidgets.QTextEdit(self.centralwidget)
        self.cards_type3.setGeometry(QtCore.QRect(620, 460, 301, 111))
        self.cards_type3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt \"微软雅黑\";")
        self.cards_type3.setPlaceholderText("")
        self.cards_type3.setObjectName("cards_type3")
        self.cards_type4 = QtWidgets.QTextEdit(self.centralwidget)
        self.cards_type4.setGeometry(QtCore.QRect(620, 600, 301, 111))
        self.cards_type4.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"font: 14pt \"微软雅黑\";")
        self.cards_type4.setPlaceholderText("")
        self.cards_type4.setObjectName("cards_type4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.slot9)
        self.commandLinkButton.clicked.connect(MainWindow.search_game)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.game_id.setPlaceholderText(_translate("MainWindow", "请输入战局id"))
        self.commandLinkButton.setText(_translate("MainWindow", "查询"))
        self.cards_type1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.cards_type2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.cards_type3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.cards_type4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
import background1_rc
