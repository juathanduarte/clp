from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showFractal(object):
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

    def retranslateUi(self, FractalGerado):
        _translate = QtCore.QCoreApplication.translate
        FractalGerado.setWindowTitle(_translate("Fractal Gerado", "Fractal Gerado"))


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    FractalGerado = QtWidgets.QFractalGerado()
    
    ui = Ui_showFractal()
    ui.setupUi(FractalGerado)
    
    FractalGerado.show()
    
    sys.exit(app.exec_())
