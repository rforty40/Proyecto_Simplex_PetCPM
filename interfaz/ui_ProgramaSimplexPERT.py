# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramaSimplexPERTurrkgv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1024, 720))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background: #FEFEFE; font-size: 14px; font-weight: bold; font-family: Roboto;\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionPrueba = QAction(MainWindow)
        self.actionPrueba.setObjectName(u"actionPrueba")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"padding:0px;")
        self.framePert = QFrame(self.centralwidget)
        self.framePert.setObjectName(u"framePert")
        self.framePert.setGeometry(QRect(0, 0, 1341, 821))
        self.framePert.setFrameShape(QFrame.StyledPanel)
        self.framePert.setFrameShadow(QFrame.Raised)
        self.lblnumActividades = QLabel(self.framePert)
        self.lblnumActividades.setObjectName(u"lblnumActividades")
        self.lblnumActividades.setGeometry(QRect(20, 40, 251, 31))
        self.lblnumActividades.setStyleSheet(u"font-size: 14px; font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"")
        self.lblFondoPert = QLabel(self.framePert)
        self.lblFondoPert.setObjectName(u"lblFondoPert")
        self.lblFondoPert.setGeometry(QRect(0, 0, 1031, 731))
        self.lblFondoPert.setStyleSheet(u"background-image: url(\"interfaz/img/fondoPert.png\");")
        self.btnGenerarTbl = QPushButton(self.framePert)
        self.btnGenerarTbl.setObjectName(u"btnGenerarTbl")
        self.btnGenerarTbl.setGeometry(QRect(348, 40, 101, 31))
        self.btnGenerarTbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGenerarTbl.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.spinNumActividades = QSpinBox(self.framePert)
        self.spinNumActividades.setObjectName(u"spinNumActividades")
        self.spinNumActividades.setGeometry(QRect(284, 40, 51, 31))
        self.spinNumActividades.setStyleSheet(u"font-size: 14px; \n"
" font-weight: bold; font-family: Kameron;")
        self.tblActividades = QTableWidget(self.framePert)
        self.tblActividades.setObjectName(u"tblActividades")
        self.tblActividades.setGeometry(QRect(20, 110, 981, 381))
        self.tblActividades.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgb(0,0,0);\n"
"background: rgba(255, 255,255,1);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tblActividades.horizontalHeader().setVisible(True)
        self.tblActividades.horizontalHeader().setDefaultSectionSize(50)
        self.tblActividades.verticalHeader().setVisible(False)
        self.btnCalcularPert = QPushButton(self.framePert)
        self.btnCalcularPert.setObjectName(u"btnCalcularPert")
        self.btnCalcularPert.setGeometry(QRect(790, 40, 101, 31))
        self.btnCalcularPert.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"border-radius: 10px;\n"
"")
        self.btnNuevoPert = QPushButton(self.framePert)
        self.btnNuevoPert.setObjectName(u"btnNuevoPert")
        self.btnNuevoPert.setGeometry(QRect(900, 40, 101, 31))
        self.btnNuevoPert.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.lblnumActividades_2 = QLabel(self.framePert)
        self.lblnumActividades_2.setObjectName(u"lblnumActividades_2")
        self.lblnumActividades_2.setGeometry(QRect(20, 519, 141, 31))
        self.lblnumActividades_2.setStyleSheet(u"font-size: 14px; font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"")
        self.lblnumActividades_3 = QLabel(self.framePert)
        self.lblnumActividades_3.setObjectName(u"lblnumActividades_3")
        self.lblnumActividades_3.setGeometry(QRect(330, 520, 111, 31))
        self.lblnumActividades_3.setStyleSheet(u"font-size: 14px; font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"")
        self.lblFechaIncio = QLabel(self.framePert)
        self.lblFechaIncio.setObjectName(u"lblFechaIncio")
        self.lblFechaIncio.setGeometry(QRect(170, 520, 141, 31))
        self.lblFechaIncio.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.lblFechaFin = QLabel(self.framePert)
        self.lblFechaFin.setObjectName(u"lblFechaFin")
        self.lblFechaFin.setGeometry(QRect(460, 520, 131, 31))
        self.lblFechaFin.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.lblFindes = QLabel(self.framePert)
        self.lblFindes.setObjectName(u"lblFindes")
        self.lblFindes.setGeometry(QRect(20, 560, 971, 81))
        self.lblFindes.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.lblFindes.setWordWrap(True)
        self.lblFondoPert.raise_()
        self.lblnumActividades.raise_()
        self.btnGenerarTbl.raise_()
        self.spinNumActividades.raise_()
        self.tblActividades.raise_()
        self.btnCalcularPert.raise_()
        self.btnNuevoPert.raise_()
        self.lblnumActividades_2.raise_()
        self.lblnumActividades_3.raise_()
        self.lblFechaIncio.raise_()
        self.lblFechaFin.raise_()
        self.lblFindes.raise_()
        self.frameSimplex = QFrame(self.centralwidget)
        self.frameSimplex.setObjectName(u"frameSimplex")
        self.frameSimplex.setGeometry(QRect(0, 0, 1031, 691))
        self.frameSimplex.setFrameShape(QFrame.StyledPanel)
        self.frameSimplex.setFrameShadow(QFrame.Raised)
        self.lblFondo = QLabel(self.frameSimplex)
        self.lblFondo.setObjectName(u"lblFondo")
        self.lblFondo.setGeometry(QRect(-80, 0, 1111, 691))
        self.lblFondo.setStyleSheet(u"background-image: url(\"interfaz/img/atardecer2.jpg\");")
        self.txtVar = QLineEdit(self.frameSimplex)
        self.txtVar.setObjectName(u"txtVar")
        self.txtVar.setGeometry(QRect(253, 80, 41, 31))
        self.txtVar.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;")
        self.txtRestr = QLineEdit(self.frameSimplex)
        self.txtRestr.setObjectName(u"txtRestr")
        self.txtRestr.setGeometry(QRect(253, 120, 41, 31))
        self.txtRestr.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;")
        self.cmbMetodo = QComboBox(self.frameSimplex)
        self.cmbMetodo.setObjectName(u"cmbMetodo")
        self.cmbMetodo.setGeometry(QRect(10, 30, 161, 31))
        self.cmbMetodo.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"")
        self.lblVarriables = QLabel(self.frameSimplex)
        self.lblVarriables.setObjectName(u"lblVarriables")
        self.lblVarriables.setGeometry(QRect(10, 80, 191, 31))
        self.lblVarriables.setStyleSheet(u"  background: rgba(255, 255,255,0);\n"
"color: rgba(255,255,255);\n"
"font-size: 12px; ")
        self.btnGenerar = QPushButton(self.frameSimplex)
        self.btnGenerar.setObjectName(u"btnGenerar")
        self.btnGenerar.setGeometry(QRect(194, 30, 101, 31))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.lblRestricciones = QLabel(self.frameSimplex)
        self.lblRestricciones.setObjectName(u"lblRestricciones")
        self.lblRestricciones.setGeometry(QRect(10, 120, 201, 31))
        self.lblRestricciones.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: rgba(255,255,255);\n"
"font-size: 12px; ")
        self.panelVarRest = QFrame(self.frameSimplex)
        self.panelVarRest.setObjectName(u"panelVarRest")
        self.panelVarRest.setGeometry(QRect(10, 180, 311, 471))
        self.panelVarRest.setCursor(QCursor(Qt.PointingHandCursor))
        self.panelVarRest.setStyleSheet(u"background: rgba(255, 255,255,0);\n"
"self.panelVarRest.setStyleSheet(\"border: none\")\n"
"")
        self.panelVarRest.setFrameShape(QFrame.NoFrame)
        self.panelVarRest.setFrameShadow(QFrame.Raised)
        self.panelVarRest.setLineWidth(0)
        self.cmbObjetivo = QComboBox(self.panelVarRest)
        self.cmbObjetivo.setObjectName(u"cmbObjetivo")
        self.cmbObjetivo.setGeometry(QRect(60, 10, 141, 31))
        self.cmbObjetivo.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"")
        self.tblVariables = QTableWidget(self.panelVarRest)
        self.tblVariables.setObjectName(u"tblVariables")
        self.tblVariables.setGeometry(QRect(10, 90, 271, 61))
        self.tblVariables.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgba(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")\n"
"")
        self.tblVariables.horizontalHeader().setVisible(True)
        self.tblVariables.horizontalHeader().setDefaultSectionSize(50)
        self.tblVariables.verticalHeader().setVisible(False)
        self.tblRestricciones = QTableWidget(self.panelVarRest)
        self.tblRestricciones.setObjectName(u"tblRestricciones")
        self.tblRestricciones.setGeometry(QRect(10, 200, 271, 171))
        self.tblRestricciones.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgba(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tblRestricciones.horizontalHeader().setVisible(True)
        self.tblRestricciones.horizontalHeader().setDefaultSectionSize(50)
        self.tblRestricciones.verticalHeader().setVisible(False)
        self.label_3 = QLabel(self.panelVarRest)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 111, 30))
        self.label_3.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);\n"
"text-align: left;")
        self.label_4 = QLabel(self.panelVarRest)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 141, 16))
        self.label_4.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);\n"
"text-align: left;")
        self.btnCalcular = QPushButton(self.panelVarRest)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(90, 390, 101, 31))
        self.btnCalcular.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"border-radius: 10px;")
        self.lblFuncionObjetivo = QLabel(self.frameSimplex)
        self.lblFuncionObjetivo.setObjectName(u"lblFuncionObjetivo")
        self.lblFuncionObjetivo.setGeometry(QRect(450, 30, 531, 31))
        self.lblFuncionObjetivo.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);")
        self.lblFunObj = QLabel(self.frameSimplex)
        self.lblFunObj.setObjectName(u"lblFunObj")
        self.lblFunObj.setGeometry(QRect(340, 30, 111, 31))
        self.lblFunObj.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0)")
        self.panelTblU = QFrame(self.frameSimplex)
        self.panelTblU.setObjectName(u"panelTblU")
        self.panelTblU.setEnabled(True)
        self.panelTblU.setGeometry(QRect(340, 70, 671, 591))
        self.panelTblU.setStyleSheet(u"  background: rgba(255, 255,255,0);")
        self.panelTblU.setFrameShape(QFrame.NoFrame)
        self.panelTblU.setFrameShadow(QFrame.Raised)
        self.tbl_U = QTableWidget(self.panelTblU)
        self.tbl_U.setObjectName(u"tbl_U")
        self.tbl_U.setGeometry(QRect(10, 80, 651, 231))
        self.tbl_U.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgba(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"self.tbl_U.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tbl_U.setStyleSheet(\"border: none;\")\n"
"\n"
"")
        self.tbl_U.horizontalHeader().setVisible(False)
        self.tbl_U.horizontalHeader().setDefaultSectionSize(75)
        self.tbl_U.verticalHeader().setVisible(False)
        self.tblOperaciones = QTableWidget(self.panelTblU)
        self.tblOperaciones.setObjectName(u"tblOperaciones")
        self.tblOperaciones.setGeometry(QRect(10, 350, 651, 231))
        self.tblOperaciones.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgba(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"self.tblOperaciones.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblOperaciones.setStyleSheet(\"border: none;\")")
        self.tblOperaciones.horizontalHeader().setVisible(False)
        self.tblOperaciones.verticalHeader().setVisible(False)
        self.btnIteracion = QPushButton(self.panelTblU)
        self.btnIteracion.setObjectName(u"btnIteracion")
        self.btnIteracion.setGeometry(QRect(160, 20, 121, 31))
        self.btnIteracion.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.btnPdf = QPushButton(self.panelTblU)
        self.btnPdf.setObjectName(u"btnPdf")
        self.btnPdf.setGeometry(QRect(290, 21, 111, 31))
        self.btnPdf.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.lblIteracionTexto = QLabel(self.panelTblU)
        self.lblIteracionTexto.setObjectName(u"lblIteracionTexto")
        self.lblIteracionTexto.setGeometry(QRect(10, 20, 61, 31))
        self.lblIteracionTexto.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);")
        self.lblIteracion = QLabel(self.panelTblU)
        self.lblIteracion.setObjectName(u"lblIteracion")
        self.lblIteracion.setGeometry(QRect(80, 20, 55, 31))
        self.lblIteracion.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Kameron;\n"
"color: rgb(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"")
        self.label = QLabel(self.panelTblU)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(620, 54, 41, 20))
        self.label.setStyleSheet(u"\n"
"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);\n"
"text-align: left;")
        self.label_2 = QLabel(self.panelTblU)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 320, 121, 20))
        self.label_2.setStyleSheet(u"color: rgba(255,255,255);\n"
"font-size: 12px;   background: rgba(255, 255,255,0);\n"
"text-align: left;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        self.menuCalculadora_M_todo_Simplex = QMenu(self.menubar)
        self.menuCalculadora_M_todo_Simplex.setObjectName(u"menuCalculadora_M_todo_Simplex")
        self.menuProyecto_PERT_CMP = QMenu(self.menubar)
        self.menuProyecto_PERT_CMP.setObjectName(u"menuProyecto_PERT_CMP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCalculadora_M_todo_Simplex.menuAction())
        self.menubar.addAction(self.menuProyecto_PERT_CMP.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"INVESTIGACI\u00d3N OPERATIVA", None))
        self.actionPrueba.setText(QCoreApplication.translate("MainWindow", u"Prueba", None))
        self.lblnumActividades.setText(QCoreApplication.translate("MainWindow", u"Ingresar el n\u00famero de actividades:", None))
        self.lblFondoPert.setText("")
        self.btnGenerarTbl.setText(QCoreApplication.translate("MainWindow", u"Generar Tabla", None))
        self.btnCalcularPert.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.btnNuevoPert.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.lblnumActividades_2.setText(QCoreApplication.translate("MainWindow", u"Desde fecha inicio:", None))
        self.lblnumActividades_3.setText(QCoreApplication.translate("MainWindow", u"Hasta fecha fin:", None))
        self.lblFechaIncio.setText(QCoreApplication.translate("MainWindow", u"13/08/2021", None))
        self.lblFechaFin.setText(QCoreApplication.translate("MainWindow", u"15/09/2021", None))
        self.lblFindes.setText(QCoreApplication.translate("MainWindow", u"Pasaron X dias sin tomar en cuenta sabados y domingos", None))
        self.lblFondo.setText("")
        self.lblVarriables.setText(QCoreApplication.translate("MainWindow", u"Ingresar el n\u00famero de variables:", None))
        self.btnGenerar.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.lblRestricciones.setText(QCoreApplication.translate("MainWindow", u"Ingresar el n\u00famero de restricciones:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n Objetivo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Restricciones", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.lblFuncionObjetivo.setText("")
        self.lblFunObj.setText(QCoreApplication.translate("MainWindow", u"Funcion Objetivo: ", None))
        self.btnIteracion.setText(QCoreApplication.translate("MainWindow", u"Siguiente Iteraci\u00f3n", None))
        self.btnPdf.setText(QCoreApplication.translate("MainWindow", u"Generar PDF", None))
        self.lblIteracionTexto.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n: ", None))
        self.lblIteracion.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tabla U", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tabla de Inecuaciones", None))
        self.menuCalculadora_M_todo_Simplex.setTitle(QCoreApplication.translate("MainWindow", u"Calculadora M\u00e9todo Simplex y Big M", None))
        self.menuProyecto_PERT_CMP.setTitle(QCoreApplication.translate("MainWindow", u"Proyecto PERT-CMP", None))
    # retranslateUi




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())