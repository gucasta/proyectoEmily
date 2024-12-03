# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tratamientoFormulario.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

import sqlite3

class Ui_TratamientoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"QTextEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}")
        self.line_2 = QFrame(self)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 60, 551, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 321, 35))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
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

        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 111, 56))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_8)

        self.fecha_dateEdit = QDateEdit(self.layoutWidget)
        self.fecha_dateEdit.setObjectName(u"fecha_dateEdit")
        self.fecha_dateEdit.setMinimumSize(QSize(0, 31))
        self.fecha_dateEdit.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout_2.addWidget(self.fecha_dateEdit)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(140, 80, 142, 59))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 21))
        self.label_4.setMaximumSize(QSize(16777215, 21))
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.duracion_lineEdit = QLineEdit(self.layoutWidget1)
        self.duracion_lineEdit.setObjectName(u"duracion_lineEdit")
        self.duracion_lineEdit.setMinimumSize(QSize(0, 28))
        self.duracion_lineEdit.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout.addWidget(self.duracion_lineEdit)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 160, 511, 311))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.indicaciones_textEdit = QTextEdit(self.layoutWidget2)
        self.indicaciones_textEdit.setObjectName(u"indicaciones_textEdit")

        self.verticalLayout_3.addWidget(self.indicaciones_textEdit)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.observaciones_textEdit = QTextEdit(self.layoutWidget2)
        self.observaciones_textEdit.setObjectName(u"observaciones_textEdit")

        self.verticalLayout_3.addWidget(self.observaciones_textEdit)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, TratamientoDialog):
        TratamientoDialog.setWindowTitle(QCoreApplication.translate("TratamientoDialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("TratamientoDialog", u"Registrar Tratamiento", None))
        self.registrar_btn.setText(QCoreApplication.translate("TratamientoDialog", u"Guardar", None))
        self.cancelar_btn.setText(QCoreApplication.translate("TratamientoDialog", u"Cancelar", None))
        self.label_8.setText(QCoreApplication.translate("TratamientoDialog", u"Fecha", None))
        self.label_4.setText(QCoreApplication.translate("TratamientoDialog", u"Duraci\u00f3n (d\u00edas)", None))
        self.label_2.setText(QCoreApplication.translate("TratamientoDialog", u"Indicaciones", None))
        self.label_5.setText(QCoreApplication.translate("TratamientoDialog", u"Observaciones", None))
    # retranslateUi

 # Se registra nuevo tratamiento cuando se presiona un boton
        self.registrar_btn.clicked.connect(self.registrar_tratamiento)
        self.cancelar_btn.clicked.connect(self.close)

    # Creamos una conexion a sqlite3
    def crear_conexion(self):
        
        con = sqlite3.connect("hospital.db")
        
        self.mydb = con
        
        return self.mydb
    
    # Registramos un nuevo tratamiento
    def insertar_nuevo_tratamiento(self):
        try:
            con = self.crear_conexion()
            cur = con.cursor()
            
            fecha = self.transformarFecha()
            duracion = self.duracion_lineEdit.text()
            indicaciones = self.indicaciones_textEdit.text()
            observaciones = self.observaciones_textEdit.text()
            
            # Insertamos en la tabla de sqlite3
            consulta_insertar_tratamiento = f"""
                INSERT INTO tratamiento (
                    fecha,
                    duracion,
                    indicaciones,
                    observaciones
                ) VALUES (
                    '{fecha}',
                    '{duracion}',
                    '{indicaciones}',
                    '{observaciones}'
                )
            """
            
            cur.execute(consulta_insertar_tratamiento)
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
        
    def registrar_tratamiento(self):
        self.insertar_nuevo_tratamiento()
        self.accept()