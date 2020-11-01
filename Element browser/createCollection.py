try:
    from PySide import QtGui,  QtGui as QtWidgets, QtCore
except:
    from PySide2 import QtWidgets, QtCore, QtGui

class Ui_popupAddCollections(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Ui_popupAddCollections, self).__init__(parent)
        self.setObjectName("popupAddCollections")
        self.resize(296, 72)
        self.addButton = QtWidgets.QPushButton(self)
        self.addButton.setGeometry(QtCore.QRect(134, 40, 75, 23))
        self.addButton.setObjectName("addButton")
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setGeometry(QtCore.QRect(214, 40, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.lineEdit_collection = QtWidgets.QLineEdit(self)
        self.lineEdit_collection.setGeometry(QtCore.QRect(8, 10, 281, 20))
        self.lineEdit_collection.setObjectName("lineEdit_collection")
        self.lineEdit_collection.setPlaceholderText('Enter the Collection Name...')
        self.setStyleSheet('''
            QDialog{
                background-color: #222222;
            }
            QLineEdit{
                border: None;
                color: #FFFFFF;
                background-color : #333333;
            }
            QPushButton{
                 background-color : #333333;
            }
            
        ''')
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, popupAddCollections):
        popupAddCollections.setWindowTitle("Create Collection")
        self.addButton.setText("Add")
        self.cancelButton.setText("Cancel")

