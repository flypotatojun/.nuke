import sys, os, math
from ui_element_browser import Ui_Form
import element_settings
import json

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *


class DraggableLabel(QWidget):
    def __init__(self, imagePath, currentItem, file, fileFormat, activeListWidget,parent=None):
        super(DraggableLabel, self).__init__(parent)
        self.addItemsToWidget()
        self.file, self.item, self.fileFormat ,self.activeListWidget, self.imagePath= file, currentItem, fileFormat, activeListWidget, imagePath
        if fileFormat == 'mov':
            gifFile = open(os.path.join(imagePath, file), 'rb').read()
            self.gifByteArray = QByteArray(gifFile)
            self.gifBuffer = QBuffer(self.gifByteArray)
            self.movie = QMovie()
            self.imagePath = imagePath
            size = self.movie.scaledSize()
            self.label.setGeometry(0, 0, size.width(), size.height())
            self.movie.setDevice(self.gifBuffer)
            self.movie.setCacheMode(QMovie.CacheAll)
            self.movie.setSpeed(100)
            self.label.setMovie(self.movie)
            self.movie.jumpToFrame(20)
        elif fileFormat == 'png' or fileFormat == 'exr' or fileFormat == 'tif':
            pixmap = QPixmap(os.path.join(imagePath, file))
            self.label.setPixmap(pixmap)
        self.addContextMenu()

    def addItemsToWidget(self):
        self.label = QLabel()
        self.label2 = QLabel()
        self.layout = QVBoxLayout()
        self.setGeometry(0, 0, 133, 80)
        self.label2.setContentsMargins(0, 0, 0, 0)
        self.label.setContentsMargins(0, 0, 0, 5)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setMaximumSize(130, 10)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)
        self.setLayout(self.layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

    def addContextMenu(self):
        playWithPdPlayer = QAction(self)
        showInExplorer = QAction(self)
        playWithPdPlayer.setText('Play')
        showInExplorer.setText('Show in Explorer')
        self.addAction(playWithPdPlayer)
        self.addAction(showInExplorer)
        playWithPdPlayer.triggered.connect(self.play)
        showInExplorer.triggered.connect(self.exploreFiles)
        if self.activeListWidget == 'list2':
            removeItem = QAction(self)
            removeItem.setText('Delete')
            self.addAction(removeItem)
            removeItem.triggered.connect(self.removeItemFromList)
        if self.activeListWidget == 'list1':
            self.label2.setText(os.path.splitext(self.file)[0] + '.' + self.fileFormat)
            self.path = os.path.normpath(
                os.path.join(element_settings.root_directory, (element_settings.dict_item[self.item]).split('@')[0],
                             os.path.splitext(self.file)[0] + '.' + self.fileFormat))

        else:
            self.load_json = json.load(open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath ,'tempCollectionData.txt'))))
            activeFilePath = self.load_json[list(os.path.splitext(self.file))[0]]
            normpath = os.path.normpath(activeFilePath).split('@')[0]
            self.label2.setText(os.path.splitext(self.file)[0] + '.' +  os.path.normpath(activeFilePath).split('@')[1])
            self.path = os.path.normpath(os.path.join(normpath))



    def exploreFiles(self):
        import platform
        if sys.platform == 'win32':
            os.system('explorer "%s"' % os.path.dirname(self.path))
        if sys.platform == 'darwin':
            os.system('open "%s"' % os.path.dirname(self.path))
        if sys.platform == 'linux2':
            os.system('xdg-open "%s"' % os.path.dirname(self.path))


    def play(self):
        import platform
        self.leaveEvent(self)
        if sys.platform == 'win32':
            os.system('explorer %s' % self.path)
        if sys.platform == 'darwin':
            os.system('open "%s"' % self.path)
        if sys.platform == 'linux2':
            os.system('xdg-open "%s"' % self.path)

    def removeItemFromList(self):
        os.remove(os.path.join(self.imagePath, self.file))

    def enterEvent(self, event):
        if self.fileFormat == 'mov':
            self.movie.jumpToFrame(0)
            self.movie.start()

    def leaveEvent(self, event):
        if self.fileFormat == 'mov':
            self.movie.jumpToFrame(20)
            self.movie.stop()

    def mouseMoveEvent(self, event):
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.path)
        drag.setMimeData(mimedata)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        text = event.mimeData().text()
        self.setText(text)
        event.accept()


class ElementBrowser(Ui_Form, QWidget):
    def __init__(self):
        super(ElementBrowser, self).__init__()
        self.setupUi(self)
        self.modifyPanelProperties()
        self.dict = {}
        element_settings.element_settings()
        self.createDataFiles()
        for item in list(element_settings.dict_item.keys()):
            self.listWidget.addItem(item)
        self.addListWidget2Items()
        self.listWidget.setCurrentRow(0)
        self.indexData, self.columnCount = [], 3
        self.listWidget.itemClicked.connect(self.switchItems)
        self.listWidget2.itemClicked.connect(self.switchItemsInCollectionList)
        self.collectionsListWidgetContextMenu()
        self.addCollectionsButton.clicked.connect(self.customCollectionList)
        self.removeCollectionsButton.clicked.connect(self.removeCollectionsFromList)
        self.load_json = json.load(open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt'))))
        self.addThumbs(self.columnCount)

    def settingUpPath(self):
        try:
            self.currentItemFromList = self.getCurrentItemFromAnyLists().split('@')[0]
            if self.getCurrentItemFromAnyLists().split('@')[1] == 'list1':
                self.rootPath = os.path.join(element_settings.root_directory,element_settings.dict_item[self.currentItemFromList])
                self.currentDictValue = str(element_settings.dict_item[self.currentItemFromList])
                self.gifPath = element_settings.gif_directory
                self.nativeFileName, self.nativeFileFormat = self.currentDictValue.split('@')[0], self.currentDictValue.split('@')[1]
                self.currentGifPath = os.path.join(self.gifPath, self.nativeFileName)
            else:
                self.load_json = json.load(open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt'))))
                self.rootPath = os.path.join(element_settings.collectionsGifRoot, self.load_json[self.currentItemFromList])
                self.currentDictValue = str(self.load_json[self.currentItemFromList])
                self.gifPath = element_settings.collectionsGifRoot
                self.nativeFileName, self.nativeFileFormat = self.currentDictValue.split('@')[0], self.currentDictValue.split('@')[1]
                self.currentGifPath = os.path.join(self.gifPath, self.nativeFileName)
        except:
            pass


    def addThumbs(self, columnCount):
        try:
            self.tableWidget.clear()
            self.settingUpPath()
            imgs = os.listdir(self.currentGifPath)
            rowCount = int(math.ceil(len(imgs) / columnCount)+1)
            self.tableWidget.setColumnCount(columnCount)
            self.tableWidget.setRowCount(rowCount)
            i = 0
            for row in range(rowCount):
                for column in range(columnCount):
                    if i == len(imgs):
                        break
                    lb = DraggableLabel(self.currentGifPath, self.currentItemFromList, imgs[i], self.nativeFileFormat,self.getCurrentItemFromAnyLists().split('@')[1])
                    self.tableWidget.setCellWidget(row, column, lb)
                    to_mov = os.path.splitext(imgs[i])[0] + ".mov"
                    self.indexData.append('{}@{}@{}@{}'.format(os.path.join(self.rootPath, to_mov), i, row, column))
                    i += 1
                    self.loadingFilesProgress(i,len(imgs))
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setMouseTracking(True)
        except:
            pass



    def modifyPanelProperties(self):
        self.setWindowTitle('Element Browser')
        self.tableWidget.setContentsMargins(0, 0, 0, 0)
        self.setGeometry(0,0, 892, 500)
        self.setMinimumSize(450, 439)
        self.setMaximumWidth(892)
        self.addCollectionsButton.setStyleSheet(
            '''QPushButton{border: 1.2px solid #111111;border-radius: 5px;image: url('%s');padding: 4px; }''' % (os.path.dirname(__file__)+'/plus_03.png'))
        self.removeCollectionsButton.setStyleSheet(
            '''QPushButton{border: 1.2px solid #111111;border-radius: 5px;image: url('%s');padding: 3px; }''' % (os.path.dirname(__file__)+'/minus_03.png'))


    def resizeEvent(self, event):
        self.tableWidget.setGeometry(QRect(170, 60, self.width() - 175, self.height() - 75))
        self.addThumbs(self.columnCountCalc())
        self.progressbar.setGeometry(QRect(int(((self.width() - 175)/2)+ 85), int(((self.height() -75)/2)+30) , 200, 30))
        self.listWidget2.setGeometry(QRect(10, 505, 151, self.height()-530))

    def createDataFiles(self):
        if not os.path.isdir(os.path.normpath(element_settings.tempCOllectionPath)):
            os.makedirs(os.path.normpath(element_settings.tempCOllectionPath))
            if not os.path.isfile(os.path.normpath(os.path.join(element_settings.tempCOllectionPath ,'tempCollectionData.txt'))):
                with open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'tempCollectionData.txt')), 'w') as fileTempCollection:
                    fileTempCollection.write('{}')
                    fileTempCollection.close()
            if not os.path.isfile(os.path.normpath(os.path.join(element_settings.tempCOllectionPath ,'custom_dict.txt'))):
                with open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt')), 'w') as fileCustomDict:
                    fileCustomDict.write('{}')
                    fileCustomDict.close()




    def columnCountCalc(self):
        if 700 < self.tableWidget.width() <= 976:
            self.columnCount = 5
        elif 550 <= self.tableWidget.width() < 730:
            self.columnCount = 4
        elif self.tableWidget.width() < 575:
            self.columnCount = 3
        return self.columnCount

    def switchItems(self):
        self.clearSelectionsOnListWidget2()
        self.addThumbs(self.columnCount)

    def switchItemsInCollectionList(self):
        self.clearSelectionsOnListWidget()
        self.addThumbs(self.columnCount)

    def clearSelectionsOnListWidget(self):
        if self.listWidget2.currentItem():
            self.listWidget.clearSelection()
        else:
            self.listWidget2.clearSelection()

    def clearSelectionsOnListWidget2(self):
        if self.listWidget.currentItem():
            self.listWidget2.clearSelection()
        else:
            self.listWidget.clearSelection()


    def getCurrentItemFromAnyLists(self):
        if self.listWidget2.selectedItems():
            activeItem = self.listWidget2.currentItem().text() + '@list2'
        else:
            activeItem = self.listWidget.currentItem().text()+ '@list1'
        return activeItem

    def loadingFilesProgress(self, filesLoaded, total):
        progress = int((float(filesLoaded) / total) * 100)
        self.progressbar.setValue(progress)
        if not progress % 100:
            self.progressbar.setVisible(False)
        else:
            self.progressbar.setVisible(True)

    def customCollectionList(self):
        from createCollection import Ui_popupAddCollections
        self.popup = Ui_popupAddCollections()
        self.popup.addButton.clicked.connect(self.addCollection)
        self.popup.cancelButton.clicked.connect(self.popup.close)
        self.showpopup()

    def addCollection(self):
        if self.popup.lineEdit_collection.text():
            collectionsGifPath = os.path.join(element_settings.collectionsGifRoot,self.popup.lineEdit_collection.text())
            if not os.path.exists(collectionsGifPath):
                os.makedirs(collectionsGifPath)
            self.listWidget2.clear()
            self.updateCollectionDict()
            self.popup.close()

    def updateCollectionDict(self):
        customCollectionsDirectory = []
        for dir in os.listdir(element_settings.collectionsGifRoot):
            self.listWidget2.addItem(dir)
            customCollectionsDirectory.append(dir)
        for dir in customCollectionsDirectory:
            t =  str(dir) +"@mov"
            self.dict.update({'{}'.format(dir):'{}'.format(t) })
            json.dump( self.dict, open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt')),'w'))

    def addListWidget2Items(self):
        if os.path.exists(element_settings.collectionsGifRoot):
            self.listWidget2.clear()
            for dir in os.listdir(element_settings.collectionsGifRoot):
                self.listWidget2.addItem(dir)

    def removeCollectionsFromList(self):
        import shutil
        activeListItem = '"%s"'%self.listWidget2.currentItem().text()
        filePath =os.path.join(element_settings.collectionsGifRoot,self.listWidget2.currentItem().text())
        with open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt'))) as customJson:
            jsonFile= json.load(customJson)
            for element in jsonFile:
                if activeListItem in element:
                    self.dict.pop(activeListItem)
                    del element[activeListItem]
        with open(os.path.normpath(os.path.join(element_settings.tempCOllectionPath, 'custom_dict.txt')),'w') as customJson:
            jsonFile = json.dump(jsonFile, customJson)
        for selectedList in self.listWidget2.selectedItems():
            self.listWidget2.takeItem(self.listWidget2.currentRow())
        shutil.rmtree(filePath)



    def collectionsListWidgetContextMenu(self):
        addActionToList = QAction(self)
        addActionToList.setText('Add Files')
        self.listWidget2.addAction(addActionToList)
        self.listWidget2.setContextMenuPolicy(Qt.ActionsContextMenu)
        addActionToList.triggered.connect(self.openCachePanel)

    def openCachePanel(self):
        from executeCache import ExecuteGifPanel
        self.cacheExecution = ExecuteGifPanel(self.listWidget2.currentItem().text(), self.nativeFileFormat)
        self.cacheExecution.show()
        self.addThumbs(self.columnCount)

    def showpopup(self):
        self.popup.exec_()






def runElementBrowser():
    runElementBrowser.browserPanel = ElementBrowser()
    runElementBrowser.browserPanel.show()
