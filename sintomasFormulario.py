# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sintomasFormulario.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

import sqlite3

class Ui_SintomasDialog(object):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 321, 35))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(320, 530, 201, 43))
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
        self.layoutWidget.setGeometry(QRect(20, 80, 241, 491))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tos_checkBox = QCheckBox(self.layoutWidget)
        self.tos_checkBox.setObjectName(u"tos_checkBox")

        self.verticalLayout.addWidget(self.tos_checkBox)

        self.fatiga_checkBox = QCheckBox(self.layoutWidget)
        self.fatiga_checkBox.setObjectName(u"fatiga_checkBox")

        self.verticalLayout.addWidget(self.fatiga_checkBox)

        self.vomito_checkBox = QCheckBox(self.layoutWidget)
        self.vomito_checkBox.setObjectName(u"vomito_checkBox")

        self.verticalLayout.addWidget(self.vomito_checkBox)

        self.dolorgarganta_checkBox = QCheckBox(self.layoutWidget)
        self.dolorgarganta_checkBox.setObjectName(u"dolorgarganta_checkBox")

        self.verticalLayout.addWidget(self.dolorgarganta_checkBox)

        self.diarrea_checkBox = QCheckBox(self.layoutWidget)
        self.diarrea_checkBox.setObjectName(u"diarrea_checkBox")

        self.verticalLayout.addWidget(self.diarrea_checkBox)

        self.dolorcabeza_checkBox = QCheckBox(self.layoutWidget)
        self.dolorcabeza_checkBox.setObjectName(u"dolorcabeza_checkBox")

        self.verticalLayout.addWidget(self.dolorcabeza_checkBox)

        self.fiebre_checkBox = QCheckBox(self.layoutWidget)
        self.fiebre_checkBox.setObjectName(u"fiebre_checkBox")

        self.verticalLayout.addWidget(self.fiebre_checkBox)

        self.dolorabdominal_checkBox = QCheckBox(self.layoutWidget)
        self.dolorabdominal_checkBox.setObjectName(u"dolorabdominal_checkBox")

        self.verticalLayout.addWidget(self.dolorabdominal_checkBox)

        self.contusion_checkBox = QCheckBox(self.layoutWidget)
        self.contusion_checkBox.setObjectName(u"contusion_checkBox")

        self.verticalLayout.addWidget(self.contusion_checkBox)

        self.deshidratacion_checkBox = QCheckBox(self.layoutWidget)
        self.deshidratacion_checkBox.setObjectName(u"deshidratacion_checkBox")

        self.verticalLayout.addWidget(self.deshidratacion_checkBox)

        self.perdidavision_checkBox = QCheckBox(self.layoutWidget)
        self.perdidavision_checkBox.setObjectName(u"perdidavision_checkBox")

        self.verticalLayout.addWidget(self.perdidavision_checkBox)

        self.quemadura_checkBox = QCheckBox(self.layoutWidget)
        self.quemadura_checkBox.setObjectName(u"quemadura_checkBox")

        self.verticalLayout.addWidget(self.quemadura_checkBox)

        self.difrespiratoria_checkBox = QCheckBox(self.layoutWidget)
        self.difrespiratoria_checkBox.setObjectName(u"difrespiratoria_checkBox")

        self.verticalLayout.addWidget(self.difrespiratoria_checkBox)

        self.dolorpecho_checkBox = QCheckBox(self.layoutWidget)
        self.dolorpecho_checkBox.setObjectName(u"dolorpecho_checkBox")

        self.verticalLayout.addWidget(self.dolorpecho_checkBox)

        self.hemorragia_checkBox = QCheckBox(self.layoutWidget)
        self.hemorragia_checkBox.setObjectName(u"hemorragia_checkBox")

        self.verticalLayout.addWidget(self.hemorragia_checkBox)

        self.conciencia_checkBox = QCheckBox(self.layoutWidget)
        self.conciencia_checkBox.setObjectName(u"conciencia_checkBox")

        self.verticalLayout.addWidget(self.conciencia_checkBox)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, SintomasDialog):
        SintomasDialog.setWindowTitle(QCoreApplication.translate("SintomasDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SintomasDialog", u"Registrar Sintomas", None))
        self.registrar_btn.setText(QCoreApplication.translate("SintomasDialog", u"Registrar", None))
        self.cancelar_btn.setText(QCoreApplication.translate("SintomasDialog", u"Cancelar", None))
        self.tos_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Tos", None))
        self.fatiga_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Fatiga", None))
        self.vomito_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Vomito", None))
        self.dolorgarganta_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Dolor de garganta", None))
        self.diarrea_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Diarrea", None))
        self.dolorcabeza_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Dolor de cabeza", None))
        self.fiebre_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Fiebre", None))
        self.dolorabdominal_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Dolor abdominal", None))
        self.contusion_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Contusi\u00f3n", None))
        self.deshidratacion_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Deshidrataci\u00f3n", None))
        self.perdidavision_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Perdida de visi\u00f3n", None))
        self.quemadura_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Quemadura", None))
        self.difrespiratoria_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Dificultad respiratoria", None))
        self.dolorpecho_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Dolor en el pecho", None))
        self.hemorragia_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Hemorragia", None))
        self.conciencia_checkBox.setText(QCoreApplication.translate("SintomasDialog", u"Perdida de conciencia", None))
    # retranslateUi

