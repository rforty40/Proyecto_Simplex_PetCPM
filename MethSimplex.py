
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
from PyQt5.QtCore import QObject

from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch

from interfaz.ui_ProgramaSimplexPERT import Ui_MainWindow


class MethSimplex(QMainWindow):
    
    def __init__(self,ui):
        super(MethSimplex, self).__init__()
        self.ui = ui
        #self.ui.setupUi(self)
        #self.ventana = Simplex(self.ui)

        #Simplex
        self.numVariables = 0
        self.numRestricciones = 0
        self.columSR = 0
        self.columSRcompletas = 0
        self.numHolgura = 0
        self.numArtificial = 0
        self.numIteraciones = 0
        self.solucion_optima = ""
        self.metodo = ""
        self.tituloMetodo = ""
        self.allTable=[]

        #Per y Simplex
        self.asignarComponentes()
        
        #Simplex
        self.editarComponentes()
        self.eventosDeBotones()
        self.eventocomboMetodo()

    def asignarComponentes(self):
         # Componentes de la interfaz Simplex
        # Paneles
        self.panelTablaU = QtWidgets.QFrame
        self.panelTablaU = self.ui.panelTblU
        self.panelFunYRest = QtWidgets.QFrame
        self.panelFunYRest = self.ui.panelVarRest
        # Combo box lista desplegables
        self.comboObjetivo = QtWidgets.QComboBox
        self.comboObjetivo = self.ui.cmbObjetivo
        self.comboMetodo = QtWidgets.QComboBox
        self.comboMetodo = self.ui.cmbMetodo
        # Etiquetas Labels
        self.etiquetaIteracion = QtWidgets.QLabel
        self.etiquetaIteracion = self.ui.lblIteracion
        self.etiquetaFunObj = QtWidgets.QLabel
        self.etiquetaFunObj = self.ui.lblFunObj
        self.etiquetaFuncionObjetivo = QtWidgets.QLabel
        self.etiquetaFuncionObjetivo = self.ui.lblFuncionObjetivo
        # Botones
        self.botonIteracion = QtWidgets.QPushButton
        self.botonIteracion = self.ui.btnIteracion
        self.botonPdf = QtWidgets.QPushButton
        self.botonPdf = self.ui.btnPdf
        self.botonCalcular = QtWidgets.QPushButton
        self.botonCalcular = self.ui.btnCalcular
        self.botonGenerar = QtWidgets.QPushButton
        self.botonGenerar = self.ui.btnGenerar

        # Campos de texto
        self.textFieldVar = QtWidgets.QLineEdit
        self.textFieldVar = self.ui.txtVar
        self.textFieldRestr = QtWidgets.QLineEdit
        self.textFieldRestr = self.ui.txtRestr

        # Tablas
        self.tablaVariables = QtWidgets.QTableWidget
        self.tablaVariables = self.ui.tblVariables
        self.tablaRestricciones = QtWidgets.QTableWidget
        self.tablaRestricciones = self.ui.tblRestricciones
        self.tablaU = QtWidgets.QTableWidget
        self.tablaU = self.ui.tbl_U
        self.tablaOperaciones = QtWidgets.QTableWidget
        self.tablaOperaciones = self.ui.tblOperaciones
        
          
    def editarComponentes(self):
        cmb = QtWidgets.QComboBox
        panel = QtWidgets.QFrame
        txt = QtWidgets.QLineEdit
        self.panelTablaU.setVisible(False)  # Ocultar panel
        self.panelFunYRest.setVisible(False)
        objMetodo = ["Método Simplex", "Método Big M"]
        self.comboMetodo.clear()
        self.comboMetodo.addItems(objMetodo)  # LLenar cmb Metodos
        objObjetivo = ["Minimizar", "Maximizar"]
        self.comboObjetivo.clear()
        self.comboObjetivo.addItems(objObjetivo) 
        self.comboObjetivo.setVisible(False)
        self.botonPdf.setVisible(False)
        self.etiquetaFunObj.setVisible(False)

    def eventosDeBotones(self):
        self.botonGenerar.clicked.connect(self.cargarProceso)
        self.botonCalcular.clicked.connect(self.cargarProceso)
        self.botonIteracion.clicked.connect(self.cargarProceso)
        self.botonPdf.clicked.connect(self.cargarProceso)
                   
    def show_popup_Informacion(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        x = msg.exec_()

    def cargarProceso(self):
        boton = self.sender()
        if boton == self.botonGenerar:

            if not self.textFieldVar.text() or not self.textFieldRestr.text():
                self.show_popup_Informacion(
                    "Datos invalidos", "No se ingresaron correctamente los datos")
            else:
                self.mostrarLabels(False)
                self.panelFunYRest.setVisible(True)
                self.numVariables = int(self.textFieldVar.text())
                self.numRestricciones = int(self.textFieldRestr.text())
                self.llenarTablaVar()
                self.llenarTablaRestr()
                if self.comboMetodo.currentIndex() == 1:
                    self.comboObjetivo.setVisible(True)

        elif boton == self.botonCalcular:
            if self.validarTablaFuncion() and self.validarTablaRestricciones(): #validar datos
                self.allTable = []
                self.matrizInicial()
                self.botonPdf.setVisible(False)
                self.metodo = ""
                self.tituloMetodo = ""
                if self.comboMetodo.currentIndex() == 0:
                    self.metodo = "MetodoSimplex"
                    self.tituloMetodo = "REPORTE MÉTODO SIMPLEX"
                else:
                    self.metodo = "MetodoBigM"
                    self.tituloMetodo = "REPORTE MÉTODO BIG M"

        elif boton == self.botonIteracion:
            
            if self.comboMetodo.currentIndex() == 0 or (self.comboMetodo.currentIndex() == 1 and self.comboObjetivo.currentIndex() == 1):
                if self.seguirIteracionesSimplex() == True:
                    self.iteraciones()
                else:
                    self.botonPdf.setVisible(True)
                    self.show_popup_Informacion(
                        "Mensaje", "Se han terminado las iteraciones")
            else:
                if self.seguirIteracionesBigM() == True:
                    self.iteraciones()
                else:
                    self.botonPdf.setVisible(True)
                    self.show_popup_Informacion(
                        "Mensaje", "Se han terminado las iteraciones")

        else:
            self.solucion_optima = self.tablaU.item((self.numRestricciones+2), self.columSRcompletas+1).text()
            
            self.generarReporte()
            #hilo = threading.Thread(target = self.generarReporte)
            #hilo.start()
    
    def mostrarLabels(self, estado):
        self.etiquetaFunObj.setVisible(estado)
        self.etiquetaFuncionObjetivo.setVisible(estado)
        self.tablaOperaciones.clear()
        self.tablaU.clear()
        self.panelTablaU.setVisible(estado)

    def llenarTablaVar(self):
        self.tablaVariables.clear()
        self.tablaVariables.setRowCount(1)
        self.tablaVariables.setColumnCount(self.numVariables)
        for i in range(self.numVariables):
            item1 = QTableWidgetItem(f"X{i+1}")
            item1.setBackground(QtGui.QColor(0, 153, 153))
            self.tablaVariables.setHorizontalHeaderItem(i, item1)

    def llenarTablaRestr(self):
        self.tablaRestricciones.clear()
        self.tablaRestricciones.setRowCount(self.numRestricciones)
        self.tablaRestricciones.setColumnCount(self.numVariables)
        for j in range(self.numVariables):
            item1 = QTableWidgetItem(f"X{j+1}")
            item1.setBackground(QtGui.QColor(0, 153, 153))
            self.tablaRestricciones.setHorizontalHeaderItem(j, item1)

        for i in range(self.numVariables, self.numVariables+2):
            item = QTableWidgetItem(" ")
            self.tablaRestricciones.insertColumn(i)
            item.setBackground(QtGui.QColor(0, 153, 153))
            self.tablaRestricciones.setHorizontalHeaderItem(i, item)

        fila = 0
        colum = self.numVariables
        cmbMeth = self.comboMetodo
        for j in range(self.numRestricciones):
            self.cmbSigno = QComboBox()
            self.cmbSigno.addItem("<=")
            if cmbMeth.currentIndex() == 1:
                self.cmbSigno.addItem(">=")
                self.cmbSigno.addItem("=")
            self.tablaRestricciones.setCellWidget(fila, colum, self.cmbSigno)

            fila += 1

    def eventocomboMetodo(self):
        self.comboMetodo.currentIndexChanged.connect(self.cambiocomboMetodo)

    def cambiocomboMetodo(self):
        fila = 0
        colum = self.numVariables
        for j in range(self.numRestricciones):
            self.cmbSigno = QComboBox()
            self.cmbSigno.addItem("<=")
            if self.comboMetodo.currentIndex() == 0:  # Metodo Simplex
                self.comboObjetivo.setCurrentIndex(1)  # Maximizar
                self.comboObjetivo.setVisible(False)
            else:
                self.comboObjetivo.setCurrentIndex(0)  # Minimizar
                self.comboObjetivo.setVisible(True)
                self.cmbSigno.addItem(">=")
                self.cmbSigno.addItem("=")
            self.tablaRestricciones.setCellWidget(fila, colum, self.cmbSigno)
            fila += 1

    def guardarRestricciones(self):
        restriccionesString = [" "]*(self.numRestricciones+1)
        columnas = self.numVariables+2
        valor = ""
        # restricciones
        comboOne = QtWidgets.QComboBox
        for i in range(0, len(restriccionesString)-1, 1):
            for j in range(0, columnas, 1):
                if j < self.numVariables:
                    valor = self.tablaRestricciones.item(i, j).text()
                  
                    if j == 0:
                        restriccionesString[i] = valor+"X"+str(j+1)
                    else:
                        if valor[0] == '-':
                            restriccionesString[i] += valor+"X"+str(j+1)
                        else:
                            restriccionesString[i] += "+" + \
                                valor + "X" + str(j + 1)
                elif j == self.numVariables:
                    comboOne = self.tablaRestricciones.cellWidget(
                        i, self.numVariables)
                    datoSigno = comboOne.currentText()
                    restriccionesString[i] += datoSigno
                else:
                    valor = self.tablaRestricciones.item(i, j).text()
                    restriccionesString[i] += valor
        
        # no negatividad
        restriccionesString[len(restriccionesString)-1] = ""

        for fila in range(0, self.numRestricciones, 1):
            restriccionesString[len(restriccionesString) -
                                1] += "X" + str(fila + 1) + ">=0"
                                
        return restriccionesString

    def matrizInicial(self):
        # Guarda las inecuaciones en el arreglo matriz inicial
        inecuaciones = self.sistemaRestricciones()
        # Definimos tamaño columnas y filas
        numColumnas = self.columSRcompletas+2
        numFilas = self.numRestricciones+4
        matriz = [["0"] * numColumnas for i in range(numFilas)]
        # espacios en blanco y datos que no cambian
        matriz[0][0] = " "
        matriz[0][1] = "CJ"
        matriz[0][numColumnas - 1] = " "
        matriz[1][0] = "CB"
        matriz[1][1] = "XB"
        matriz[1][numColumnas - 1] = "BI"
        matriz[numFilas - 2][0] = " "
        matriz[numFilas - 2][1] = "ZJ"
        matriz[numFilas - 1][0] = " "
        matriz[numFilas - 1][1] = "ZJ-CJ"
        matriz[numFilas - 1][numColumnas - 1] = " "
        # Xb, Cj filas
        numVar = 0
        numArt = 0
        funcion = ""
        stringDecimal = ""
        for j in range(2, (numColumnas-1), 1):
            # Cj Xb
            if numVar < self.numVariables:
                stringDecimal = self.tablaVariables.item(0, numVar).text()
                matriz[0][j] = self.devolverValorSR(stringDecimal)
                if matriz[0][j] == "Dato vacio":
                    print("Pendiente Thow Null")
                funcion += " "+str(matriz[0][j])
                matriz[1][j] = "X"+str(numVar+1)
                funcion += str(matriz[1][j])+" +"
                numVar += 1
            elif numVar < self.columSR:
                matriz[0][j] = "0"
                matriz[1][j] = "X"+str(numVar+1)
                numVar += 1
            else:
                if self.comboMetodo.currentIndex() == 0:  # Metodo Simplex
                    matriz[0][j] = "1"
                else:  # Metodo Big M
                    if self.comboObjetivo.currentIndex() == 0:  # Minimizar
                        matriz[0][j] = "M"
                    else:
                        matriz[0][j] = "-M"
                matriz[1][j] = "A" + str(numArt+1)
                numArt += 1
        # Ya no se lanza excepcion se pueden mostrar la tablaU y las etiquetas
        self.mostrarLabels(True)
        minmax = ""
        # Mostrar minimizar o maximizar
        if self.comboMetodo.currentIndex() == 0 or self.comboObjetivo.currentIndex() == 1:
            minmax = "Max Z = "
        else:
            minmax = "Min Z = "

        self.etiquetaFuncionObjetivo.setText(
            " "+minmax+funcion[0:len(funcion)-1])

        # Guardamos inecuaciones en matriz inicial
        for q in range(0, self.numRestricciones, 1):  # filas
            for w in range(0, self.columSRcompletas, 1):  # columnas
                matriz[q+2][w+2] = str(inecuaciones[q][w])
                # Agregar Cb y Xb columnas
                if str(inecuaciones[q][w]) == "1" and w >= self.numVariables:
                    matriz[q+2][0] = matriz[0][w+2]  # Cb
                    matriz[q+2][1] = matriz[1][w+2]  # Xb

        # Obtener fila zj
        stringZj = ""
        acumulaZj = ""
        for col in range(0, self.columSRcompletas, 1):
            acumulaZj = ""
            for fila in range(0, self.numRestricciones, 1):
                stringZj = self.guardarZj(
                    str(matriz[fila+2][0]), str(matriz[fila + 2][col + 2]))
                acumulaZj += stringZj+";"
            matriz[numFilas - 2][col + 2] = self.devolverZj(acumulaZj)

        # obtener fila cj-zj
        for col in range(2, (numColumnas-1), 1):
            matriz[numFilas - 1][col] = self.devolverZjCj(
                str(matriz[0][col]), str(matriz[numFilas - 2][col]))

        # mostrar matriz en la tabla
        self.tablaU.clear()
        self.tablaU.setRowCount(numFilas)
        self.tablaU.setColumnCount(numColumnas)

        for j in range(numColumnas):
            item1 = QTableWidgetItem(" ")
            #item1.setBackground(QtGui.QColor(0, 153, 153))
            self.tablaU.setHorizontalHeaderItem(j, item1)

        for row in range(0, numFilas, 1):
            for col in range(0, numColumnas, 1):
                item = QTableWidgetItem(str(matriz[row][col]))
                self.tablaU.setItem(row, col, item)

        self.tablaU.resizeColumnsToContents()

        # pintar pivote
        self.pintarPivote()

        self.numIteraciones = 0
        self.etiquetaIteracion.setText(" "+str(self.numIteraciones))

        # Guardar tabla para el pdf
        fila = self.numRestricciones+4
        columna = self.columSRcompletas+2
        tablaInicial = []
        for f in range(fila):
            filaAnterior = []
            for c in range(columna):
                item = self.tablaU.item(f, c).text()
                filaAnterior.append(item)
            tablaInicial.append(filaAnterior)
        self.allTable.append(tablaInicial)

    def guardarZj(self, cb, numero):
        multiCb = ""
        fracNum = Fraccion.Fraccion(0, 0)
        fracCB = Fraccion.Fraccion(0, 0)
        if numero == "0" or cb == "0":
            multiCb = "0"
        elif cb == "M":
            multiCb = numero + "M"
        elif cb == "-M":
            fracNum = fracNum.deTablaFraccion(numero)
            fracCB.setNumerador(-1)
            fracCB.setDenominador(1)
            multiCb = fracCB.multiplicar(fracNum).__str__() + "M"
        else:
            fracNum = fracNum.deTablaFraccion(numero)
            fracCB = fracCB.deTablaFraccion(cb)
            multiCb = fracCB.multiplicar(fracNum).__str__()
        return multiCb

    def devolverZj(self, acumulaZj):
        acumulaZj = acumulaZj[0:len(acumulaZj)-1]  # quitar ultimo ;
        arregloZj = acumulaZj.split(";")
        zjfinal = ""
        llevaM = False
        llevaFrac = False
        claseM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
        claseMAcum = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
        claseMAcum.setCoeficiente(Fraccion.Fraccion(0, 1))
        fracAcumuladora = Fraccion.Fraccion(0, 1)
        frac = Fraccion.Fraccion(0, 0)
    
        for k in range(0, len(arregloZj), 1):
            if claseM.esM(arregloZj[k]):
                claseM = claseM.obtenerM(arregloZj[k])
                claseMAcum = claseMAcum.sumaM(claseM)
                llevaM = True
            elif not arregloZj[k] == "0":
                fracAcumuladora = fracAcumuladora.sumar(
                    frac.deTablaFraccion(arregloZj[k]))
                llevaFrac = True
       
        if llevaM == False:
            zjfinal = fracAcumuladora.__str__()
        elif (llevaFrac == True) and (fracAcumuladora.__str__()[0] == "-"):
            zjfinal = claseMAcum.__str__()+fracAcumuladora.__str__()
        elif (llevaFrac == True) and (not fracAcumuladora.__str__()[0] == "-"):
            newM = ""
            if not claseMAcum.__str__() == "0":
                newM = claseMAcum.__str__()+"+"

            zjfinal = newM+fracAcumuladora.__str__()

        else:
            zjfinal = claseMAcum.__str__()
        corte0=""
        if len(zjfinal)>2:
            corte0 = zjfinal[len(zjfinal)-2:len(zjfinal)]
            if (corte0=="+0") or (corte0=="-0") :
                zjfinal= zjfinal[0:len(zjfinal)-2]
       
        return zjfinal

    def devolverZjCj(self, cj, zj):
        zjcj = ""
        newCj = ""
        corteM = ""
        corteFrac = ""
        posM = 0
        fraccionZj = Fraccion.Fraccion(0, 0)
        fraccionCj = Fraccion.Fraccion(0, 0)
        fracCorte = Fraccion.Fraccion(0, 0)
        zjM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
        cjM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
       
        if cj == "0" and zj == "0":  # 0 y 0
            zjcj = "0"
           
        elif zj=="" or zj==" ":
            zjcj=cj
          
        
        elif zjM.esM(zj) == True and cjM.esM(cj) == True:  # ambas son M
           
            if cj == "M":
                cj = "1M"
            if cj == "-M":
                cj = "-1M"
            if zj[len(zj)-1]=="0": #0-0
                zj= zj[0:len(zj)-2]
            posM = zj.find('M')
            # separar fraccion de M
            if posM == len(zj)-1:  # no tiene nada despues de M
                corteFrac = ""
            else:  # si tiene despues de M
                corteFrac = zj[posM+1:len(zj)]
                if corteFrac[0] == '-':
                    corteFrac = "+"+corteFrac[1:len(corteFrac)]
                else:
                    corteFrac = "-"+corteFrac[1:len(corteFrac)]

            corteM = zj[0:posM+1]
            # cambiar signo al corte M
            if corteM[0] == '-':
                corteM = corteM[1:len(corteM)]
            else:
                corteM = "-"+corteM

            cjM = cjM.obtenerM(cj)
            zjM = zjM.obtenerM(corteM)
            cjM = cjM.sumaM(zjM)
            zjcj = cjM.__str__()+corteFrac
            
          
        elif zjM.esM(zj):  # cj es numero zj = tiene M
            posM = zj.find('M')
            # separar M de fraccion
            if posM == len(zj)-1:  # no tiene nada despues de M
                fracCorte.setNumerador(0)
                fracCorte.setDenominador(1)
            else:  # si tiene despues de M
                corteFrac = zj[posM+1:len(zj)]
                # cambiar signo a fraccion
                if corteFrac[0] == '-':
                    corteFrac = corteFrac[1:len(corteFrac)]
                else:
                    corteFrac = "-" + corteFrac[1:len(corteFrac)]

                fracCorte = fracCorte.deTablaFraccion(corteFrac)

            corteM = zj[0:posM+1]
            

            # cambiar signo al corte M
            if corteM[0] == '-':
                corteM = corteM[1:len(corteM)]
            else:
                corteM = "-"+corteM

            # hacer calculo para la fraccion
            if cj == "0":
                fraccionCj.setNumerador(0)
                fraccionCj.setDenominador(1)
                fraccionCj = fraccionCj.deTablaFraccion(cj)
            else:
                fraccionCj = fraccionCj.deTablaFraccion(cj)

            fraccionCj = fraccionCj.sumar(fracCorte)

            if not fraccionCj.__str__()[0] == '-':
                newCj = "+"+fraccionCj.__str__()
            else:
                newCj = fraccionCj.__str__()
            if newCj[len(newCj)-1] == '0':
                newCj = ""

            zjcj = corteM+newCj
         

        elif cjM.esM(cj):  # cj tiene M zj es fraccion
            if cj == 'M':
                corteM = "1M"
            if cj == "-M":
                corteM = "-1M"

            if zj == "0":
                zjcj = corteM
            else:
                if zj[0] == '-':
                    zj = "+"+zj[1:len(zj)]
                else:
                    zj = "-"+zj
                zjcj = corteM+zj
           

        else:
            fraccionCj = fraccionCj.deTablaFraccion(cj)
            if zj[0] == '-':
                zj = zj[1:len(zj)]
            else:
                zj = "-"+zj
            fraccionZj = fraccionZj.deTablaFraccion(zj)
            zjcj = fraccionCj.sumar(fraccionZj).__str__()
           
        return zjcj

    def sistemaRestricciones(self):
        sinExpcecion = False
        self.columSR = 0
        self.columSRcompletas = 0
        self.numHolgura = 0
        self.numArtificial = 0
        # numero de columnas que ocupan las variables de la funcion objtivo
        self.columSR = self.numVariables
        # ciclo que aumenta columnas
        combo = QtWidgets.QComboBox
        for i in range(0, self.numRestricciones, 1):
            combo = self.tablaRestricciones.cellWidget(i, self.numVariables)
            signo = combo.currentText()
            if signo == ">=":
                self.numHolgura += 1
                self.numArtificial += 1
            elif signo == "=":
                self.numArtificial += 1
            else:
                self.numHolgura += 1

        self.columSR += self.numHolgura
        self.columSRcompletas = self.columSR+self.numArtificial+1

        # Matriz
        restricciones = [
            [0] * self.columSRcompletas for i in range(self.numRestricciones)]

        # Ciclo para agregar los coeficientes de la funcion objetivo
        stringDecimal1 = ""
        for iResFila in range(0, self.numRestricciones, 1):
            if sinExpcecion:
                break

            for iResCol in range(0, self.numVariables, 1):
                stringDecimal1 = self.tablaRestricciones.item(
                    iResFila, iResCol).text()
                restricciones[iResFila][iResCol] = self.devolverValorSR(
                    stringDecimal1)
                if restricciones[iResFila][iResCol] == "Dato vacio":
                    sinExpcecion = True
                    break

        if sinExpcecion == False:
            numIguales = 0
            combo = QtWidgets.QComboBox
            for iResFila in range(0, self.numRestricciones, 1):
                combo = self.tablaRestricciones.cellWidget(
                    iResFila, self.numVariables)
                signo = combo.currentText()
                for iResCol in range(0, self.numHolgura, 1):
                    if iResFila == (iResCol+numIguales):
                        if signo == ">=":
                            restricciones[iResFila][iResCol +
                                                    self.numVariables] = "-1"
                        elif signo == "=":
                            restricciones[iResFila][iResCol +
                                                    self.numVariables] = "0"
                        else:
                            restricciones[iResFila][iResCol +
                                                    self.numVariables] = "1"
                    else:
                        restricciones[iResFila][iResCol +
                                                self.numVariables] = "0"
                if signo == "=":
                    numIguales += 1

            saltoFila = 0
            combo = QtWidgets.QComboBox
            for iResFila in range(0, self.numRestricciones, 1):
                combo = self.tablaRestricciones.cellWidget(
                    iResFila, self.numVariables)
                signo = combo.currentText()
                for iResCol in range(0, self.numArtificial, 1):

                    if iResFila == (iResCol+saltoFila):

                        if signo == "<=":
                            restricciones[iResFila][iResCol+self.columSR] = "0"
                        else:
                            restricciones[iResFila][iResCol+self.columSR] = "1"
                    else:
                        restricciones[iResFila][iResCol+self.columSR] = "0"

                if signo == "<=":
                    saltoFila += 1

            stringDecimal2 = ""
            for bi in range(0, self.numRestricciones, 1):
                stringDecimal2 = self.tablaRestricciones.item(
                    bi, self.tablaRestricciones.columnCount()-1).text()
                restricciones[bi][self.columSRcompletas -
                                  1] = self.devolverValorSR(stringDecimal2)
                if restricciones[bi][self.columSRcompletas-1] == "Dato vacio":
                    sinExpcecion = True
                    break
            if sinExpcecion:
                return  # retorna None
            else:
                return restricciones

        else:
            return  # retorna None
    
    def devolverValorSR(self, stringDecimal):
        fracString = ""
        frac = Fraccion.Fraccion(0, 0)
        try:
            decimal = float(stringDecimal)  #convierto a decimal
            try:
                if decimal % int(decimal) == 0:#es un numero entero
                    fracString = stringDecimal 
                else:
                     fracString =  frac.toFraccion(decimal).__str__()
            except ZeroDivisionError:# en caso de ingresar un 0.4
                     fracString =  frac.toFraccion(decimal).__str__()
        except ValueError:
             fracString = "Dato vacio"
        
        return fracString

    def variableSalida(self):
        fraccionAij = Fraccion.Fraccion(0, 0)
        fraccionBi = Fraccion.Fraccion(0, 0)
        vSal = float(0)
        siguiente = float(0)
        numColumnas = self.columSRcompletas+2
        numFilas = self.numRestricciones+4
        menor = 2  # posicion ubicacion
        ve = self.variableEntrada()  # ubicacion de la variable de entrada
        entra = True  # booleana para ejecutarse una sola vez
        aij = float(0)
        bi = float(0)
        stringAij = ""
        stringBi = ""
        for i in range(2, (numFilas-2), 1):  # ciclo recorre las filas de las inecuaciones
            stringAij = self.tablaU.item(i, ve).text()
            if fraccionAij.posicionBarra(stringAij) == -1:
                aij = float(stringAij)
            else:
                fraccionAij = fraccionAij.deTablaFraccion(stringAij)
                aij = fraccionAij.toDecimal()

            stringBi = self.tablaU.item(i, numColumnas-1).text()
            if fraccionBi.posicionBarra(stringBi) == -1:
                bi = float(stringBi)
            else:
                fraccionBi = fraccionBi.deTablaFraccion(stringBi)
                bi = fraccionBi.toDecimal()
          
            if (aij > 0) and (bi > 0):  # para que no haya division entre 0
                siguiente = float(bi/aij)
                if entra:  # solo se ejecuta una vez al inicio del ciclo
                    vSal = siguiente  # vSal toma el primer valor de siguiente
                    entra = False
                    menor = i

                if siguiente < vSal:  # condicional para que determinar el menor valor
                    vSal = siguiente
                    menor = i
        return menor

    def variableEntrada(self):
        numColumnas = self.columSRcompletas+2
        numFilas = self.numRestricciones+4
        contador = 3
        posicion = 2  # primera posicion
        fraccionVent = Fraccion.Fraccion(0, 0)
        fraccionSig = Fraccion.Fraccion(0, 0)
        vEnt = float(0)
        siguiente = float(0)
        stringVent = ""
        stringSig = ""
        claseM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")

        stringVent = claseM.obtenerValorSinM(
            self.tablaU.item(numFilas-1, 2).text())
        if fraccionVent.posicionBarra(stringVent) == -1:
            vEnt = float(stringVent)
        else:
            fraccionVent = fraccionVent.deTablaFraccion(stringVent)
            vEnt = fraccionVent.toDecimal()

        while contador < numColumnas-1:  # ciclo para hallar
            stringSig = claseM.obtenerValorSinM(
                self.tablaU.item(numFilas-1, contador).text())
            if fraccionSig.posicionBarra(stringSig) == -1:
                siguiente = float(stringSig)
            else:
                fraccionSig = fraccionSig.deTablaFraccion(stringSig)
                siguiente = fraccionSig.toDecimal()

            if self.comboMetodo.currentIndex() == 0 or self.comboObjetivo.currentIndex() == 1:
                if siguiente > vEnt:  # si el siguiente valor es menor
                    vEnt = siguiente  # vEnt toma ese valor para ser comparado en la siguiente vuelta del ciclo
                    posicion = contador  # guarda la ubicacion de la columna
            else:
                if siguiente < vEnt:  # si el siguiente valor es menor
                    vEnt = siguiente  # vEnt toma ese valor para ser comparado en la siguiente vuelta del ciclo
                    posicion = contador
            contador += 1

        return posicion

    def iteraciones(self):
        numColumnas = self.columSRcompletas+2
        numFilas = self.numRestricciones+4
        # matriz para tomar los datos actuales de la tabla
        anteriorIteracion = [[" "]*numColumnas for i in range(numFilas)]
        # matriz para insertar nuevos datos a la tabla
        nuevaIteracion = [[" "]*numColumnas for i in range(numFilas)]

        # llenar matriz anterior
        for i in range(0, numFilas, 1):
            for j in range(0, numColumnas, 1):
                anteriorIteracion[i][j] = self.tablaU.item(i, j).text()

        # llenar 2 primeras filas de la nueva matriz
        for k in range(0, 2, 1):
            for m in range(0, numColumnas, 1):
                nuevaIteracion[k][m] = self.tablaU.item(k, m).text()

        col = self.variableEntrada()  # ubicacion de la columna del pivote
        fila = self.variableSalida()  # ubicacion de la fila del pivote

        # obtener fila 1
        f1Fila1 = Fraccion.Fraccion(0, 0)
        f2Fila1 = Fraccion.Fraccion(0, 0)
        fila1 = [Fraccion.Fraccion(0, 0)]*(numColumnas-2)
        string1Fila1 = ""
        string2Fila1 = ""
        for i in range(0, len(fila1), 1):
            string1Fila1 = str(anteriorIteracion[fila][2+i])
            string2Fila1 = str(anteriorIteracion[fila][col])
            f1Fila1 = f1Fila1.deTablaFraccion(string1Fila1)
            fila1[i] = f1Fila1.dividir(f2Fila1.deTablaFraccion(string2Fila1))

        # obtener las otras filas 0 y llenar la tabla de ecuaciones
        numColEcuaciones = numColumnas - 1
        numFilaEcuaciones = (self.numRestricciones - 1) * 6
        matrizEcuaciones = [
            [" "]*numColEcuaciones for i in range(numFilaEcuaciones)]  # matriz
        stringNega = ""
        stringFila0 = ""
        fracNega = Fraccion.Fraccion(0, 0)
        fracFila0 = Fraccion.Fraccion(0, 0)
        fracMulti0 = Fraccion.Fraccion(0, 0)
        saltoFila = -6
        multiplicador = ""

        for iterador in range(2, (numFilas-2), 1):
            if not iterador == fila:  # si se cumpla se calcula el valor de las nuevas filas 0
                saltoFila += 6
                for j in range(2, numColumnas, 1):
                    stringNega = str(anteriorIteracion[iterador][col])
                    fracNega = fracNega.deTablaFraccion(stringNega)
                    fracNega = fracNega.multiplicar(Fraccion.Fraccion(-1, 1))

                    stringFila0 = str(anteriorIteracion[iterador][j])
                    fracFila0 = fracFila0.deTablaFraccion(stringFila0)
                    fracMulti0 = fila1[j - 2].multiplicar(fracNega)
                    matrizEcuaciones[saltoFila + 1][j - 1] = str(fila1[j - 2])
                    matrizEcuaciones[saltoFila + 2][j -
                                                    1] = str(fracMulti0.__str__())
                    fracMulti0 = fracMulti0.sumar(fracFila0)
                    matrizEcuaciones[saltoFila + 3][j -
                                                    1] = str(fracFila0.__str__())
                    matrizEcuaciones[saltoFila + 4][j -
                                                    1] = str(fracMulti0.__str__())
                    nuevaIteracion[iterador][j] = fracMulti0.__str__()

                    multiplicador = str(anteriorIteracion[iterador][col])
                    if multiplicador[0] == '-':
                        multiplicador[1:len(multiplicador)]
                    else:
                        multiplicador = "-" + multiplicador

                    matrizEcuaciones[saltoFila][0] = anteriorIteracion[iterador][1] + "' = " + \
                        anteriorIteracion[1][col] + \
                        "(" + multiplicador + ") + " + \
                        anteriorIteracion[iterador][1]
                    matrizEcuaciones[1 +
                                     saltoFila][0] = anteriorIteracion[1][col] + " = "
                    matrizEcuaciones[2 + saltoFila][0] = multiplicador + \
                        "(" + anteriorIteracion[1][col] + ") = "
                    matrizEcuaciones[3 +
                                     saltoFila][0] = anteriorIteracion[iterador][1] + " = "
                    matrizEcuaciones[4 +
                                     saltoFila][0] = anteriorIteracion[iterador][1] + "' = "
            else:  # si no se cumple se guarda la fila 1 donde corresponde
                for j in range(2, numColumnas, 1):
                    nuevaIteracion[iterador][j] = fila1[j - 2].__str__()

        # mostrar matriz en la tabla de ecuaciones
        self.tablaOperaciones.clear()
        self.tablaOperaciones.setRowCount(numFilaEcuaciones)
        self.tablaOperaciones.setColumnCount(numColEcuaciones)

        for j in range(numColEcuaciones):
            item1 = QTableWidgetItem(" ")
            self.tablaOperaciones.setHorizontalHeaderItem(j, item1)

        for row in range(0, numFilaEcuaciones, 1):
            for colT in range(0, numColEcuaciones, 1):
                item = QTableWidgetItem(str(matrizEcuaciones[row][colT]))
                self.tablaOperaciones.setItem(row, colT, item)

        self.tablaOperaciones.resizeColumnsToContents()

        # llenar CB y XB
        for icb in range(2, (numFilas-2), 1):
            for ixb in range(0, 2, 1):
                if icb == fila:
                    nuevaIteracion[fila][ixb] = anteriorIteracion[ixb][col]
                else:
                    nuevaIteracion[icb][ixb] = anteriorIteracion[icb][ixb]

        # llenar Zj
        nuevaIteracion[numFilas -
                       2][0] = anteriorIteracion[numFilas - 2][0]  # " "
        nuevaIteracion[numFilas -
                       2][1] = anteriorIteracion[numFilas - 2][1]  # "Zj"
        stringZj = ""
        acumulaZj = ""

        for i in range(2, numColumnas, 1):
            acumulaZj = ""
            for j in range(2, (numFilas-2), 1):
                stringZj = self.guardarZj(
                    str(nuevaIteracion[j][0]), str(nuevaIteracion[j][i]))
                acumulaZj += stringZj + ";"

            nuevaIteracion[numFilas - 2][i] = self.devolverZj(acumulaZj)
            
        # llenar Cj-Zj
        nuevaIteracion[numFilas -
                       1][0] = anteriorIteracion[numFilas - 1][0]  # " "
        nuevaIteracion[numFilas -
                       1][1] = anteriorIteracion[numFilas - 1][1]  # "Zj-Cj"
        nuevaIteracion[numFilas - 1][numColumnas -
                                     1] = anteriorIteracion[numFilas - 1][numColumnas - 1]  # " "
        stringA = ""
        stringB = ""
        for i in range(2, (numColumnas-1), 1):
            stringA = str(nuevaIteracion[0][i])
            stringB = str(nuevaIteracion[numFilas - 2][i])
            nuevaIteracion[numFilas -
                           1][i] = self.devolverZjCj(stringA, stringB)
           
        # mostrar matriz en la tabla
        self.tablaU.clear()
        self.tablaU.setRowCount(numFilas)
        self.tablaU.setColumnCount(numColumnas)

        for j in range(numColumnas):
            item1 = QTableWidgetItem(" ")
            self.tablaU.setHorizontalHeaderItem(j, item1)

        for row in range(0, numFilas, 1):
            for colT in range(0, numColumnas, 1):
                item = QTableWidgetItem(str(nuevaIteracion[row][colT]))
                self.tablaU.setItem(row, colT, item)
        self.tablaU.resizeColumnsToContents()

        # pintar pivote
        self.pintarPivote()

        self.numIteraciones += 1
        self.etiquetaIteracion.setText(" "+str(self.numIteraciones))

        # Guardar tabla para el pdf
        fila = self.numRestricciones+4
        columna = self.columSRcompletas+2
        tablaItera = []
        for f in range(fila):
            filaAnterior = []
            for c in range(columna):
                item = self.tablaU.item(f, c).text()
                filaAnterior.append(item)
            tablaItera.append(filaAnterior)
        self.allTable.append(tablaItera)

    def seguirIteracionesSimplex(self):
        seSigue = False
        numColumnas = self.columSRcompletas + 2
        numFilas = self.numRestricciones + 4
        stringSig = ""
        siguiente = float(0)
        claseM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
        fraccionSig = Fraccion.Fraccion(0, 0)
        for i in range(2, (numColumnas-2), 1):
            stringSig = claseM.obtenerValorSinM(
                self.tablaU.item(numFilas-1, i).text())
            if fraccionSig.posicionBarra(stringSig) == -1:
                siguiente = float(stringSig)
            else:
                fraccionSig = fraccionSig.deTablaFraccion(stringSig)
                siguiente = fraccionSig.toDecimal()

            if siguiente > 0:
                seSigue = True

        return seSigue

    def seguirIteracionesBigM(self):
        seSigue = False
        numColumnas = self.columSRcompletas + 2
        numFilas = self.numRestricciones + 4
        stringSig = ""
        siguiente = float(0)
        claseM = ClaseM.ClaseM(Fraccion.Fraccion(0, 0), "M")
        fraccionSig = Fraccion.Fraccion(0, 0)
        for i in range(2, (numColumnas-2), 1):
            stringSig = claseM.obtenerValorSinM(
                self.tablaU.item(numFilas-1, i).text())
            if fraccionSig.posicionBarra(stringSig) == -1:
                siguiente = float(stringSig)
            else:
                fraccionSig = fraccionSig.deTablaFraccion(stringSig)
                siguiente = fraccionSig.toDecimal()

            if siguiente < 0:
                seSigue = True

        return seSigue

    def pintarPivote(self):
        fila = self.variableSalida()  # ubicacion de la variable de salida
        col = self.variableEntrada()  # ubicacion de la variable de entrada
        pivote = self.tablaU.item(fila, col).text()
        item = QTableWidgetItem(str(pivote))
        item.setBackground(QtGui.QColor(0, 153, 153))
        self.tablaU.setItem(fila, col, item)

    def generarReporte(self):

        fila = self.numRestricciones+4
        columna = self.columSRcompletas+2

        tituloReporte = "Reporte_"+self.metodo+".pdf"
        try:
            doc = SimpleDocTemplate(tituloReporte, pagesize=A4, topMargin=12)
            alineacionTitulo = ParagraphStyle(
                name="centrar", alignment=TA_CENTER, fontSize=20, leading=40)
            alineacionTituloTabla = ParagraphStyle(
                name="centrar", alignment=TA_CENTER, fontSize=14, leading=40)
            alineacionOpTable = ParagraphStyle(
                name="centrar", alignment=TA_CENTER, fontSize=12, leading=40)
            alineacionResultados = ParagraphStyle(
                name="centrar", alignment=TA_LEFT, fontSize=12, leading=30)
            alineacionRestr = ParagraphStyle(
                name="centrar", alignment=TA_CENTER, fontSize=12, leading=30)

            story = []

            restriccionesGuardadas = self.guardarRestricciones()
            resultados = self.guardarResultados()
            self.guardarRestricciones() #guarda solucion optima y el resultados de las variables

            story.append(Paragraph(self.tituloMetodo, alineacionTitulo))
            story.append(Paragraph(
                f"Función Objetivo: {self.etiquetaFuncionObjetivo.text()}", alineacionResultados))
            
            story.append(Paragraph(f"S.R:", alineacionResultados))
            
            for restr in range(len(restriccionesGuardadas)):
                story.append(
                    Paragraph(restriccionesGuardadas[restr], alineacionResultados))
            
            solucion = "La solución óptima es Z = "+self.solucion_optima
            story.append(Paragraph(solucion, alineacionTituloTabla))
            
            variables =""
            for iResul in range(len(resultados)):
                variables+=resultados[iResul]
            story.append(Paragraph(variables, alineacionOpTable)) 

          
            for table in range(len(self.allTable)):
                self.arrayFila = []
                for f in range(fila):
                    item = self.allTable[table][f]
                    self.arrayFila.append(item)

                tabla = Table(self.arrayFila, colWidths=50, rowHeights=40)
                tabla.setStyle([
                    ('GRID', (0, 0), (-1, -1), 2, colors.black),
                    ('BOX', (0, 0), (-1, -1), 2, colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('BACKGROUND', (0, 0), (-1, 1),
                     colors.HexColor('#009999')),
                    ('TEXTCOLOR', (0, 0), (-1, 1), colors.HexColor('#ffffff'))
                ])

                story.append(
                    Paragraph(f"Iteración #{table}", alineacionTituloTabla))
                story.append(tabla)
                story.append(Spacer(0, 2))
                
                if(table+1 == len(self.allTable)):
                    story.append(Spacer(0, 0))
                else:
                    story.append(Spacer(0, 250))
                
               

            doc.build(story)

            msjErr = "Reporte generado correctamente"
            msgBox5 = QMessageBox()
            msgBox5.setText(msjErr)
            msgBox5.setWindowTitle("Éxito")
            msgBox5.setStyleSheet(
                "font-size: 14px; font-weight: bold; font-family: Century Gothic")
            msgBox5.exec_()

            os.system(tituloReporte+"&& exit")
        except PermissionError:
            msjErr = "Ocurrió un error al generar el reporte"
            msgBox6 = QMessageBox()
            msgBox6.setText(msjErr)
            msgBox6.setWindowTitle("Error")
            msgBox6.setStyleSheet(
                "font-size: 14px; font-weight: bold; font-family: Century Gothic")
            msgBox6.exec_()
        
    def guardarResultados(self):
        resultados = []
        columnas = self.columSRcompletas+2
        filas = self.numRestricciones+4
        arregloXBFila = [" "] * (columnas-3)
        arregloXBCol = [" "] * self.numRestricciones
        for i in range(0, len(arregloXBFila), 1):
            arregloXBFila[i] = self.tablaU.item(1,(i+2)).text() #guardo XB Fila
        for i in range(0,len(arregloXBCol),1):
            arregloXBCol[i]= self.tablaU.item((i+2),1).text() #guardo XB columna
        
        resultados=[" "]*len(arregloXBFila)
        #ciclo para llenar el arreglo de resultado
        for i in range(0, len(arregloXBFila), 1):
            resultados[i]=arregloXBFila[i]+" = 0, "
            #ciclo para asignar el valor de BI
            for j in range(0,len(arregloXBCol),1):
                if arregloXBFila[i] == arregloXBCol[j]:
                    resultados[i]=arregloXBFila[i]+" = "+self.tablaU.item((j+2),(columnas-1)).text()+", "
        return resultados



    def validarTablaFuncion(self):
        datosOk= True
        for i in range(self.numVariables):
            try:
                dato= int(self.tablaVariables.item(0,i).text())
            except ValueError:
                try:
                    dato = float(self.tablaVariables.item(0,i).text())
                except ValueError:
                    datosOk=False
                    self.show_popup_Informacion("Dato no válido en la tabla Función Objetivo",
                    "Solo se permite el ingreso de enteros o decimales")
                    break           
            except AttributeError:
                datosOk=False
                self.show_popup_Informacion("Dato inválido",
                "Dato vacío en la tabla Función Objetivo")
                break


    
        return datosOk

    def validarTablaRestricciones(self):
        datosOk=True
        for row in range (self.tablaRestricciones.rowCount()):
            for col in range (self.tablaRestricciones.columnCount()):
                if not col == self.tablaRestricciones.columnCount()-2: #no se toma en cuenta la columna con el signo de la restriccion
                    try:
                        dato= int(self.tablaRestricciones.item(row,col).text())
                        
                    except ValueError:
                        try:
                            dato = float(self.tablaRestricciones.item(row,col).text())
                        except ValueError:
                            datosOk=False
                            self.show_popup_Informacion("Dato no válido en la tabla Restricciones","Solo se permite el ingreso de enteros o decimales")
                            break
                    except AttributeError:
                        datosOk=False
                        self.show_popup_Informacion("Dato inválido",
                        "Dato vacío en la tabla Restricciones")
                        break

            if datosOk == False:
                break
        return datosOk







