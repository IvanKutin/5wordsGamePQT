# Form implementation generated from reading ui file 'second_player_field.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 871))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setMouseTracking(False)
        self.frame.setStyleSheet("background-color: #e0e0e0;border-radius: 10px ;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(100, 40, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#fff000")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(170, 40, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#fff000")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(310, 40, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#fff000")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(240, 40, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:#fff000")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#fff000;")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.Play = QtWidgets.QPushButton(self.frame)
        self.Play.setEnabled(False)
        self.Play.setGeometry(QtCore.QRect(580, 380, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Play.setFont(font)
        self.Play.setStyleSheet("background-color: #e3dede; border-radius: 20px ;background-color : #99e2f2")
        self.Play.setObjectName("Play")
        self.s2 = QtWidgets.QLabel(self.frame)
        self.s2.setGeometry(QtCore.QRect(210, 170, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s2.setFont(font)
        self.s2.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s2.setText("")
        self.s2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s2.setObjectName("s2")
        self.s7 = QtWidgets.QLabel(self.frame)
        self.s7.setGeometry(QtCore.QRect(210, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s7.setFont(font)
        self.s7.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s7.setText("")
        self.s7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s7.setObjectName("s7")
        self.s12 = QtWidgets.QLabel(self.frame)
        self.s12.setGeometry(QtCore.QRect(210, 370, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s12.setFont(font)
        self.s12.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s12.setText("")
        self.s12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s12.setObjectName("s12")
        self.s17 = QtWidgets.QLabel(self.frame)
        self.s17.setGeometry(QtCore.QRect(210, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s17.setFont(font)
        self.s17.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s17.setText("")
        self.s17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s17.setObjectName("s17")
        self.s22 = QtWidgets.QLabel(self.frame)
        self.s22.setGeometry(QtCore.QRect(210, 570, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s22.setFont(font)
        self.s22.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s22.setText("")
        self.s22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s22.setObjectName("s22")
        self.s27 = QtWidgets.QLabel(self.frame)
        self.s27.setGeometry(QtCore.QRect(210, 660, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s27.setFont(font)
        self.s27.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s27.setText("")
        self.s27.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s27.setObjectName("s27")
        self.s1 = QtWidgets.QLabel(self.frame)
        self.s1.setGeometry(QtCore.QRect(130, 170, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s1.setFont(font)
        self.s1.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s1.setText("")
        self.s1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s1.setObjectName("s1")
        self.s3 = QtWidgets.QLabel(self.frame)
        self.s3.setGeometry(QtCore.QRect(290, 170, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s3.setFont(font)
        self.s3.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s3.setText("")
        self.s3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s3.setObjectName("s3")
        self.s8 = QtWidgets.QLabel(self.frame)
        self.s8.setEnabled(True)
        self.s8.setGeometry(QtCore.QRect(290, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s8.setFont(font)
        self.s8.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s8.setText("")
        self.s8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s8.setObjectName("s8")
        self.s13 = QtWidgets.QLabel(self.frame)
        self.s13.setGeometry(QtCore.QRect(290, 370, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s13.setFont(font)
        self.s13.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s13.setText("")
        self.s13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s13.setObjectName("s13")
        self.s18 = QtWidgets.QLabel(self.frame)
        self.s18.setGeometry(QtCore.QRect(290, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s18.setFont(font)
        self.s18.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s18.setText("")
        self.s18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s18.setObjectName("s18")
        self.s23 = QtWidgets.QLabel(self.frame)
        self.s23.setGeometry(QtCore.QRect(290, 570, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s23.setFont(font)
        self.s23.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s23.setText("")
        self.s23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s23.setObjectName("s23")
        self.s28 = QtWidgets.QLabel(self.frame)
        self.s28.setGeometry(QtCore.QRect(290, 660, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s28.setFont(font)
        self.s28.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s28.setText("")
        self.s28.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s28.setObjectName("s28")
        self.s4 = QtWidgets.QLabel(self.frame)
        self.s4.setGeometry(QtCore.QRect(370, 170, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s4.setFont(font)
        self.s4.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s4.setText("")
        self.s4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s4.setObjectName("s4")
        self.s9 = QtWidgets.QLabel(self.frame)
        self.s9.setGeometry(QtCore.QRect(370, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s9.setFont(font)
        self.s9.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s9.setText("")
        self.s9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s9.setObjectName("s9")
        self.s14 = QtWidgets.QLabel(self.frame)
        self.s14.setGeometry(QtCore.QRect(370, 370, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s14.setFont(font)
        self.s14.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s14.setText("")
        self.s14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s14.setObjectName("s14")
        self.s5 = QtWidgets.QLabel(self.frame)
        self.s5.setGeometry(QtCore.QRect(450, 170, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s5.setFont(font)
        self.s5.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s5.setText("")
        self.s5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s5.setObjectName("s5")
        self.s10 = QtWidgets.QLabel(self.frame)
        self.s10.setGeometry(QtCore.QRect(450, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s10.setFont(font)
        self.s10.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s10.setText("")
        self.s10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s10.setObjectName("s10")
        self.s19 = QtWidgets.QLabel(self.frame)
        self.s19.setGeometry(QtCore.QRect(370, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s19.setFont(font)
        self.s19.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s19.setText("")
        self.s19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s19.setObjectName("s19")
        self.s24 = QtWidgets.QLabel(self.frame)
        self.s24.setGeometry(QtCore.QRect(370, 570, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s24.setFont(font)
        self.s24.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s24.setText("")
        self.s24.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s24.setObjectName("s24")
        self.s29 = QtWidgets.QLabel(self.frame)
        self.s29.setGeometry(QtCore.QRect(370, 660, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s29.setFont(font)
        self.s29.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s29.setText("")
        self.s29.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s29.setObjectName("s29")
        self.s15 = QtWidgets.QLabel(self.frame)
        self.s15.setGeometry(QtCore.QRect(450, 370, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s15.setFont(font)
        self.s15.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s15.setText("")
        self.s15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s15.setObjectName("s15")
        self.s6 = QtWidgets.QLabel(self.frame)
        self.s6.setGeometry(QtCore.QRect(130, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s6.setFont(font)
        self.s6.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s6.setText("")
        self.s6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s6.setObjectName("s6")
        self.s11 = QtWidgets.QLabel(self.frame)
        self.s11.setGeometry(QtCore.QRect(130, 370, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s11.setFont(font)
        self.s11.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s11.setText("")
        self.s11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s11.setObjectName("s11")
        self.s16 = QtWidgets.QLabel(self.frame)
        self.s16.setGeometry(QtCore.QRect(130, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s16.setFont(font)
        self.s16.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s16.setText("")
        self.s16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s16.setObjectName("s16")
        self.s20 = QtWidgets.QLabel(self.frame)
        self.s20.setGeometry(QtCore.QRect(450, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s20.setFont(font)
        self.s20.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s20.setText("")
        self.s20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s20.setObjectName("s20")
        self.s25 = QtWidgets.QLabel(self.frame)
        self.s25.setGeometry(QtCore.QRect(450, 570, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s25.setFont(font)
        self.s25.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s25.setText("")
        self.s25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s25.setObjectName("s25")
        self.s30 = QtWidgets.QLabel(self.frame)
        self.s30.setGeometry(QtCore.QRect(450, 660, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s30.setFont(font)
        self.s30.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s30.setText("")
        self.s30.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s30.setObjectName("s30")
        self.s21 = QtWidgets.QLabel(self.frame)
        self.s21.setGeometry(QtCore.QRect(130, 570, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s21.setFont(font)
        self.s21.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s21.setText("")
        self.s21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s21.setObjectName("s21")
        self.s26 = QtWidgets.QLabel(self.frame)
        self.s26.setGeometry(QtCore.QRect(130, 660, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.s26.setFont(font)
        self.s26.setStyleSheet("border: 1px solid;background-color:#fff")
        self.s26.setText("")
        self.s26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.s26.setObjectName("s26")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(520, 10, 371, 111))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mistake = QtWidgets.QLabel(self.frame)
        self.mistake.setGeometry(QtCore.QRect(540, 180, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        self.mistake.setFont(font)
        self.mistake.setText("")
        self.mistake.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mistake.setObjectName("mistake")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "5 ????????"))
        self.label_5.setText(_translate("MainWindow", "??"))
        self.label_6.setText(_translate("MainWindow", "??"))
        self.label_8.setText(_translate("MainWindow", "??"))
        self.label_9.setText(_translate("MainWindow", "??"))
        self.label_10.setText(_translate("MainWindow", "5"))
        self.Play.setText(_translate("MainWindow", "??????????????????\n"
" ??????????"))
        self.label.setText(_translate("MainWindow", "??????????, ???????? ?????????? ??????????\n"
"     ?????????????????? ??????????"))
