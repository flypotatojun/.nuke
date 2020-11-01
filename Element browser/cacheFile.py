try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *


from ui_cacheFiles import Ui_CacheFiles
import os
import element_settings


class TestListView(QListWidget):
    def __init__(self, parent=None):
        super(TestListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(72, 72))
        self.setObjectName("listWidget_file")
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addMenu()

    def addMenu(self):
        remove = QAction(self)
        clear_all = QAction(self)
        remove.setText('Remove')
        clear_all.setText('clear all')
        remove.triggered.connect(self.removeItem)
        clear_all.triggered.connect(self.clearAll)
        self.addAction(remove)
        self.addAction(clear_all)

    def clearAll(self):
        for l in range(self.count()):
            self.takeItem(self.row(self.item(l)))
    def removeItem(self):
        row = self.selectedItems()
        for item in row:
            self.takeItem(self.row(item))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path):
                self.addItem(path)

class ExecuteGifPanelCache(Ui_CacheFiles, QWidget):
    def __init__(self):
        super(ExecuteGifPanelCache, self).__init__()
        self.setupUi(self)
        self.dict = {}
        self.pushButton_images.setChecked(True)
        # self.currentCollectionItem = currentCollectionItemName
        element_settings.element_settings()
        self.pushButton_images.clicked.connect(self.activeButton)
        self.pushButton_imgSeq.clicked.connect(self.activeButton)

        self.lineEdit_destination.setText("{}".format(element_settings.gif_directory))
        self.list = TestListView(self)
        self.gridLayout.addWidget(self.list)
        self.pushButton_startCache.clicked.connect(self.triggerConversion)
        self.pushButton_cancel.clicked.connect(self.close)

    def activeButton(self):
        buttons = [self.pushButton_images,  self.pushButton_imgSeq]
        for button in buttons:
            sender = self.sender()
            if button == sender:
                button.setCheckable(True)
                button.setStyleSheet('''QPushButton{
                            background-color: rgb(0, 100, 200);
                }''')
            else:
                button.setCheckable(False)
                button.setStyleSheet('''QPushButton{
                            background-color: #333333;
                }''')


    def triggerConversion(self):
        self.convertToGif(os.path.basename(self.lineEdit_source.text()))

    def convertToGif(self,currentCollection):
        self.sourceFilePath = []
        if os.path.isdir(self.lineEdit_source.text()):
            if os.listdir(self.lineEdit_source.text()):
                for file in os.listdir(self.lineEdit_source.text()):
                    sourceFile = os.path.join(self.lineEdit_source.text(), file)
                    self.sourceFilePath.append(sourceFile)
                    tst = list(os.path.splitext(sourceFile))
                    if os.path.exists(
                            os.path.join(element_settings.gif_directory, currentCollection)):
                        pass
                    else:
                        os.makedirs(
                            os.path.join(element_settings.gif_directory, currentCollection))
                    targetFile = os.path.join(element_settings.gif_directory,
                                              currentCollection, os.path.basename(tst[0]) + '.gif')
                    self.startConvert(sourceFile, targetFile)
        else:
            for item in range(self.list.count()):
                sourceFile = os.path.join(self.list.item(item).text())
                tst = list(os.path.splitext(self.list.item(item).text()))
                self.sourceFilePath.append(sourceFile)
                if os.path.exists(os.path.join(element_settings.gif_directory, currentCollection)):
                    pass
                else:
                    os.makedirs(os.path.join(element_settings.gif_directory, currentCollection))
                targetFile = os.path.join(element_settings.gif_directory, currentCollection, os.path.basename(tst[0]) + '.gif')
                self.startConvert(sourceFile, targetFile)


    def startConvert(self, input, output):
        import subprocess
        cmds = [element_settings.ffmpegPath , '-i', input, '-aspect', '16:9', '-vf', 'scale=133:80', '-r', '15', output, '-hide_banner']
        t = subprocess.Popen(cmds)



def runCachePanel():
    runCachePanel.cachePanel = ExecuteGifPanelCache()
    runCachePanel.cachePanel.show()
