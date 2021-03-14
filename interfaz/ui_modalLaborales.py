# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalLaboralestsGMwm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_modalFecha(object):
    def setupUi(self, modalFecha):
        if not modalFecha.objectName():
            modalFecha.setObjectName(u"modalFecha")
        modalFecha.resize(350, 501)
        modalFecha.setStyleSheet(u"border-color: rgb(255,255,255);\n"
"border-width: 7px;")
        self.lbl1 = QLabel(modalFecha)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(10, 10, 351, 31))
        self.lbl1.setStyleSheet(u"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 12px; ")
        self.lblFondoModal = QLabel(modalFecha)
        self.lblFondoModal.setObjectName(u"lblFondoModal")
        self.lblFondoModal.setGeometry(QRect(-10, -10, 381, 521))
        self.lblFondoModal.setStyleSheet(u"background-image: url(\"interfaz/img/fondoPert.png\");")
        self.calendarWidget = QCalendarWidget(modalFecha)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(9, 50, 331, 211))
        self.calendarWidget.setStyleSheet(u"font-size: 12px; ")
        self.grupoBotones = QGroupBox(modalFecha)
        self.grupoBotones.setObjectName(u"grupoBotones")
        self.grupoBotones.setGeometry(QRect(10, 280, 331, 151))
        self.grupoBotones.setStyleSheet(u"\n"
"color: #ffdf00;\n"
"font-size: 12px; ")
        self.checkLunes = QCheckBox(self.grupoBotones)
        self.checkLunes.setObjectName(u"checkLunes")
        self.checkLunes.setGeometry(QRect(20, 30, 81, 20))
        self.checkLunes.setStyleSheet(u"\n"
"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkMartes = QCheckBox(self.grupoBotones)
        self.checkMartes.setObjectName(u"checkMartes")
        self.checkMartes.setGeometry(QRect(20, 59, 81, 20))
        self.checkMartes.setStyleSheet(u"\n"
"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkMier = QCheckBox(self.grupoBotones)
        self.checkMier.setObjectName(u"checkMier")
        self.checkMier.setGeometry(QRect(20, 88, 101, 20))
        self.checkMier.setStyleSheet(u"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkSabado = QCheckBox(self.grupoBotones)
        self.checkSabado.setObjectName(u"checkSabado")
        self.checkSabado.setGeometry(QRect(137, 58, 91, 20))
        self.checkSabado.setStyleSheet(u"\n"
"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkViernes = QCheckBox(self.grupoBotones)
        self.checkViernes.setObjectName(u"checkViernes")
        self.checkViernes.setGeometry(QRect(137, 31, 91, 20))
        self.checkViernes.setStyleSheet(u"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkDom = QCheckBox(self.grupoBotones)
        self.checkDom.setObjectName(u"checkDom")
        self.checkDom.setGeometry(QRect(137, 88, 121, 20))
        self.checkDom.setStyleSheet(u"color: #ffffff;\n"
"font-size: 12px; ")
        self.checkJueves = QCheckBox(self.grupoBotones)
        self.checkJueves.setObjectName(u"checkJueves")
        self.checkJueves.setGeometry(QRect(20, 116, 91, 20))
        self.checkJueves.setStyleSheet(u"color: #ffffff;\n"
"font-size: 12px; ")
        self.btnAceptarFecha = QPushButton(modalFecha)
        self.btnAceptarFecha.setObjectName(u"btnAceptarFecha")
        self.btnAceptarFecha.setGeometry(QRect(126, 450, 91, 31))
        self.btnAceptarFecha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAceptarFecha.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgba(250,250,250);\n"
"border-radius: 10px;")
        self.lblFondoModal.raise_()
        self.lbl1.raise_()
        self.calendarWidget.raise_()
        self.grupoBotones.raise_()
        self.btnAceptarFecha.raise_()

        self.retranslateUi(modalFecha)

        QMetaObject.connectSlotsByName(modalFecha)
    # setupUi

    def retranslateUi(self, modalFecha):
        modalFecha.setWindowTitle(QCoreApplication.translate("modalFecha", u"D\u00edas Laborables", None))
        self.lbl1.setText(QCoreApplication.translate("modalFecha", u"Seleccione la fecha incial del proyecto:", None))
        self.lblFondoModal.setText("")
        self.grupoBotones.setTitle(QCoreApplication.translate("modalFecha", u"Seleccione los d\u00edas de la semana que no se trabajar\u00e1n:", None))
        self.checkLunes.setText(QCoreApplication.translate("modalFecha", u"Lunes", None))
        self.checkMartes.setText(QCoreApplication.translate("modalFecha", u"Martes", None))
        self.checkMier.setText(QCoreApplication.translate("modalFecha", u"Mi\u00e9rcoles", None))
        self.checkSabado.setText(QCoreApplication.translate("modalFecha", u"S\u00e1bado", None))
        self.checkViernes.setText(QCoreApplication.translate("modalFecha", u"Viernes", None))
        self.checkDom.setText(QCoreApplication.translate("modalFecha", u"Domingo", None))
        self.checkJueves.setText(QCoreApplication.translate("modalFecha", u"Jueves", None))
        self.btnAceptarFecha.setText(QCoreApplication.translate("modalFecha", u"Aceptar", None))
    # retranslateUi

