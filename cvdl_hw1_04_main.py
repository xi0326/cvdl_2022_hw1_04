from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import MainWindow as ui
import os

from Q4.Q4 import Question4

class Main(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image1Path = None
        self.image2Path = None

        # Load data
        self.pushButtonLoadImage1.clicked.connect(self.getImage1Path)
        self.pushButtonLoadImage2.clicked.connect(self.getImage2Path)
        
        # Question 4
        self.pushButtonShowKeypoints.clicked.connect(lambda: Q4Object.showKeypoints(self.image1Path))
        self.pushButtonShowMatchedKeypoints.clicked.connect(lambda: Q4Object.showMatchedKeypoints(self.image1Path, self.image2Path))

    def selectFile(self):
        fileName = QtCore.QDir.toNativeSeparators(QtWidgets.QFileDialog.getOpenFileName(None, caption='Choose a File', directory='C:\\', filter='Image Files (*.png *.jpg *.bmp)')[0])  # get turple[0] which is file name
        return fileName
    
    def getImage1Path(self):
        self.image1Path = self.selectFile()
    
    def getImage2Path(self):
        self.image2Path = self.selectFile()
    
    # overide to force exit
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        os._exit(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Q4Object = Question4()
    window = Main()
    window.show()
    sys.exit(app.exec_())