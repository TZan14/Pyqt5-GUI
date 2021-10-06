# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Counter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Counter(object):
    def setupUi(self, Counter):
        Counter.setObjectName("Counter")
        Counter.resize(400, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Counter.sizePolicy().hasHeightForWidth())
        Counter.setSizePolicy(sizePolicy)
        Counter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayoutWidget = QtWidgets.QWidget(Counter)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd.sizePolicy().hasHeightForWidth())
        self.lcd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.lcd.setFont(font)
        self.lcd.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd.setStyleSheet("QLCDNumber{\n"
"    background: #f3f6f4;\n"
"    border-radius: 80%;\n"
"}")
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd.setObjectName("lcd")
        self.verticalLayout.addWidget(self.lcd)
        self.gridLayoutWidget = QtWidgets.QWidget(Counter)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 120, 401, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.decrease = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.decrease.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.decrease.setFont(font)
        self.decrease.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  color: #990000;\n"
"  width: 120px;\n"
"  height: 120px;\n"
"  line-height: 120px;\n"
"  border-radius: 50%;\n"
"  border: solid 2px #ffffff;\n"
"  text-align: center;\n"
"  vertical-align: middle;\n"
"  overflow: hidden;\n"
"  font-weight: bold;\n"
"  transition: .4s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #ea9999;\n"
"}")
        self.decrease.setObjectName("decrease")
        self.gridLayout.addWidget(self.decrease, 0, 1, 1, 1)
        self.increase = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.increase.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.increase.setFont(font)
        self.increase.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  color: #668ad8;\n"
"  width: 120px;\n"
"  height: 120px;\n"
"  line-height: 120px;\n"
"  border-radius: 50%;\n"
"  border: solid 2px #668ad8;\n"
"  text-align: center;\n"
"  vertical-align: middle;\n"
"  overflow: hidden;\n"
"  font-weight: bold;\n"
"  transition: .4s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #b3e1ff;\n"
"}")
        self.increase.setObjectName("increase")
        self.gridLayout.addWidget(self.increase, 0, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  color: #ef2718;\n"
"  width: 120px;\n"
"  height: 120px;\n"
"  line-height: 120px;\n"
"  border-radius: 50%;\n"
"  border: solid 2px #ffffff;\n"
"  text-align: center;\n"
"  vertical-align: middle;\n"
"  overflow: hidden;\n"
"  font-weight: bold;\n"
"  transition: .4s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f4cccc;\n"
"}")
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Counter)
        self.label.setGeometry(QtCore.QRect(170, 290, 231, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Counter)
        self.label_2.setGeometry(QtCore.QRect(110, 260, 191, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Counter)
        QtCore.QMetaObject.connectSlotsByName(Counter)

    def retranslateUi(self, Counter):
        _translate = QtCore.QCoreApplication.translate
        Counter.setWindowTitle(_translate("Counter", "Tally Counter"))
        self.decrease.setText(_translate("Counter", "Decrease"))
        self.increase.setText(_translate("Counter", "Increase"))
        self.exit.setText(_translate("Counter", "Exit"))
        self.label.setText(_translate("Counter", "Tally Counter Version 1.2 by T Zan"))
        self.label_2.setText(_translate("Counter", "Date Time"))