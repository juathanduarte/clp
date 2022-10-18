from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_LoadingPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(252, 60)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
                
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Gerando Fractal", "Gerando Fractal"))
        self.label.setText(_translate("MainWindow", "Gerando Fractal, aguarde por favor!"))


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_LoadingPage()
    
    ui.setupUi(MainWindow)
    
    MainWindow.show()

    MainWindow.close()
        
    sys.exit(app.exec_())
