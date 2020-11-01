# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cacheFiles.ui',
# licensing of 'cacheFiles.ui' applies.
#
# Created: Wed Aug 28 14:32:28 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!


try:
    from PySide import QtGui, QtGui as QtWidgets,  QtCore
    unicodeUTF = QtWidgets.QApplication.UnicodeUTF8
except:
    from PySide2 import QtWidgets, QtCore, QtGui
    unicodeUTF = -1

class Ui_CacheFiles(object):
    def setupUi(self, CacheFiles):
        CacheFiles.setObjectName("CacheFiles")
        CacheFiles.resize(644, 350)
        CacheFiles.setMaximumSize(644,350)
        self.pushButton_images = QtWidgets.QPushButton(CacheFiles)
        self.pushButton_images.setGeometry(QtCore.QRect(184, 10, 111, 23))
        self.pushButton_images.setObjectName("pushButton_images")
        self.pushButton_imgSeq = QtWidgets.QPushButton(CacheFiles)
        self.pushButton_imgSeq.setGeometry(QtCore.QRect(74, 10, 111, 23))
        self.pushButton_imgSeq.setObjectName("pushButton_imgSeq")
        self.pushButton_images.setCheckable(True)
        self.pushButton_imgSeq.setCheckable(True)
        self.lineEdit_source = QtWidgets.QLineEdit(CacheFiles)
        self.lineEdit_source.setGeometry(QtCore.QRect(100, 91, 531, 20))
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.lineEdit_destination = QtWidgets.QLineEdit(CacheFiles)
        self.lineEdit_destination.setGeometry(QtCore.QRect(100, 117, 531, 20))
        self.lineEdit_destination.setObjectName("lineEdit_destination")
        self.pushButton_startCache = QtWidgets.QPushButton(CacheFiles)
        self.pushButton_startCache.setGeometry(QtCore.QRect(478, 10, 81, 23))
        self.pushButton_startCache.setObjectName("pushButton_startCache")
        self.pushButton_cancel = QtWidgets.QPushButton(CacheFiles)
        self.pushButton_cancel.setGeometry(QtCore.QRect(560, 10, 71, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_2 = QtWidgets.QLabel(CacheFiles)
        self.label_2.setGeometry(QtCore.QRect(49, 92, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CacheFiles)
        self.label_3.setGeometry(QtCore.QRect(27, 115, 61, 16))
        self.label_3.setObjectName("label_3")
        self.gridWidget = QtWidgets.QWidget(CacheFiles)
        self.gridWidget.setGeometry(QtCore.QRect(10, 160, 621, 180))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.retranslateUi(CacheFiles)
        QtCore.QMetaObject.connectSlotsByName(CacheFiles)

    def retranslateUi(self, CacheFiles):
        CacheFiles.setWindowTitle(QtWidgets.QApplication.translate("CacheFiles", "Cache Files", None, unicodeUTF))
        self.pushButton_images.setText(QtWidgets.QApplication.translate("CacheFiles", "Imgs/Movie", None, unicodeUTF))
        self.pushButton_imgSeq.setText(QtWidgets.QApplication.translate("CacheFiles", "Image Seq", None, unicodeUTF))
        self.pushButton_startCache.setText(QtWidgets.QApplication.translate("CacheFiles", "Start Cache", None, unicodeUTF))
        self.pushButton_cancel.setText(QtWidgets.QApplication.translate("CacheFiles", "Cancel", None, unicodeUTF))
        self.label_2.setText(QtWidgets.QApplication.translate("CacheFiles", "Source", None, unicodeUTF))
        self.label_3.setText(QtWidgets.QApplication.translate("CacheFiles", "Destination", None, unicodeUTF))

