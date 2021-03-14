from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import QBrush
from PyQt5.Qt import QColor
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator

from interfaz.ui_modalLaborales import Ui_modalFecha

from datetime import date, datetime, timedelta

import Actividad  # CLASE ACTIVIDAD
import sys
import os


class MethPert(QMainWindow):

    def __init__(self, ui):
        super(MethPert, self).__init__()
        self.ui = ui

        self.asignarcomponentesPert()
        self.eventosBotonesPert()

        # Variables globales
        self.MatrizActividades = []
        self.diasNoLab = []
        self.numActividades = 0

        self.mostrarEtiquetas(False)

        # desactivar botones
        self.cambiarEstadoBoton(self.botonCalPert, False)
        self.cambiarEstadoBoton(self.botonNewPert, False)

    def cambiarEstadoBoton(self, botonP, estado):
        if estado:
            botonP.setEnabled(estado)
            botonP.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"border-radius: 10px;")
        else:
            botonP.setEnabled(estado)
            botonP.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250,0.7);\n"
"border-radius: 10px;")

    def asignarcomponentesPert(self):

        # SpinBox
        self.spinNumPert = QtWidgets.QSpinBox
        self.spinNumPert = self.ui.spinNumActividades

        # Botones
        self.botonCalPert = self.ui.btnCalcularPert
        self.botonGenPert = self.ui.btnGenerarTbl
        self.botonNewPert = self.ui.btnNuevoPert

        # Tabla
        self.tablaActividades = self.ui.tblActividades

        # Etiquetas
        self.etiquetaFechaInicio = self.ui.lblFechaIncio
        self.etiquetaFechaFin = self.ui.lblFechaFin
        self.etiquetaFindes = self.ui.lblFindes

    def eventosBotonesPert(self):
        self.botonGenPert.clicked.connect(self.cargarProcesoPert)
        self.botonCalPert.clicked.connect(self.cargarProcesoPert)
        self.botonNewPert.clicked.connect(self.cargarProcesoPert)

    def cargarProcesoPert(self):
        boton = self.sender()

        if boton == self.botonGenPert:
            # Validar datos y generar la fila de las actividades
            if self.spinNumPert.text() == "0" or int(self.spinNumPert.text()) > 26:
                self.show_popup_InformacionP(
                    "Dato no válido", "El número de actividades debe ser mayor que 0 y menor a 27")
            else:
                self.generarTablaPer()
                self.mostrarEtiquetas(False)

        elif boton == self.botonCalPert:
            # Validar numeros enteros en To, Tn, Tp y los antecesores
            if self.verificarDatosIngresados():

                # desactivar botones
                self.cambiarEstadoBoton(self.botonCalPert, True)
                self.cambiarEstadoBoton(self.botonNewPert, True)

                self.calcularRutasCriticas()
                self.pintarRutasCriticas()

                # mostrar ventana para seleccionar Fecha
                rutaFondoIm = self.resolver_ruta("interfaz/img/fondoPert.png")
                nuevaRutaiMagen = self.rutaParaCSS(rutaFondoIm)
                self.dialogFecha = DialogFecha()
                self.dialogFecha.ui.lblFondoModal.setStyleSheet(
                    "background-image: url("+nuevaRutaiMagen+");")
                self.dialogFecha.show()
                self.dialogFecha.ui.btnAceptarFecha.clicked.connect(
                    self.obtenerFechas)

                self.cambiarEstadoBoton(self.botonNewPert, True)

        else:  # boton Nuevo
            self.generarTablaPer()
            self.mostrarEtiquetas(False)
            # desactivar botones
            self.cambiarEstadoBoton(self.botonNewPert, False)

    def generarTablaPer(self):
        # habilito botones
        self.cambiarEstadoBoton(self.botonCalPert, True)
        self.cambiarEstadoBoton(self.botonNewPert, True)

        # guardo el numero de las actividades
        self.numActividades = int(self.spinNumPert.text())
        # limpiar tabla
        self.tablaActividades.clear()
        # numero de filas
        self.tablaActividades.setRowCount(self.numActividades)
        # numero de columnas
        self.tablaActividades.setColumnCount(18)
        # ponemos los titulos de la columna
        self.listColumnas = [" Actividad ", " Detalle ", " Predecesores ", " To ", " Tn ", " Tp ", " D i,j ", " O i,j ", " Ti0 ", " Ti1 ", " Tj0 ",
                             " Tj1 ", " MT i,j ", " MI i,j ", " Fecha Inicio temprano ", " Fecha Inicio tardío ", " Fecha Fin temprano ", " Fecha Fin tardío "]
        # insertar columnas
        for i in range(18):
            item = QTableWidgetItem(self.listColumnas[i])
            item.setBackground(QtGui.QColor(21, 30, 61))
            item.setForeground(QBrush(QColor(255, 223, 0)))
            self.tablaActividades.setHorizontalHeaderItem(i, item)

        # insertat celdas
        for j in range(self.numActividades):
            for k in range(18):
                item = QTableWidgetItem("")
                self.tablaActividades.setItem(j, k, item)

        self.tablaActividades.resizeColumnsToContents()
        # lista de actividades
        self.listadeActividades = []
        # poner las letras del abecedario
        self.letras = list(map(chr, range(65, 91)))  # Lista de A - Z
        for i in range(self.numActividades):
            celda = QTableWidgetItem(self.letras[i])
            self.listadeActividades.append(self.letras[i])
            # celda.setTextAlignment(Qt.AlignHCenter)
            self.tablaActividades.setItem(i, 0, celda)

        self.show_popup_InformacionP(
            "Guía", "Los precedesores de las actividades deben ser ingresados separados por comas, asi A,B\nPara las actividades sin predecesores debe ingresar N/A")

    def calcularRutasCriticas(self):
        # matriz de las actividades
        self.MatrizActividades = [Actividad.Actividad]*(self.numActividades+2)

        # Actividades que no estan en la tabla
        self.MatrizActividades[0] = Actividad.Actividad("N/A", "", "", 0, 0, 0)
        self.MatrizActividades[len(
            self.MatrizActividades)-1] = Actividad.Actividad("FIN", "", "", 0, 0, 0)

        # ciclo para crear los objetos de la matriz
        for row in range(1, (len(self.MatrizActividades)-1), 1):
            self.MatrizActividades[row] = Actividad.Actividad(
                self.tablaActividades.item(row-1, 0).text(),
                self.tablaActividades.item(row-1, 1).text(),
                self.tablaActividades.item(row-1, 2).text(),
                int(self.tablaActividades.item(row-1, 3).text()),
                int(self.tablaActividades.item(row-1, 4).text()),
                int(self.tablaActividades.item(row-1, 5).text()))

        # IDA
        self.ida()

        # VUELTA
        self.vuelta()

        # ciclo para mostrar en la tabla Dij, Oij, Ti0, Tj0, Ti1, Tj1, Mtij, Mlij
        for tabrow in range(0, self.numActividades, 1):
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getDij()))
            self.tablaActividades.setItem(tabrow, 6, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getOij()))
            self.tablaActividades.setItem(tabrow, 7, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getTi0()))
            self.tablaActividades.setItem(tabrow, 8, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getTi1()))
            self.tablaActividades.setItem(tabrow, 9, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getTj0()))
            self.tablaActividades.setItem(tabrow, 10, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getTj1()))
            self.tablaActividades.setItem(tabrow, 11, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getMargenTotal()))
            self.tablaActividades.setItem(tabrow, 12, item)
            item = QTableWidgetItem(
                str(self.MatrizActividades[tabrow+1].getMargenLibre()))
            self.tablaActividades.setItem(tabrow, 13, item)

    # Ida en busca de Ti0 y Tj0
    def ida(self):
        for i in range(1, len(self.MatrizActividades), 1):  # Empieza desde la actividad A

            if i == (len(self.MatrizActividades)-1):
                self.MatrizActividades[i].setlistaPredecesores(
                    self.obtenerPredecesoresDelFin())

            if self.MatrizActividades[i].getlistaPredecesores()[0] == "N/A":

                self.MatrizActividades[i].setTi0(
                    self.MatrizActividades[0].getTj0())
                self.MatrizActividades[i].setTj0(
                    self.MatrizActividades[0].getTj0()+self.MatrizActividades[i].getDij())

            elif len(self.MatrizActividades[i].getlistaPredecesores()) == 1:

                posicion = 0

                posicion = self.obtenerPosicion(
                    self.MatrizActividades[i].getlistaPredecesores()[0])  # "A"

                self.MatrizActividades[i].setTi0(
                    self.MatrizActividades[posicion].getTj0())
                self.MatrizActividades[i].setTj0(
                    self.MatrizActividades[posicion].getTj0()+self.MatrizActividades[i].getDij())

                self.MatrizActividades[posicion].setlistaSucesores(
                    self.MatrizActividades[i].getIdentificador())  # Guardar sucesor

            else:

                mayor_auxiliar = 0
                mayor = 0
                posicionMayor = 0
                for listP in range(0, len(self.MatrizActividades[i].getlistaPredecesores()), 1):
                    posicion = 0

                    posicion = self.obtenerPosicion(
                        self.MatrizActividades[i].getlistaPredecesores()[listP])

                    mayor_auxiliar = self.MatrizActividades[posicion].getTi0(
                    )+self.MatrizActividades[posicion].getDij()

                    if mayor_auxiliar >= mayor:
                        mayor = mayor_auxiliar
                        posicionMayor = posicion

                    self.MatrizActividades[posicion].setlistaSucesores(
                        self.MatrizActividades[i].getIdentificador())  # Guardar sucesor

                self.MatrizActividades[i].setTi0(
                    self.MatrizActividades[posicionMayor].getTj0())
                self.MatrizActividades[i].setTj0(
                    self.MatrizActividades[posicionMayor].getTj0()+self.MatrizActividades[i].getDij())

    # Vuelta en la busqueda de  Ti1 y Tj1
    def vuelta(self):

        self.MatrizActividades[len(self.MatrizActividades)-1].setTi1(
            self.MatrizActividades[len(self.MatrizActividades)-1].getTi0())  # 26 26
        self.MatrizActividades[len(self.MatrizActividades)-1].setTj1(
            self.MatrizActividades[len(self.MatrizActividades)-1].getTj0())  # 26 26

        for i in range((len(self.MatrizActividades)-2), 0, -1):

            if len(self.MatrizActividades[i].getlistaSucesores()) == 1:

                posicion = self.obtenerPosicion(
                    self.MatrizActividades[i].getlistaSucesores()[0])

                self.MatrizActividades[i].setTi1(
                    self.MatrizActividades[posicion].getTi1()-self.MatrizActividades[i].getDij())
                self.MatrizActividades[i].setTj1(
                    self.MatrizActividades[posicion].getTi1())

            else:

                menor_auxiliar = 0
                menor = 0
                posicionMenor = 0
                for listP in range(0, len(self.MatrizActividades[i].getlistaSucesores()), 1):
                    posicion = 0

                    posicion = self.obtenerPosicion(
                        self.MatrizActividades[i].getlistaSucesores()[listP])

                    menor_auxiliar = self.MatrizActividades[posicion].getTi1(
                    )-self.MatrizActividades[i].getDij()

                    if listP == 0:
                        menor = menor_auxiliar
                        posicionMenor = posicion
                    if menor_auxiliar <= menor:
                        menor = menor_auxiliar
                        posicionMenor = posicion

                self.MatrizActividades[i].setTi1(
                    self.MatrizActividades[posicionMenor].getTi1()-self.MatrizActividades[i].getDij())
                self.MatrizActividades[i].setTj1(
                    self.MatrizActividades[posicionMenor].getTi1())

    # Metodo para obtener la posicion de un predecesor en un arreglo
    def obtenerPosicion(self, identificador):
        iterador = 0
        posicion = 0
        while(iterador < len(self.MatrizActividades)):
            if self.MatrizActividades[iterador].getIdentificador() == identificador:
                posicion = iterador
                break
            iterador += 1
        return posicion

    # Metodo para obtener el predecesor del ultimo nodo
    def obtenerPredecesoresDelFin(self):
        arregloIdentificador = []
        predecesores = ""
        predecesoresFin = ""
        for i in range(1, len(self.MatrizActividades)-1, 1):
            arregloIdentificador.append(
                self.MatrizActividades[i].getIdentificador())
            predecesores += self.MatrizActividades[i].getlistaPredecesores(
            ).__str__()

        for j in range(0, len(arregloIdentificador), 1):
            if predecesores.find(arregloIdentificador[j]) == -1:
                predecesoresFin += arregloIdentificador[j]+","

        return predecesoresFin

    # Verifica que los datos ingresados sean validos antes de hacer el calculo
    def verificarDatosIngresados(self):

        datosCorrecto = True
        dato = 0
        predecesor = ""
        salidadelciclo = False
        if self.numActividades == 0:  # no se creo la tablas
            datosCorrecto = False
        else:
            for i in range(0, self.numActividades, 1):
                predecesor = str(self.tablaActividades.item(i, 2).text())
                arregloPredecesores = []
                if not predecesor == "N/A":
                    arregloPredecesores = predecesor.split(",")

                if len(predecesor) == 0:  # validar predecesores
                    self.show_popup_InformacionP("Dato inválido", "Predesor vacio en actividad " +
                                                 self.listadeActividades[i]+"\nPara actividades sin predecesores se debe ingresar N/A")
                    datosCorrecto = False
                    break

                else:
                    for ar in range(len(arregloPredecesores)):
                        try:
                            # el predecesor se encuentra en la lista en una posicion pero en una posicion mas adelante o igual
                            if (self.listadeActividades.index(arregloPredecesores[ar])) >= i:
                                self.show_popup_InformacionP("Dato inválido", "Predecesores de la actividad " +
                                                             self.tablaActividades.item(i, 0).text()+" no se encuentran en la lista antes de la actividad")
                                salidadelciclo = True
                                break
                        except ValueError:
                            self.show_popup_InformacionP(
                                "Dato inválido", "Predecesores de la actividad "+self.tablaActividades.item(i, 0).text()+" no están en la lista")
                            salidadelciclo = True
                            break

                    if salidadelciclo:
                        datosCorrecto = False
                        break
        if datosCorrecto:
            for i in range(0, self.numActividades, 1):
                for j in range(3, 6, 1):
                    try:
                        dato = int(self.tablaActividades.item(i, j).text())

                    except ValueError:
                        self.show_popup_InformacionP("Dato inválido", str(
                            self.tablaActividades.item(i, j).text())+" no es permitido en la columna "+str(self.listColumnas[j])+"\nIngrese números enteros")
                        datosCorrecto = False
                        break
                if not datosCorrecto:
                    break

        return datosCorrecto

    # pintar filas con margen total = cero
    def pintarRutasCriticas(self):
        for row in range(self.numActividades):
            if int(self.tablaActividades.item(row, 12).text()) == 0:
                for col in range(18):
                    item1 = QTableWidgetItem(
                        self.tablaActividades.item(row, col).text())
                    item1.setBackground(QtGui.QColor(244, 67, 54))
                    self.tablaActividades.setItem(row, col, item1)

        self.tablaActividades.resizeColumnsToContents()

    # mostrar mensaje
    def show_popup_InformacionP(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        x = msg.exec_()

    # ocultar y mostrar Etiquetas
    def mostrarEtiquetas(self, estado):
        self.etiquetaFechaFin.setText("")
        self.etiquetaFechaInicio.setText("")
        self.etiquetaFindes.setText("")
        self.ui.lblnumActividades_2.setVisible(estado)
        self.ui.lblnumActividades_3.setVisible(estado)

    # mostrar resultados
    def mostrarResultados(self):
        self.mostrarEtiquetas(True)
        self.etiquetaFechaInicio.setText(
            self.tablaActividades.item(0, 14).text())
        self.etiquetaFechaFin.setText(
            self.tablaActividades.item(self.numActividades-1, 17).text())
        mensajeResultado = ""
        mensajeResultado = "Para terminar el proyecto se estiman " + \
            self.tablaActividades.item(
                self.numActividades-1, 11).text() + " dias sin tomar en cuenta "
        diccionarioDias = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miércoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'
        }
        for nolab in range(len(self.diasNoLab)):
            separacion = ""
            if nolab == len(self.diasNoLab)-1:
                separacion = " y "
            elif not nolab == 0:
                separacion = ", "
            mensajeResultado += separacion + \
                diccionarioDias[self.diasNoLab[nolab]]

        self.etiquetaFindes.setText(mensajeResultado)

    # metodo para obtener Fechas
    def obtenerFechas(self):
        self.fechInicio = self.dialogFecha.ui.calendarWidget.selectedDate().toPyDate()
        self.getDiasNoLaborables()
        self.generadorDeFechas(self.numActividades)
        self.pintarRutasCriticas()
        # mostrar etiquetas con datos de fecha inicial y fecha final
        self.mostrarResultados()

    # Método para obtener dias no laborables
    def getDiasNoLaborables(self):
        self.diasNoLab = []

        if(self.dialogFecha.ui.checkLunes.isChecked()):
            dia = "Monday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkMartes.isChecked()):
            dia = "Tuesday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkMier.isChecked()):
            dia = "Wednesday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkJueves.isChecked()):
            dia = "Thursday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkViernes.isChecked()):
            dia = "Friday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkSabado.isChecked()):
            dia = "Saturday"
            self.diasNoLab.append(dia)

        if(self.dialogFecha.ui.checkDom.isChecked()):
            dia = "Sunday"
            self.diasNoLab.append(dia)

    # calcular las fechas
    def calcularFecha(self, tiempo):
        self.fechaLab = self.fechInicio
        i = 0
        while(i < tiempo):
            if(i == 0):
                dia = self.fechInicio + timedelta(days=i)
            else:
                self.fechaLab = self.fechaLab + timedelta(days=1)
                diaActual = self.fechaLab.strftime("%A")
                if(diaActual in self.diasNoLab):
                    i -= 1

            if(tiempo == 1):
                self.fechaLab = self.fechaLab + timedelta(days=1)
                diaActual = self.fechaLab.strftime("%A")
                if(diaActual in self.diasNoLab):
                    i -= 1
            i += 1

        return self.fechaLab

    # Metodo para insertar fechas en la tabla
    def generadorDeFechas(self, filas):
        # ciclo para mostrar en la tabla Dij, Oij, Ti0, Tj0, Ti1, Tj1, Mtij, Mlij
        for tabrow in range(0, self.numActividades, 1):

            # Fecha de Inicio temprano
            fechaTi0 = self.calcularFecha(
                int(self.MatrizActividades[tabrow+1].getTi0()))
            itemFechaTi0 = QTableWidgetItem(fechaTi0.strftime("%d/%m/%Y"))
            self.tablaActividades.setItem(tabrow, 14, itemFechaTi0)

            # Fecha de Inicio tardio
            fechaTi1 = self.calcularFecha(
                int(self.MatrizActividades[tabrow+1].getTi1()))
            itemFechaTi1 = QTableWidgetItem(fechaTi1.strftime("%d/%m/%Y"))
            self.tablaActividades.setItem(tabrow, 15, itemFechaTi1)

            # Fecha de Fin Temprano
            fechaTj0 = self.calcularFecha(
                int(self.MatrizActividades[tabrow+1].getTj0()))
            itemFechaTj0 = QTableWidgetItem(fechaTj0.strftime("%d/%m/%Y"))
            self.tablaActividades.setItem(tabrow, 16, itemFechaTj0)

            # Fecha de fin tardio
            fechaTj1 = self.calcularFecha(
                int(self.MatrizActividades[tabrow+1].getTj1()))
            itemFechaTj1 = QTableWidgetItem(fechaTj1.strftime("%d/%m/%Y"))
            self.tablaActividades.setItem(tabrow, 17, itemFechaTj1)

    def resolver_ruta(self, ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

    def rutaParaCSS(self, rutaFondo):
        nuevaRutaiM = ""
        for iRu in range(0, len(rutaFondo), 1):
            if ord(rutaFondo[iRu]) == 92:
                nuevaRutaiM += str("/")
            else:
                nuevaRutaiM += rutaFondo[iRu]
        return nuevaRutaiM


class DialogFecha(QDialog):
    def __init__(self, *args, **kwargs):
        super(DialogFecha, self).__init__(*args, **kwargs)
        self.ui = Ui_modalFecha()
        self.ui.setupUi(self)
        self.setWindowTitle("Fecha de incio del proyecto")
        self.setStyle(QStyleFactory.create('Fusion'))
        self.ui.btnAceptarFecha.clicked.connect(self.close)
