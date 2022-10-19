from PyQt5 import QtCore, QtWidgets

class Ui_loadingPage(object):
    #We define the objects on the screen, as if it were the "css" of python.
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

    #This function is made to implement the multi-language support logic .
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Gerando Fractal", "Gerando Fractal"))
        self.label.setText(_translate("MainWindow", "Gerando Fractal, aguarde por favor!"))

#Where we render the window we call a popup, in which we ask the user to wait for the fractal to be generated!
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_loadingPage()
    
    ui.setupUi(MainWindow)
    
    MainWindow.show()

    MainWindow.close()
        
    sys.exit(app.exec_())
