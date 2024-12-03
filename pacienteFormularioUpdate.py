# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pacienteFormularioUpdate.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QMessageBox,
    QWidget)

import sqlite3

class Ui_PacienteDialogUpdate(QDialog):
    
    # Definimos una señal como una variable de clase
    datos_editados = Signal()
    
    def __init__(self, row_index, row_data):
        super().__init__()
        
        # guardamos el row_index y el row_data como variables de instancia
        self.row_index = row_index
        self.row_data = row_data
        
        self.paciente_info = self.paciente_seleccionado()[0]
        
        self.paciente_fecha = self.paciente_info[0]
        self.paciente_poliza = self.paciente_info[1]
        self.paciente_nombre = self.paciente_info[2]
        self.paciente_apellidos = self.paciente_info[3]
        self.paciente_edad = self.paciente_info[4]
        self.paciente_genero = self.paciente_info[5]
        
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
        self.update_registrar_btn = QPushButton(self.layoutWidget_2)
        self.update_registrar_btn.setObjectName(u"update_registrar_btn")
        self.update_registrar_btn.setMinimumSize(QSize(0, 41))
        self.update_registrar_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.update_registrar_btn)

        self.update_cancelar_btn = QPushButton(self.layoutWidget_2)
        self.update_cancelar_btn.setObjectName(u"update_cancelar_btn")
        self.update_cancelar_btn.setMinimumSize(QSize(0, 41))
        self.update_cancelar_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.update_cancelar_btn)

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


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("PacienteDialog", u"Editar Paciente", None))
        self.label.setText(QCoreApplication.translate("PacienteDialog", u"Editar Información Paciente", None))
        self.label.setFixedSize(380, 31) # modificamos dimensiones del titulo para que se muestre
        self.update_registrar_btn.setText(QCoreApplication.translate("PacienteDialog", u"Editar", None))
        self.update_cancelar_btn.setText(QCoreApplication.translate("PacienteDialog", u"Cancelar", None))
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

        # Convertimos la cadena a QDate para QDateEdit
        fecha_objeto = QDate.fromString(self.paciente_fecha, "yyyy-MM-dd")
        
        self.fecha_dateEdit.setDate(fecha_objeto)
        self.poliza_lineEdit.setText(str(self.poliza_paciente))
        self.nombre_lineEdit.setText(str(self.paciente_nombre))
        self.apellido_lineEdit.setText(str(self.paciente_apellidos))
        self.edad_lineEdit.setText(str(self.paciente_edad))
        self.comboBox.setCurrentText(str(self.paciente_genero))
        
        self.update_registrar_btn.clicked.connect(self.editar_datos)
        self.update_cancelar_btn.clicked.connect(self.close)
    
    # Funcion o metodo para crear BD
    def crear_conexion(self):
        con = sqlite3.connect("hospital.db")
    
        self.mydb = con
    
        return self.mydb

    def paciente_seleccionado(self):
        
        self.cur = self.crear_conexion().cursor()
        
        # obtenemos las variables del paciente de la tabla
        self.poliza_paciente = self.row_data[1]
        
        consulta = f"SELECT fecha, poliza, nombre, apellidos, edad, genero FROM pacientes WHERE poliza = '{self.poliza_paciente}'"
        
        self.cur.execute(consulta)
        
        registros = self.cur.fetchall()
        
        self.mydb.commit()
        self.mydb.close()
        return registros
    
    def editar_datos(self):
        try:
            con = self.crear_conexion()
            
            if con is None:
                return
            
            cur = con.cursor()
            
            # Convertimos la fecha a formato SQL
            fecha = self.handleDateChange()
            
            consulta_editar = f"""
                UPDATE pacientes
                SET
                    fecha='{fecha}',
                    poliza='{self.poliza_lineEdit.text()}',
                    nombre='{self.nombre_lineEdit.text()}',
                    apellidos='{self.apellido_lineEdit.text()}',
                    edad='{self.edad_lineEdit.text()}',
                    genero='{self.comboBox.currentText()}'
                WHERE
                    poliza='{self.poliza_paciente}'
            """
            
            cur.execute(consulta_editar)
            con.commit()
            self.mostrar_mensaje_editar()
            cur.close()
            con.close()
            self.close()
            
            # Emitimos la señal
            self.datos_editados.emit()
        
        except sqlite3.Error as err:
            print(f"Error: {err}")
            
    def handleDateChange(self):
        
        # Convert QDate to a string in the format YYYY-MM-DD
        selected_date = self.fecha_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)
        
        return self.date_string
    
    def mostrar_mensaje_editar(self):
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Editado")
        msg_box.setText("la información del paciente" + self.paciente_nombre + " ha sido editada")
        msg_box.exec()