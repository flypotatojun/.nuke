try:
    from PySide import QtGui as QtWidgets, QtGui, QtCore
    unicodeUTF = QtWidgets.QApplication.UnicodeUTF8
except:
    from PySide2 import QtWidgets, QtCore, QtGui
    unicodeUTF = -1

import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 610)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 151, 390))
        self.myCustomLabel = QtWidgets.QLabel(self)
        self.myCustomLabel.setGeometry(QtCore.QRect(10,470, 151, 30))
        self.myCustomLabel.setText('My Collections')
        self.listWidget2 = QtWidgets.QListWidget(Form)
        self.listWidget2.setGeometry(QtCore.QRect(10, 400, 151, 200))
        self.myCustomLabel.setStyleSheet('''
            QLabel{
                color: #666666;
            }
        ''')

        self.addCollectionsButton = QtWidgets.QPushButton(Form)
        self.addCollectionsButton.setGeometry(QtCore.QRect(138,472, 22, 22))
        self.addCollectionsButton.setToolTip('create custom element collections')
        self.removeCollectionsButton = QtWidgets.QPushButton(Form)
        self.removeCollectionsButton.setGeometry(QtCore.QRect(112,472, 22, 22))
        self.removeCollectionsButton.setToolTip('Remove element collections')
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(170, 60, 400, 400))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(131, 11, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(0,100, 200)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(131, 28, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.progressbar = QtWidgets.QProgressBar(self)
        self.progressbar.setGeometry(375,300,200,30)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color: rgb(255,255, 255)\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(14, 13, 91, 25))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap('%s'% (os.path.dirname(__file__)+'/logo.png')))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, unicodeUTF))

