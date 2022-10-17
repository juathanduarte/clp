import time
from PyQt5 import QtCore, QtGui, QtWidgets
from ctypes import *
from segundaTela import Ui_SecondWindow

mandelbrotGen = CDLL("./libMandelbrot.so")

# mandelbrotGen.mandelbrot()
class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        mandelbrotGen.main()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.left_container = QtWidgets.QFrame(self.centralwidget)
        self.left_container.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_container.setObjectName("left_container")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.left_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.frame = QtWidgets.QFrame(self.left_container)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.title_Fractal = QtWidgets.QLabel(self.frame)
        self.title_Fractal.setObjectName("title_Fractal")
        
        self.horizontalLayout_2.addWidget(self.title_Fractal)
        
        self.verticalLayout_4.addWidget(self.frame)
        
        self.frame_2 = QtWidgets.QFrame(self.left_container)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setObjectName("toolBox")
        
        self.page_membros = QtWidgets.QWidget()
        self.page_membros.setGeometry(QtCore.QRect(0, 0, 246, 370))
        self.page_membros.setObjectName("page_membros")
        
        self.gridLayout = QtWidgets.QGridLayout(self.page_membros)
        self.gridLayout.setObjectName("gridLayout")
        
        self.avatar_Juathan = QtWidgets.QLabel(self.page_membros)
        self.avatar_Juathan.setMaximumSize(QtCore.QSize(150, 150))
        self.avatar_Juathan.setText("")
        self.avatar_Juathan.setPixmap(QtGui.QPixmap("interface/avatares/juatsAvatar.png"))
        self.avatar_Juathan.setScaledContents(True)
        self.avatar_Juathan.setObjectName("avatar_Juathan")
        
        self.gridLayout.addWidget(self.avatar_Juathan, 0, 0, 1, 1)
        
        self.name_Juathan = QtWidgets.QLabel(self.page_membros)
        self.name_Juathan.setObjectName("name_Juathan")
        
        self.gridLayout.addWidget(self.name_Juathan, 1, 0, 1, 1)
        
        self.avatar_Lucas = QtWidgets.QLabel(self.page_membros)
        self.avatar_Lucas.setMaximumSize(QtCore.QSize(150, 150))
        self.avatar_Lucas.setText("")
        self.avatar_Lucas.setPixmap(QtGui.QPixmap("interface/avatares/lucasAvatar.png"))
        self.avatar_Lucas.setScaledContents(True)
        self.avatar_Lucas.setObjectName("avatar_Lucas")
        
        self.gridLayout.addWidget(self.avatar_Lucas, 2, 0, 1, 1)
        
        self.name_Lucas = QtWidgets.QLabel(self.page_membros)
        self.name_Lucas.setObjectName("name_Lucas")
        
        self.gridLayout.addWidget(self.name_Lucas, 3, 0, 1, 1)
        
        self.toolBox.addItem(self.page_membros, "")
        
        self.page_sobre = QtWidgets.QWidget()
        self.page_sobre.setGeometry(QtCore.QRect(0, 0, 260, 358))
        self.page_sobre.setObjectName("page_sobre")
        
        self.label = QtWidgets.QLabel(self.page_sobre)
        self.label.setGeometry(QtCore.QRect(10, 0, 241, 351))
        self.label.setObjectName("label")
        
        self.toolBox.addItem(self.page_sobre, "")
        
        self.horizontalLayout_3.addWidget(self.toolBox)
        
        self.verticalLayout_4.addWidget(self.frame_2)
        
        self.horizontalLayout.addWidget(self.left_container)
        
        self.right_container = QtWidgets.QFrame(self.centralwidget)
        self.right_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_container.setObjectName("right_container")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_container)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.header_frame = QtWidgets.QFrame(self.right_container)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.title_clp = QtWidgets.QLabel(self.header_frame)
        self.title_clp.setObjectName("title_clp")
        
        self.verticalLayout_2.addWidget(self.title_clp)
        
        self.verticalLayout.addWidget(self.header_frame)
        
        self.main_frame = QtWidgets.QFrame(self.right_container)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        
        self.label_4 = QtWidgets.QLabel(self.main_frame)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 62, 17))
        self.label_4.setObjectName("label_4")
        
        self.button_GerarFractal = QtWidgets.QPushButton(self.main_frame, clicked = lambda: self.openWindow())
        self.button_GerarFractal.setGeometry(QtCore.QRect(10, 320, 435, 150))
        self.button_GerarFractal.setMinimumSize(QtCore.QSize(250, 150))
        self.button_GerarFractal.setMaximumSize(QtCore.QSize(435, 150))
        self.button_GerarFractal.setObjectName("button_GerarFractal")
        # self.button_GerarFractal.clicked.connect(mandelbrot)
        
        self.verticalLayout.addWidget(self.main_frame)
        
        self.footer_frame = QtWidgets.QFrame(self.right_container)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footer_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.title_footer = QtWidgets.QLabel(self.footer_frame)
        self.title_footer.setObjectName("title_footer")
        
        self.verticalLayout_3.addWidget(self.title_footer)
        
        self.verticalLayout.addWidget(self.footer_frame)
        
        self.horizontalLayout.addWidget(self.right_container)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Fractal de Mandelbrot - Juathan Duarte & Lucas Ferreira", "Fractal de Mandelbrot - Juathan Duarte & Lucas Ferreira"))
        self.title_Fractal.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Fractal de</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Mandelbrot</span></p></body></html>"))
        self.name_Juathan.setText(_translate("MainWindow", "Juathan Coelho Duarte"))
        self.name_Lucas.setText(_translate("MainWindow", "Lucas Simões Ferreira"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_membros), _translate("MainWindow", "Membros"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:6pt; font-weight:600;\">Conjunto de Mandelbrot</span><span style=\" font-size:6pt;\"> é um </span></p><p align=\"center\"><span style=\" font-size:6pt;\">fractal definido como o conjunto </span></p><p align=\"center\"><span style=\" font-size:6pt;\">de pontos no plano, definido </span></p><p align=\"center\"><span style=\" font-size:6pt;\">recursidamente.</span></p><p align=\"center\"><span style=\" font-size:6pt;\">Em sua representação gráfica, pode </span></p><p align=\"center\"><span style=\" font-size:6pt;\">ser dividido em um conjunto infinito de </span></p><p align=\"center\"><span style=\" font-size:6pt;\">figuras, sendo a maior delas um </span></p><p align=\"center\"><span style=\" font-size:6pt;\">cardióide localizado ao centro do plano.</span></p><p align=\"center\"><span style=\" font-size:6pt;\">Existe uma infinidade de quase-círculos </span></p><p align=\"center\"><span style=\" font-size:6pt;\">que tangenciam o cardióide e variam </span></p><p align=\"center\"><span style=\" font-size:6pt;\">de tamanho com raio tendendo a zero.</span></p><p align=\"center\"><span style=\" font-size:6pt;\">Cada um desses círculos tem seu </span></p><p align=\"center\"><span style=\" font-size:6pt;\">próprio conjunto infinito de pequenos </span></p><p align=\"center\"><span style=\" font-size:6pt;\">círculos cujos raios também tendem a zero. </span></p><p align=\"center\"><span style=\" font-size:6pt;\">Esse processo se repete infinitamente, </span></p><p align=\"center\"><span style=\" font-size:6pt;\">gerando uma figura fractal.</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_sobre), _translate("MainWindow", "Sobre"))
        self.title_clp.setText(_translate("MainWindow", "CLP - Conceitos de Linguagens de Programação"))
        self.label_4.setText(_translate("MainWindow", "Options:"))
        self.button_GerarFractal.setText(_translate("MainWindow", "Gerar Fractal de Mandelbrot aleatório"))
        self.title_footer.setText(_translate("MainWindow", "Todos direitos reservados"))
    
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    
    sys.exit(app.exec_())