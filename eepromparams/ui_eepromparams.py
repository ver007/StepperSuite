# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eepromparams.ui'
#
# Created: Fri Jun 29 22:44:24 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_driveparams(object):
    def setupUi(self, driveparams):
        driveparams.setObjectName("driveparams")
        driveparams.setWindowModality(QtCore.Qt.NonModal)
        driveparams.resize(499, 319)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(driveparams.sizePolicy().hasHeightForWidth())
        driveparams.setSizePolicy(sizePolicy)
        self.label_5 = QtGui.QLabel(driveparams)
        self.label_5.setGeometry(QtCore.QRect(4, 7, 491, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_saveparam = QtGui.QPushButton(driveparams)
        self.pushButton_saveparam.setGeometry(QtCore.QRect(292, 287, 120, 30))
        self.pushButton_saveparam.setStyleSheet("None")
        self.pushButton_saveparam.setObjectName("pushButton_saveparam")
        self.layoutWidget = QtGui.QWidget(driveparams)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 44, 486, 237))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_X = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        self.label_X.setFont(font)
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")
        self.gridLayout.addWidget(self.label_X, 0, 1, 1, 1)
        self.label_Y = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        self.label_Y.setFont(font)
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y.setObjectName("label_Y")
        self.gridLayout.addWidget(self.label_Y, 0, 2, 1, 1)
        self.label_Z = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        self.label_Z.setFont(font)
        self.label_Z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z.setObjectName("label_Z")
        self.gridLayout.addWidget(self.label_Z, 0, 3, 1, 1)
        self.label_accel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_accel.setFont(font)
        self.label_accel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_accel.setObjectName("label_accel")
        self.gridLayout.addWidget(self.label_accel, 1, 0, 1, 1)
        self.label_maxspeed = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_maxspeed.setFont(font)
        self.label_maxspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_maxspeed.setObjectName("label_maxspeed")
        self.gridLayout.addWidget(self.label_maxspeed, 2, 0, 1, 1)
        self.spinBox_drv_para_X_maxspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_maxspeed.setFont(font)
        self.spinBox_drv_para_X_maxspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_maxspeed.setReadOnly(False)
        self.spinBox_drv_para_X_maxspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_maxspeed.setMinimum(1)
        self.spinBox_drv_para_X_maxspeed.setMaximum(999999999)
        self.spinBox_drv_para_X_maxspeed.setProperty("value", 1)
        self.spinBox_drv_para_X_maxspeed.setObjectName("spinBox_drv_para_X_maxspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_maxspeed, 2, 1, 1, 1)
        self.spinBox_drv_para_Y_maxspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_maxspeed.setFont(font)
        self.spinBox_drv_para_Y_maxspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_maxspeed.setReadOnly(False)
        self.spinBox_drv_para_Y_maxspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_maxspeed.setMinimum(1)
        self.spinBox_drv_para_Y_maxspeed.setMaximum(999999999)
        self.spinBox_drv_para_Y_maxspeed.setProperty("value", 1)
        self.spinBox_drv_para_Y_maxspeed.setObjectName("spinBox_drv_para_Y_maxspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_maxspeed, 2, 2, 1, 1)
        self.spinBox_drv_para_Z_maxspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_maxspeed.setFont(font)
        self.spinBox_drv_para_Z_maxspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_maxspeed.setReadOnly(False)
        self.spinBox_drv_para_Z_maxspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_maxspeed.setMinimum(1)
        self.spinBox_drv_para_Z_maxspeed.setMaximum(999999999)
        self.spinBox_drv_para_Z_maxspeed.setProperty("value", 1)
        self.spinBox_drv_para_Z_maxspeed.setObjectName("spinBox_drv_para_Z_maxspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_maxspeed, 2, 3, 1, 1)
        self.label_softendpos = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_softendpos.setFont(font)
        self.label_softendpos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_softendpos.setObjectName("label_softendpos")
        self.gridLayout.addWidget(self.label_softendpos, 3, 0, 1, 1)
        self.spinBox_drv_para_X_softend_pos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_softend_pos.setFont(font)
        self.spinBox_drv_para_X_softend_pos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_softend_pos.setReadOnly(False)
        self.spinBox_drv_para_X_softend_pos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_softend_pos.setMinimum(-999999999)
        self.spinBox_drv_para_X_softend_pos.setMaximum(999999999)
        self.spinBox_drv_para_X_softend_pos.setProperty("value", 0)
        self.spinBox_drv_para_X_softend_pos.setObjectName("spinBox_drv_para_X_softend_pos")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_softend_pos, 3, 1, 1, 1)
        self.spinBox_drv_para_Y_softend_pos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_softend_pos.setFont(font)
        self.spinBox_drv_para_Y_softend_pos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_softend_pos.setReadOnly(False)
        self.spinBox_drv_para_Y_softend_pos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_softend_pos.setMinimum(-999999999)
        self.spinBox_drv_para_Y_softend_pos.setMaximum(999999999)
        self.spinBox_drv_para_Y_softend_pos.setProperty("value", 0)
        self.spinBox_drv_para_Y_softend_pos.setObjectName("spinBox_drv_para_Y_softend_pos")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_softend_pos, 3, 2, 1, 1)
        self.spinBox_drv_para_Z_softend_pos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_softend_pos.setFont(font)
        self.spinBox_drv_para_Z_softend_pos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_softend_pos.setReadOnly(False)
        self.spinBox_drv_para_Z_softend_pos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_softend_pos.setMinimum(-999999999)
        self.spinBox_drv_para_Z_softend_pos.setMaximum(999999999)
        self.spinBox_drv_para_Z_softend_pos.setProperty("value", 0)
        self.spinBox_drv_para_Z_softend_pos.setObjectName("spinBox_drv_para_Z_softend_pos")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_softend_pos, 3, 3, 1, 1)
        self.label_softendneg = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_softendneg.setFont(font)
        self.label_softendneg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_softendneg.setObjectName("label_softendneg")
        self.gridLayout.addWidget(self.label_softendneg, 4, 0, 1, 1)
        self.spinBox_drv_para_X_softend_neg = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_softend_neg.setFont(font)
        self.spinBox_drv_para_X_softend_neg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_softend_neg.setReadOnly(False)
        self.spinBox_drv_para_X_softend_neg.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_softend_neg.setMinimum(-999999999)
        self.spinBox_drv_para_X_softend_neg.setMaximum(999999999)
        self.spinBox_drv_para_X_softend_neg.setProperty("value", 0)
        self.spinBox_drv_para_X_softend_neg.setObjectName("spinBox_drv_para_X_softend_neg")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_softend_neg, 4, 1, 1, 1)
        self.spinBox_drv_para_Y_softend_neg = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_softend_neg.setFont(font)
        self.spinBox_drv_para_Y_softend_neg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_softend_neg.setReadOnly(False)
        self.spinBox_drv_para_Y_softend_neg.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_softend_neg.setMinimum(-999999999)
        self.spinBox_drv_para_Y_softend_neg.setMaximum(999999999)
        self.spinBox_drv_para_Y_softend_neg.setProperty("value", 0)
        self.spinBox_drv_para_Y_softend_neg.setObjectName("spinBox_drv_para_Y_softend_neg")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_softend_neg, 4, 2, 1, 1)
        self.spinBox_drv_para_Z_softend_neg = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_softend_neg.setFont(font)
        self.spinBox_drv_para_Z_softend_neg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_softend_neg.setReadOnly(False)
        self.spinBox_drv_para_Z_softend_neg.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_softend_neg.setMinimum(-999999999)
        self.spinBox_drv_para_Z_softend_neg.setMaximum(999999999)
        self.spinBox_drv_para_Z_softend_neg.setProperty("value", 0)
        self.spinBox_drv_para_Z_softend_neg.setObjectName("spinBox_drv_para_Z_softend_neg")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_softend_neg, 4, 3, 1, 1)
        self.label_refp = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_refp.setFont(font)
        self.label_refp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_refp.setObjectName("label_refp")
        self.gridLayout.addWidget(self.label_refp, 5, 0, 1, 1)
        self.spinBox_drv_para_X_refpos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_refpos.setFont(font)
        self.spinBox_drv_para_X_refpos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_refpos.setReadOnly(False)
        self.spinBox_drv_para_X_refpos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_refpos.setMinimum(-999999999)
        self.spinBox_drv_para_X_refpos.setMaximum(999999999)
        self.spinBox_drv_para_X_refpos.setProperty("value", 0)
        self.spinBox_drv_para_X_refpos.setObjectName("spinBox_drv_para_X_refpos")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_refpos, 5, 1, 1, 1)
        self.spinBox_drv_para_Y_refpos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_refpos.setFont(font)
        self.spinBox_drv_para_Y_refpos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_refpos.setReadOnly(False)
        self.spinBox_drv_para_Y_refpos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_refpos.setMinimum(-999999999)
        self.spinBox_drv_para_Y_refpos.setMaximum(999999999)
        self.spinBox_drv_para_Y_refpos.setProperty("value", 0)
        self.spinBox_drv_para_Y_refpos.setObjectName("spinBox_drv_para_Y_refpos")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_refpos, 5, 2, 1, 1)
        self.spinBox_drv_para_Z_refpos = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_refpos.setFont(font)
        self.spinBox_drv_para_Z_refpos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_refpos.setReadOnly(False)
        self.spinBox_drv_para_Z_refpos.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_refpos.setMinimum(-999999999)
        self.spinBox_drv_para_Z_refpos.setMaximum(999999999)
        self.spinBox_drv_para_Z_refpos.setProperty("value", 0)
        self.spinBox_drv_para_Z_refpos.setObjectName("spinBox_drv_para_Z_refpos")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_refpos, 5, 3, 1, 1)
        self.label_refspeed = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_refspeed.setFont(font)
        self.label_refspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_refspeed.setObjectName("label_refspeed")
        self.gridLayout.addWidget(self.label_refspeed, 6, 0, 1, 1)
        self.spinBox_drv_para_X_refspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_refspeed.setFont(font)
        self.spinBox_drv_para_X_refspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_refspeed.setReadOnly(False)
        self.spinBox_drv_para_X_refspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_refspeed.setMinimum(-999999999)
        self.spinBox_drv_para_X_refspeed.setMaximum(999999999)
        self.spinBox_drv_para_X_refspeed.setProperty("value", 0)
        self.spinBox_drv_para_X_refspeed.setObjectName("spinBox_drv_para_X_refspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_refspeed, 6, 1, 1, 1)
        self.spinBox_drv_para_Y_refspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_refspeed.setFont(font)
        self.spinBox_drv_para_Y_refspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_refspeed.setReadOnly(False)
        self.spinBox_drv_para_Y_refspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_refspeed.setMinimum(-999999999)
        self.spinBox_drv_para_Y_refspeed.setMaximum(999999999)
        self.spinBox_drv_para_Y_refspeed.setProperty("value", 0)
        self.spinBox_drv_para_Y_refspeed.setObjectName("spinBox_drv_para_Y_refspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_refspeed, 6, 2, 1, 1)
        self.spinBox_drv_para_Z_refspeed = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_refspeed.setFont(font)
        self.spinBox_drv_para_Z_refspeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_refspeed.setReadOnly(False)
        self.spinBox_drv_para_Z_refspeed.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_refspeed.setMinimum(-999999999)
        self.spinBox_drv_para_Z_refspeed.setMaximum(999999999)
        self.spinBox_drv_para_Z_refspeed.setProperty("value", 0)
        self.spinBox_drv_para_Z_refspeed.setObjectName("spinBox_drv_para_Z_refspeed")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_refspeed, 6, 3, 1, 1)
        self.label_poscor = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(8)
        self.label_poscor.setFont(font)
        self.label_poscor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_poscor.setObjectName("label_poscor")
        self.gridLayout.addWidget(self.label_poscor, 7, 0, 1, 1)
        self.spinBox_drv_para_X_poscor = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_X_poscor.setFont(font)
        self.spinBox_drv_para_X_poscor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_X_poscor.setReadOnly(False)
        self.spinBox_drv_para_X_poscor.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_X_poscor.setMinimum(-999999999)
        self.spinBox_drv_para_X_poscor.setMaximum(999999999)
        self.spinBox_drv_para_X_poscor.setProperty("value", 0)
        self.spinBox_drv_para_X_poscor.setObjectName("spinBox_drv_para_X_poscor")
        self.gridLayout.addWidget(self.spinBox_drv_para_X_poscor, 7, 1, 1, 1)
        self.spinBox_drv_para_Y_poscor = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.spinBox_drv_para_Y_poscor.setFont(font)
        self.spinBox_drv_para_Y_poscor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Y_poscor.setReadOnly(False)
        self.spinBox_drv_para_Y_poscor.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Y_poscor.setMinimum(-999999999)
        self.spinBox_drv_para_Y_poscor.setMaximum(999999999)
        self.spinBox_drv_para_Y_poscor.setProperty("value", 0)
        self.spinBox_drv_para_Y_poscor.setObjectName("spinBox_drv_para_Y_poscor")
        self.gridLayout.addWidget(self.spinBox_drv_para_Y_poscor, 7, 2, 1, 1)
        self.spinBox_drv_para_Z_poscor = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.spinBox_drv_para_Z_poscor.setFont(font)
        self.spinBox_drv_para_Z_poscor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_drv_para_Z_poscor.setReadOnly(False)
        self.spinBox_drv_para_Z_poscor.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_drv_para_Z_poscor.setMinimum(-999999999)
        self.spinBox_drv_para_Z_poscor.setMaximum(999999999)
        self.spinBox_drv_para_Z_poscor.setProperty("value", 0)
        self.spinBox_drv_para_Z_poscor.setObjectName("spinBox_drv_para_Z_poscor")
        self.gridLayout.addWidget(self.spinBox_drv_para_Z_poscor, 7, 3, 1, 1)
        self.doubleSpinBox_drv_para_X_accel = QtGui.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.doubleSpinBox_drv_para_X_accel.setFont(font)
        self.doubleSpinBox_drv_para_X_accel.setMaximum(100000.0)
        self.doubleSpinBox_drv_para_X_accel.setObjectName("doubleSpinBox_drv_para_X_accel")
        self.gridLayout.addWidget(self.doubleSpinBox_drv_para_X_accel, 1, 1, 1, 1)
        self.doubleSpinBox_drv_para_Y_accel = QtGui.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.doubleSpinBox_drv_para_Y_accel.setFont(font)
        self.doubleSpinBox_drv_para_Y_accel.setMaximum(100000.0)
        self.doubleSpinBox_drv_para_Y_accel.setObjectName("doubleSpinBox_drv_para_Y_accel")
        self.gridLayout.addWidget(self.doubleSpinBox_drv_para_Y_accel, 1, 2, 1, 1)
        self.doubleSpinBox_drv_para_Z_accel = QtGui.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.doubleSpinBox_drv_para_Z_accel.setFont(font)
        self.doubleSpinBox_drv_para_Z_accel.setMaximum(100000.0)
        self.doubleSpinBox_drv_para_Z_accel.setSingleStep(10.0)
        self.doubleSpinBox_drv_para_Z_accel.setObjectName("doubleSpinBox_drv_para_Z_accel")
        self.gridLayout.addWidget(self.doubleSpinBox_drv_para_Z_accel, 1, 3, 1, 1)
        self.pushButton_loadparam = QtGui.QPushButton(driveparams)
        self.pushButton_loadparam.setGeometry(QtCore.QRect(158, 287, 130, 30))
        self.pushButton_loadparam.setObjectName("pushButton_loadparam")
        self.buttonBox = QtGui.QDialogButtonBox(driveparams)
        self.buttonBox.setGeometry(QtCore.QRect(414, 287, 81, 30))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(driveparams)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("clicked(QAbstractButton*)"), driveparams.close)
        QtCore.QMetaObject.connectSlotsByName(driveparams)
        driveparams.setTabOrder(self.spinBox_drv_para_X_maxspeed, self.spinBox_drv_para_X_softend_pos)
        driveparams.setTabOrder(self.spinBox_drv_para_X_softend_pos, self.spinBox_drv_para_X_softend_neg)
        driveparams.setTabOrder(self.spinBox_drv_para_X_softend_neg, self.spinBox_drv_para_X_refpos)
        driveparams.setTabOrder(self.spinBox_drv_para_X_refpos, self.spinBox_drv_para_X_refspeed)
        driveparams.setTabOrder(self.spinBox_drv_para_X_refspeed, self.spinBox_drv_para_X_poscor)
        driveparams.setTabOrder(self.spinBox_drv_para_X_poscor, self.spinBox_drv_para_Y_maxspeed)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_maxspeed, self.spinBox_drv_para_Y_softend_pos)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_softend_pos, self.spinBox_drv_para_Y_softend_neg)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_softend_neg, self.spinBox_drv_para_Y_refpos)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_refpos, self.spinBox_drv_para_Y_refspeed)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_refspeed, self.spinBox_drv_para_Y_poscor)
        driveparams.setTabOrder(self.spinBox_drv_para_Y_poscor, self.spinBox_drv_para_Z_maxspeed)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_maxspeed, self.spinBox_drv_para_Z_softend_pos)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_softend_pos, self.spinBox_drv_para_Z_softend_neg)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_softend_neg, self.spinBox_drv_para_Z_refpos)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_refpos, self.spinBox_drv_para_Z_refspeed)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_refspeed, self.spinBox_drv_para_Z_poscor)
        driveparams.setTabOrder(self.spinBox_drv_para_Z_poscor, self.pushButton_loadparam)
        driveparams.setTabOrder(self.pushButton_loadparam, self.pushButton_saveparam)

    def retranslateUi(self, driveparams):
        driveparams.setWindowTitle(QtGui.QApplication.translate("driveparams", "Drive Parameter Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("driveparams", "controller eeprom parameter setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_saveparam.setText(QtGui.QApplication.translate("driveparams", "&Save to Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.label_X.setText(QtGui.QApplication.translate("driveparams", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Y.setText(QtGui.QApplication.translate("driveparams", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Z.setText(QtGui.QApplication.translate("driveparams", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_accel.setText(QtGui.QApplication.translate("driveparams", "acceleration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_maxspeed.setText(QtGui.QApplication.translate("driveparams", "maximum speed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_softendpos.setText(QtGui.QApplication.translate("driveparams", "softend positiv", None, QtGui.QApplication.UnicodeUTF8))
        self.label_softendneg.setText(QtGui.QApplication.translate("driveparams", "softend negativ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_refp.setText(QtGui.QApplication.translate("driveparams", "reference pos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_refspeed.setText(QtGui.QApplication.translate("driveparams", "reference speed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_poscor.setText(QtGui.QApplication.translate("driveparams", "pos correction", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_loadparam.setText(QtGui.QApplication.translate("driveparams", "&Load from Controller", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    driveparams = QtGui.QWidget()
    ui = Ui_driveparams()
    ui.setupUi(driveparams)
    driveparams.show()
    sys.exit(app.exec_())
