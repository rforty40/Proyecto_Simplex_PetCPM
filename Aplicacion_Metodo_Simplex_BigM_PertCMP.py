from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import os
from PyQt5.Qt import QAbstractItemModel, QApplication, QBrush, QColor, QComboBox, QStyleFactory, QTableWidgetItem
import sys
import Fraccion
import ClaseM
import MethPert
import MethSimplex
from PyQt5.QtCore import QObject

from interfaz.ui_ProgramaSimplexPERT import Ui_MainWindow



class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventanaPert = MethPert.MethPert(self.ui)
        self.ventanaSimplex = MethSimplex.MethSimplex(self.ui)
        self.eventosFrame()
    
    def eventosFrame(self):
        self.ui.menuCalculadora_M_todo_Simplex.aboutToShow.connect(self.cargarFrame)
        self.ui.menuProyecto_PERT_CMP.aboutToShow.connect(self.cargarFrame)
            
    def cargarFrame(self):
        ventana = self.sender()

        if ventana == self.ui.menuProyecto_PERT_CMP:
            self.ventana = self.ventanaPert
            self.ui.frameSimplex.setVisible(False)
            self.ui.framePert.setVisible(True)
       
            
           
        else:      
            self.ventana = self.ventanaSimplex
            self.ui.framePert.setVisible(False)
            self.ui.frameSimplex.setVisible(True)
           

    def resolver_ruta(self, ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

    def rutaParaCSS(self,rutaFondo):
        nuevaRutaiM = ""
        for iRu in range(0, len(rutaFondo), 1):
            if ord(rutaFondo[iRu]) == 92:
                nuevaRutaiM += str("/")
            else:
                nuevaRutaiM += rutaFondo[iRu]
        return nuevaRutaiM

 


# Inicia la aplicación
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    mi_App = VentanaPrincipal()
    #Definir icono ventana
    rutaIcono = mi_App.resolver_ruta("interfaz/img/iconoDelaTabla.ico")
    mi_App.setWindowIcon(QIcon(rutaIcono))
    #Fondo Frame Simplex
    rutaFondoIm = mi_App.resolver_ruta("interfaz/img/atardecer2.jpg")
    nuevaRutaiMagen = mi_App.rutaParaCSS(rutaFondoIm)
    mi_App.ui.lblFondo.setStyleSheet("background-image: url("+nuevaRutaiMagen+");")
    #Fondo Frame Pert
    rutaFondoIm = mi_App.resolver_ruta("interfaz/img/fondoPert.png")
    nuevaRutaiMagen = mi_App.rutaParaCSS(rutaFondoIm)
    mi_App.ui.lblFondoPert.setStyleSheet("background-image: url("+nuevaRutaiMagen+");")

    mi_App.show()
    sys.exit(app.exec_())
