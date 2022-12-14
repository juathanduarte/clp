from PyQt5 import QtCore, QtWidgets
from ctypes import *

from showFractal import Ui_showFractal
from loadingPage import Ui_loadingPage

mandelbrotGen = CDLL("./libMandelbrot.so")

class FractalThread(QtCore.QThread):
    def run(self):
        mandelbrotGen.main()

class Ui_MainWindow(object):
    def openLoadingPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loadingPage()
        self.ui.setupUi(self.window)
        self.window.show()
        self.worker = FractalThread()
        self.worker.start()
        self.worker.finished.connect(self.openWindow)
    
    def openWindow(self):
        self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_showFractal()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 535)
        MainWindow.setMinimumSize(QtCore.QSize(775, 535))
        MainWindow.setMaximumSize(QtCore.QSize(775, 535))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.left_container = QtWidgets.QFrame(self.centralwidget)
        self.left_container.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_container.setObjectName("left_container")
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left_container)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.title_Fractal = QtWidgets.QLabel(self.left_container)
        self.title_Fractal.setObjectName("title_Fractal")
        
        self.verticalLayout_5.addWidget(self.title_Fractal)
        
        self.label = QtWidgets.QLabel(self.left_container)
        self.label.setObjectName("label")
        
        self.verticalLayout_5.addWidget(self.label)
        
        self.horizontalLayout.addWidget(self.left_container)
        
        self.right_container = QtWidgets.QFrame(self.centralwidget)
        self.right_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_container.setObjectName("right_container")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_container)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.rightTop_container = QtWidgets.QFrame(self.right_container)
        self.rightTop_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightTop_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightTop_container.setObjectName("rightTop_container")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rightTop_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.title_clp = QtWidgets.QLabel(self.rightTop_container)
        self.title_clp.setObjectName("title_clp")
        
        self.verticalLayout_2.addWidget(self.title_clp)
        
        self.verticalLayout.addWidget(self.rightTop_container)
        
        self.rightDown_container = QtWidgets.QFrame(self.right_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightDown_container.sizePolicy().hasHeightForWidth())
        self.rightDown_container.setSizePolicy(sizePolicy)
        self.rightDown_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightDown_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightDown_container.setObjectName("rightDown_container")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightDown_container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Descricao = QtWidgets.QLabel(self.rightDown_container)
        
        self.label_Descricao.setObjectName("label_Descricao")
        
        self.verticalLayout_3.addWidget(self.label_Descricao)
        
        self.button_GerarFractal = QtWidgets.QPushButton(self.rightDown_container, clicked = lambda: self.openLoadingPage())
        self.button_GerarFractal.setMinimumSize(QtCore.QSize(250, 150))
        self.button_GerarFractal.setMaximumSize(QtCore.QSize(500, 150))
        self.button_GerarFractal.setObjectName("button_GerarFractal")
        
        self.verticalLayout_3.addWidget(self.button_GerarFractal)
        self.verticalLayout.addWidget(self.rightDown_container)
        self.horizontalLayout.addWidget(self.right_container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fractal de Mandelbrot - Juathan Duarte & Lucas Ferreira"))
        self.title_Fractal.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Fractal de</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Mandelbrot</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Membros: </span></p><p align=\"center\">Juathan Coelho Duarte</p><p align=\"center\">Lucas Sim??es Ferreira</p></body></html>"))
        self.title_clp.setText(_translate("MainWindow", "CLP - Conceitos de Linguagens de Programa????o | 2022/1"))
        self.label_Descricao.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Conjunto de Mandelbrot</span> ?? um fractal definido como o conjunto </p><p align=\"center\">de pontos no plano, definido recursidamente.</p><p align=\"center\">Em sua representa????o gr??fica, pode ser dividido em um conjunto </p><p align=\"center\">infinito de figuras, sendo a maior delas um cardi??ide localizado ao </p><p align=\"center\">centro do plano.</p><p align=\"center\">Existe uma infinidade de quase-c??rculos que tangenciam o </p><p align=\"center\">cardi??ide e variam de tamanho com raio tendendo a zero.</p><p align=\"center\">Cada um desses c??rculos tem seu pr??prio conjunto infinito de </p><p align=\"center\">pequenos c??rculos cujos raios tamb??m tendem a zero. </p><p align=\"center\">Esse processo se repete infinitamente, gerando uma figura fractal.</p></body></html>"))
        self.button_GerarFractal.setText(_translate("MainWindow", "Gerar Fractal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
