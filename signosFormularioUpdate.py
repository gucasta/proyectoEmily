# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signosFormularioUpdate.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
    QSizePolicy, QVBoxLayout, QWidget)

import sqlite3

class Ui_SignosDialogUpdate(QDialog):
    
    datos_editados = Signal()
    
    def __init__(self, row_index, row_data):
        super().__init__()
        
        self.row_index = row_index
        self.row_data = row_data
        
        self.signos_info = self.signos_seleccionado()[0]
        
        self.signos_id = self.signos_info[0]
        self.signos_peso = self.signos_info[1]
        self.signos_estatura = self.signos_info[2]
        self.signos_sistolica = self.signos_info[3]
        self.signos_diastolica = self.signos_info[4]
        self.signos_oxigenacion = self.signos_info[5]
        self.signos_temperatura = self.signos_info[6]
        self.signos_frecuencia = self.signos_info[7]
        self.signos_paciente_id = self.signos_info[8]
        
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
"")
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 310, 127, 61))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 21))
        self.label_5.setMaximumSize(QSize(16777215, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.sistolica_lineEdit_3 = QLineEdit(self.layoutWidget)
        self.sistolica_lineEdit_3.setObjectName(u"sistolica_lineEdit_3")
        self.sistolica_lineEdit_3.setMinimumSize(QSize(0, 28))
        self.sistolica_lineEdit_3.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_3.addWidget(self.sistolica_lineEdit_3)

        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 310, 127, 61))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 21))
        self.label_6.setMaximumSize(QSize(16777215, 21))
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.diastolica_lineEdit_4 = QLineEdit(self.layoutWidget_2)
        self.diastolica_lineEdit_4.setObjectName(u"diastolica_lineEdit_4")
        self.diastolica_lineEdit_4.setMinimumSize(QSize(0, 28))
        self.diastolica_lineEdit_4.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_4.addWidget(self.diastolica_lineEdit_4)

        self.layoutWidget_3 = QWidget(self)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 230, 161, 59))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 21))
        self.label_8.setMaximumSize(QSize(16777215, 21))
        self.label_8.setFont(font)

        self.verticalLayout_6.addWidget(self.label_8)

        self.temperatura_lineEdit_6 = QLineEdit(self.layoutWidget_3)
        self.temperatura_lineEdit_6.setObjectName(u"temperatura_lineEdit_6")
        self.temperatura_lineEdit_6.setMinimumSize(QSize(0, 28))
        self.temperatura_lineEdit_6.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_6.addWidget(self.temperatura_lineEdit_6)

        self.layoutWidget_4 = QWidget(self)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 390, 182, 59))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 21))
        self.label_9.setMaximumSize(QSize(16777215, 21))
        self.label_9.setFont(font)

        self.verticalLayout_7.addWidget(self.label_9)

        self.frecuencia_lineEdit_7 = QLineEdit(self.layoutWidget_4)
        self.frecuencia_lineEdit_7.setObjectName(u"frecuencia_lineEdit_7")
        self.frecuencia_lineEdit_7.setMinimumSize(QSize(0, 28))
        self.frecuencia_lineEdit_7.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_7.addWidget(self.frecuencia_lineEdit_7)

        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 321, 35))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.layoutWidget_5 = QWidget(self)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(330, 520, 201, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.guardar_btn = QPushButton(self.layoutWidget_5)
        self.guardar_btn.setObjectName(u"guardar_btn")
        self.guardar_btn.setMinimumSize(QSize(0, 41))
        self.guardar_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.guardar_btn)

        self.cancelar_btn = QPushButton(self.layoutWidget_5)
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

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 150, 127, 59))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 21))
        self.label_3.setMaximumSize(QSize(16777215, 21))
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.peso_lineEdit = QLineEdit(self.layoutWidget1)
        self.peso_lineEdit.setObjectName(u"peso_lineEdit")
        self.peso_lineEdit.setMinimumSize(QSize(0, 28))
        self.peso_lineEdit.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout.addWidget(self.peso_lineEdit)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(180, 150, 127, 59))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 21))
        self.label_4.setMaximumSize(QSize(16777215, 21))
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.estatura_lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.estatura_lineEdit_2.setObjectName(u"estatura_lineEdit_2")
        self.estatura_lineEdit_2.setMinimumSize(QSize(0, 28))
        self.estatura_lineEdit_2.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_2.addWidget(self.estatura_lineEdit_2)

        self.layoutWidget3 = QWidget(self)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(200, 230, 191, 59))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 21))
        self.label_7.setMaximumSize(QSize(16777215, 21))
        self.label_7.setFont(font)

        self.verticalLayout_5.addWidget(self.label_7)

        self.oxigenacion_lineEdit_5 = QLineEdit(self.layoutWidget3)
        self.oxigenacion_lineEdit_5.setObjectName(u"oxigenacion_lineEdit_5")
        self.oxigenacion_lineEdit_5.setMinimumSize(QSize(0, 28))
        self.oxigenacion_lineEdit_5.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_5.addWidget(self.oxigenacion_lineEdit_5)

        self.layoutWidget4 = QWidget(self)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(9, 77, 521, 60))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 21))
        self.label_10.setMaximumSize(QSize(16777215, 21))
        self.label_10.setFont(font)

        self.verticalLayout_8.addWidget(self.label_10)

        self.signos_nombre = QLabel(self.layoutWidget4)
        self.signos_nombre.setObjectName(u"signos_nombre")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.signos_nombre.setFont(font2)

        self.verticalLayout_8.addWidget(self.signos_nombre)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("SignosDialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("SignosDialog", u"Presi\u00f3n Sist\u00f3lica", None))
        self.label_6.setText(QCoreApplication.translate("SignosDialog", u"Presi\u00f3n Diast\u00f3lica", None))
        self.label_8.setText(QCoreApplication.translate("SignosDialog", u"Temp. Corporal (\u00b0C)", None))
        self.label_9.setText(QCoreApplication.translate("SignosDialog", u"Frecuencia cardiaca (LPM)", None))
        self.label.setText(QCoreApplication.translate("SignosDialog", u"Editar Signos", None))
        self.guardar_btn.setText(QCoreApplication.translate("SignosDialog", u"Editar", None))
        self.cancelar_btn.setText(QCoreApplication.translate("SignosDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("SignosDialog", u"Peso (kg)", None))
        self.label_4.setText(QCoreApplication.translate("SignosDialog", u"Estatura (m)", None))
        self.label_7.setText(QCoreApplication.translate("SignosDialog", u"Saturaci\u00f3n de oxigeno (%)", None))
        self.label_10.setText(QCoreApplication.translate("SignosDialog", u"Paciente", None))
        self.signos_nombre.setText(QCoreApplication.translate("SignosDialog", self.row_data[1], None))
    # retranslateUi

        self.peso_lineEdit.setText(str(self.signos_peso))
        self.estatura_lineEdit_2.setText(str(self.signos_estatura))
        self.sistolica_lineEdit_3.setText(str(self.signos_sistolica))
        self.diastolica_lineEdit_4.setText(str(self.signos_diastolica))
        self.oxigenacion_lineEdit_5.setText(str(self.signos_oxigenacion))
        self.temperatura_lineEdit_6.setText(str(self.signos_temperatura))
        self.frecuencia_lineEdit_7.setText(str(self.signos_frecuencia))    
    
        self.guardar_btn.clicked.connect(self.editar_datos)
        self.cancelar_btn.clicked.connect(self.close)
        
    def crear_conexion(self):
        con = sqlite3.connect("hospital.db")
    
        self.mydb = con
    
        return self.mydb

    def signos_seleccionado(self):
        
        self.cur = self.crear_conexion().cursor()
        
        # obtenemos las variables del paciente de la tabla
        self.id_signo = self.row_data[0]
        
        consulta = f"SELECT * FROM signos WHERE id = '{self.id_signo}'"
        
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
            
            consulta_editar = f"""
                UPDATE signos
                SET
                    peso='{self.peso_lineEdit.text()}',
                    estatura='{self.estatura_lineEdit_2.text()}',
                    sistolica='{self.sistolica_lineEdit_3.text()}',
                    diastolica='{self.diastolica_lineEdit_4.text()}',
                    oxigenacion='{self.oxigenacion_lineEdit_5.text()}',
                    temperatura='{self.temperatura_lineEdit_6.text()}',
                    frecuencia='{self.frecuencia_lineEdit_7.text()}',
                    idPaciente='{self.signos_info[8]}'
                WHERE
                    id='{self.id_signo}'
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
            
    def mostrar_mensaje_editar(self):
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Editado")
        msg_box.setText("la información de los signos ha sido editada")
        msg_box.exec()
    


