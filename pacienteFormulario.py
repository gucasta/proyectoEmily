# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pacienteFormulario.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

import sqlite3

class Ui_PacienteDialog(QDialog):
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
"\n"
"QComboBox{\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(19, 16, 321, 35))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(329, 520, 201, 43))
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
        self.layoutWidget.setGeometry(QRect(10, 81, 521, 411))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 21))
        self.label_3.setMaximumSize(QSize(16777215, 21))
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.poliza_lineEdit = QLineEdit(self.layoutWidget)
        self.poliza_lineEdit.setObjectName(u"poliza_lineEdit")
        self.poliza_lineEdit.setMinimumSize(QSize(0, 28))
        self.poliza_lineEdit.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_3.addWidget(self.poliza_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.nombre_lineEdit = QLineEdit(self.layoutWidget)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setMinimumSize(QSize(0, 31))
        self.nombre_lineEdit.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout.addWidget(self.nombre_lineEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_4)

        self.apellido_lineEdit = QLineEdit(self.layoutWidget)
        self.apellido_lineEdit.setObjectName(u"apellido_lineEdit")
        self.apellido_lineEdit.setMinimumSize(QSize(0, 31))
        self.apellido_lineEdit.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout_4.addWidget(self.apellido_lineEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edad_lineEdit = QLineEdit(self.layoutWidget)
        self.edad_lineEdit.setObjectName(u"edad_lineEdit")
        self.edad_lineEdit.setMinimumSize(QSize(181, 31))
        self.edad_lineEdit.setMaximumSize(QSize(181, 31))

        self.horizontalLayout_3.addWidget(self.edad_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(328, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(181, 0))
        self.comboBox.setMaximumSize(QSize(181, 16777215))
        font2 = QFont()
        self.comboBox.setFont(font2)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(338, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, PacienteDialog):
        PacienteDialog.setWindowTitle(QCoreApplication.translate("PacienteDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PacienteDialog", u"Registrar Paciente", None))
        self.registrar_btn.setText(QCoreApplication.translate("PacienteDialog", u"Registrar", None))
        self.cancelar_btn.setText(QCoreApplication.translate("PacienteDialog", u"Cancelar", None))
        self.label_8.setText(QCoreApplication.translate("PacienteDialog", u"Fecha de Ingreso", None))
        self.label_3.setText(QCoreApplication.translate("PacienteDialog", u"Poliza", None))
        self.label_2.setText(QCoreApplication.translate("PacienteDialog", u"Nombre", None))
        self.label_4.setText(QCoreApplication.translate("PacienteDialog", u"Apellido", None))
        self.label_5.setText(QCoreApplication.translate("PacienteDialog", u"Edad", None))
        self.label_6.setText(QCoreApplication.translate("PacienteDialog", u"Genero", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PacienteDialog", u"SELECCIONA GENERO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PacienteDialog", u"Masculino", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PacienteDialog", u"Femenino", None))
    # retranslateUi
    
        # Se registra nuevo paciente cuando se presiona un boton
        self.registrar_btn.clicked.connect(self.registrar_paciente)
        self.cancelar_btn.clicked.connect(self.close)

    # Creamos una conexion a sqlite3
    def crear_conexion(self):
        
        con = sqlite3.connect("hospital.db")
        
        self.mydb = con
        
        return self.mydb
    
    # Registramos un nuevo paciente
    def insertar_nuevo_paciente(self):
        try:
            con = self.crear_conexion()
            cur = con.cursor()
            
            fecha = self.transformarFecha()
            poliza = self.poliza_lineEdit.text()
            nombre = self.nombre_lineEdit.text()
            apellidos = self.apellido_lineEdit.text()
            edad = self.edad_lineEdit.text()
            genero = self.comboBox.currentText()
            
            # Insertamos en la tabla paciente de sqlite3
            consulta_insertar_paciente = f"""
                INSERT INTO pacientes (
                    fecha,
                    poliza,
                    nombre,
                    apellidos,
                    edad,
                    genero
                ) VALUES (
                    '{fecha}',
                    '{poliza}',
                    '{nombre}',
                    '{apellidos}',
                    '{edad}',
                    '{genero}'
                )
            """
            
            cur.execute(consulta_insertar_paciente)
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
    
    def mostrar_mensaje_insertar(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Registrado")
        msg_box.setText(self.nombre_lineEdit.text() + " ha sido registrado")
        msg_box.exec()
        
    def registrar_paciente(self):
        self.insertar_nuevo_paciente()
        self.accept()