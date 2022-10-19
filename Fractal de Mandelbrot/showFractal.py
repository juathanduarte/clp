from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showFractal(object):
    #We set the objects on the screen, from the image to the size of the window.
    def setupUi(self, FractalGerado):
        FractalGerado.setObjectName("FractalGerado")
        FractalGerado.resize(1280, 720)
        FractalGerado.setMinimumSize(QtCore.QSize(1280, 720))
        FractalGerado.setMaximumSize(QtCore.QSize(1280, 720))
    
        self.centralwidget = QtWidgets.QWidget(FractalGerado)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(1280, 720))
        self.label.setMaximumSize(QtCore.QSize(1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fractal.png"))
        self.label.setObjectName("label")
        
        self.horizontalLayout.addWidget(self.label)
        
        FractalGerado.setCentralWidget(self.centralwidget)

        self.retranslateUi(FractalGerado)
        QtCore.QMetaObject.connectSlotsByName(FractalGerado)

    #This function is made to implement the multi-language support logic.
    def retranslateUi(self, FractalGerado):
        _translate = QtCore.QCoreApplication.translate
        FractalGerado.setWindowTitle(_translate("Fractal Gerado", "Fractal Gerado"))

#Where we render the window with the generated fractal!
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    FractalGerado = QtWidgets.QFractalGerado()
    
    ui = Ui_showFractal()
    ui.setupUi(FractalGerado)
    
    FractalGerado.show()
    
    sys.exit(app.exec_())
