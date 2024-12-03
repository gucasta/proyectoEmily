# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnosticoFormulario.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

import sqlite3

class Ui_DiagnosticoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 321, 35))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(330, 520, 201, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.registrar_btn = QPushButton(self.layoutWidget_2)
        self.registrar_btn.setObjectName(u"registrar_btn")
        self.registrar_btn.setMinimumSize(QSize(0, 41))
        self.registrar_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.registrar_btn)

        self.cancelar_btn = QPushButton(self.layoutWidget_2)
        self.cancelar_btn.setObjectName(u"cancelar_btn")
        self.cancelar_btn.setMinimumSize(QSize(0, 41))
        self.cancelar_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.cancelar_btn)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 531, 431))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.rx_textEdit = QTextEdit(self.widget)
        self.rx_textEdit.setObjectName(u"rx_textEdit")

        self.verticalLayout.addWidget(self.rx_textEdit)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, DiagnosticoDialog):
        DiagnosticoDialog.setWindowTitle(QCoreApplication.translate("DiagnosticoDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DiagnosticoDialog", u"Registrar Diagn\u00f3stico", None))
        self.registrar_btn.setText(QCoreApplication.translate("DiagnosticoDialog", u"Guardar", None))
        self.cancelar_btn.setText(QCoreApplication.translate("DiagnosticoDialog", u"Cancelar", None))
        self.label_2.setText(QCoreApplication.translate("DiagnosticoDialog", u"Rx", None))
    # retranslateUi

# Se registra nuevo diagnostico cuando se presiona un boton
        self.registrar_btn.clicked.connect(self.registrar_diagnostico)
        self.cancelar_btn.clicked.connect(self.close)

    # Creamos una conexion a sqlite3
    def crear_conexion(self):
        
        con = sqlite3.connect("hospital.db")
        
        self.mydb = con
        
        return self.mydb
    
    # Registramos un nuevo paciente
    def ingresar_nuevo_diagnostico(self):
        try:
            con = self.crear_conexion()
            cur = con.cursor()
            
            diagnostico = self.rx_textEdit.text()
            
            # Insertamos en la tabla diagnostico de sqlite3
            consulta_insertar_diagnostico = f"""
                INSERT INTO rx (
                    fecha,
                    poliza,
                    nombre,
                    apellido,
                    diagnostico
                ) VALUES (
                    '{fecha}',
                    '{poliza}',
                    '{nombre}',
                    '{apellido}',
                    '{diagnostico}'
                )
            """
            
            cur.execute(consulta_insertar_diagnostico)
            self.mostrar_mensaje_insertar()
            con.commit()
            con.close()
        except sqlite3.Error as err:
            print(f"Error: {err}")

    def transformarFecha(self):
        # Convertimos QDate a un string en el formato YYYY-MM-DD
        fecha_seleccionada = self.fecha_dateEdit.date()
        self.fecha_string = fecha_seleccionada.toString(Qt.ISODate)
        
        return self.fecha_string
    
    def mostrar_mensaje(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Registrado")
        msg_box.setText(self.nombre_lineEdit.text() + " ha sido ingresado su diagnostico")
        msg_box.exec()
        
    def registrar_diagnostico(self):
        self.insertar_nuevo_diagnostico()
        self.accept()

#duda en arrastrar los datos del paciente a esa tabla