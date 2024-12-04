# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assests_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setGeometry(QRect(0, 0, 171, 721))
        self.menu_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(139, 208, 208);\n"
"}\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.frame = QFrame(self.menu_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 150, 130))
        self.frame.setMinimumSize(QSize(0, 130))
        self.frame.setMaximumSize(QSize(16777215, 130))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, -3, 121, 141))
        font = QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u":/iconos/icons/logo.png"))
        self.layoutWidget = QWidget(self.menu_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 151, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pacientes_btn = QPushButton(self.layoutWidget)
        self.pacientes_btn.setObjectName(u"pacientes_btn")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.pacientes_btn.setFont(font1)
        self.pacientes_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left:-24px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"	color: #8BD0D0;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/iconos/icons/paciente.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/iconos/icons/doctor-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pacientes_btn.setIcon(icon)
        self.pacientes_btn.setIconSize(QSize(16, 16))
        self.pacientes_btn.setCheckable(True)
        self.pacientes_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pacientes_btn)

        self.signos_btn = QPushButton(self.layoutWidget)
        self.signos_btn.setObjectName(u"signos_btn")
        self.signos_btn.setFont(font1)
        self.signos_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left:-50px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"	color: #8BD0D0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons/signos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/iconos/icons/signos-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signos_btn.setIcon(icon1)
        self.signos_btn.setIconSize(QSize(16, 16))
        self.signos_btn.setCheckable(True)
        self.signos_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.signos_btn)

        self.sintomas_btn = QPushButton(self.layoutWidget)
        self.sintomas_btn.setObjectName(u"sintomas_btn")
        self.sintomas_btn.setFont(font1)
        self.sintomas_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left:-28px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"	color: #8BD0D0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons/sintomas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/iconos/icons/sintomas-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.sintomas_btn.setIcon(icon2)
        self.sintomas_btn.setIconSize(QSize(16, 16))
        self.sintomas_btn.setCheckable(True)
        self.sintomas_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sintomas_btn)

        self.diagnostico_btn = QPushButton(self.layoutWidget)
        self.diagnostico_btn.setObjectName(u"diagnostico_btn")
        self.diagnostico_btn.setFont(font1)
        self.diagnostico_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left:0px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"	color: #8BD0D0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons/diagnostico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/iconos/icons/diagnostico-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.diagnostico_btn.setIcon(icon3)
        self.diagnostico_btn.setIconSize(QSize(16, 16))
        self.diagnostico_btn.setCheckable(True)
        self.diagnostico_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.diagnostico_btn)

        self.tratamiento_btn = QPushButton(self.layoutWidget)
        self.tratamiento_btn.setObjectName(u"tratamiento_btn")
        self.tratamiento_btn.setFont(font1)
        self.tratamiento_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left:0px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"	color: #8BD0D0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/icons/tratamiento.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/iconos/icons/tratamiento-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tratamiento_btn.setIcon(icon4)
        self.tratamiento_btn.setIconSize(QSize(16, 16))
        self.tratamiento_btn.setCheckable(True)
        self.tratamiento_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.tratamiento_btn)

        self.principal_widget = QWidget(self.centralwidget)
        self.principal_widget.setObjectName(u"principal_widget")
        self.principal_widget.setGeometry(QRect(180, 70, 1091, 641))
        self.stackedWidget = QStackedWidget(self.principal_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1071, 621))
        self.paciente_page = QWidget()
        self.paciente_page.setObjectName(u"paciente_page")
        self.label_9 = QLabel(self.paciente_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(9, 0, 301, 31))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_19 = QLabel(self.paciente_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 30, 251, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_19.setFont(font3)
        self.layoutWidget1 = QWidget(self.paciente_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 116, 431, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_paciente_apellidos = QLineEdit(self.layoutWidget1)
        self.search_paciente_apellidos.setObjectName(u"search_paciente_apellidos")
        self.search_paciente_apellidos.setMinimumSize(QSize(0, 38))
        self.search_paciente_apellidos.setMaximumSize(QSize(16777215, 38))
        self.search_paciente_apellidos.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.search_paciente_apellidos)

        self.search_paciente_poliza = QLineEdit(self.layoutWidget1)
        self.search_paciente_poliza.setObjectName(u"search_paciente_poliza")
        self.search_paciente_poliza.setMinimumSize(QSize(161, 38))
        self.search_paciente_poliza.setMaximumSize(QSize(161, 38))
        self.search_paciente_poliza.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.search_paciente_poliza)

        self.layoutWidget2 = QWidget(self.paciente_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 63, 431, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.regPaciente_btn = QPushButton(self.layoutWidget2)
        self.regPaciente_btn.setObjectName(u"regPaciente_btn")
        self.regPaciente_btn.setMinimumSize(QSize(0, 41))
        self.regPaciente_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.regPaciente_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 208, 208);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/icons/paciente.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.regPaciente_btn.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.regPaciente_btn)

        self.expExcel_paciente_btn = QPushButton(self.layoutWidget2)
        self.expExcel_paciente_btn.setObjectName(u"expExcel_paciente_btn")
        self.expExcel_paciente_btn.setMinimumSize(QSize(131, 41))
        self.expExcel_paciente_btn.setMaximumSize(QSize(131, 41))
        self.expExcel_paciente_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expExcel_paciente_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 127);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expExcel_paciente_btn.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.expExcel_paciente_btn)

        self.expPdf_paciente_btn = QPushButton(self.layoutWidget2)
        self.expPdf_paciente_btn.setObjectName(u"expPdf_paciente_btn")
        self.expPdf_paciente_btn.setMinimumSize(QSize(121, 41))
        self.expPdf_paciente_btn.setMaximumSize(QSize(121, 41))
        self.expPdf_paciente_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expPdf_paciente_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 92, 95);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expPdf_paciente_btn.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.expPdf_paciente_btn)

        self.paciente_tableWidget = QTableWidget(self.paciente_page)
        if (self.paciente_tableWidget.columnCount() < 8):
            self.paciente_tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.paciente_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.paciente_tableWidget.setObjectName(u"paciente_tableWidget")
        self.paciente_tableWidget.setEnabled(True)
        self.paciente_tableWidget.setGeometry(QRect(10, 170, 1061, 451))
        self.paciente_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: rgb(231, 231, 231);\n"
"	background-color: white;\n"
"}")
        self.paciente_tableWidget.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.paciente_page)
        self.signos_page = QWidget()
        self.signos_page.setObjectName(u"signos_page")
        self.label_4 = QLabel(self.signos_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 230, 271, 141))
        font4 = QFont()
        font4.setPointSize(24)
        self.label_4.setFont(font4)
        self.regSignos_btn = QPushButton(self.signos_page)
        self.regSignos_btn.setObjectName(u"regSignos_btn")
        self.regSignos_btn.setGeometry(QRect(10, 70, 151, 41))
        self.regSignos_btn.setMinimumSize(QSize(0, 41))
        self.regSignos_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 208, 208);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/icons/signos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.regSignos_btn.setIcon(icon8)
        self.label_10 = QLabel(self.signos_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 301, 31))
        self.label_10.setFont(font2)
        self.label_21 = QLabel(self.signos_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 30, 251, 31))
        self.label_21.setFont(font3)
        self.signos_tableWidget = QTableWidget(self.signos_page)
        if (self.signos_tableWidget.columnCount() < 10):
            self.signos_tableWidget.setColumnCount(10)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.signos_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        self.signos_tableWidget.setObjectName(u"signos_tableWidget")
        self.signos_tableWidget.setGeometry(QRect(10, 170, 1071, 441))
        self.signos_tableWidget.setMinimumSize(QSize(1071, 0))
        self.signos_tableWidget.setMaximumSize(QSize(1071, 16777215))
        self.signos_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: rgb(231, 231, 231);\n"
"	background-color: white;\n"
"}")
        self.signos_tableWidget.setAlternatingRowColors(True)
        self.search_signos_paciente = QLineEdit(self.signos_page)
        self.search_signos_paciente.setObjectName(u"search_signos_paciente")
        self.search_signos_paciente.setGeometry(QRect(10, 120, 262, 38))
        self.search_signos_paciente.setMinimumSize(QSize(0, 38))
        self.search_signos_paciente.setMaximumSize(QSize(16777215, 38))
        self.search_signos_paciente.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget.addWidget(self.signos_page)
        self.sintomas_page = QWidget()
        self.sintomas_page.setObjectName(u"sintomas_page")
        self.label_13 = QLabel(self.sintomas_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(9, 0, 261, 31))
        self.label_13.setFont(font2)
        self.label_20 = QLabel(self.sintomas_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 30, 251, 31))
        self.label_20.setFont(font3)
        self.regSintomas_btn = QPushButton(self.sintomas_page)
        self.regSintomas_btn.setObjectName(u"regSintomas_btn")
        self.regSintomas_btn.setGeometry(QRect(10, 63, 165, 41))
        self.regSintomas_btn.setMinimumSize(QSize(0, 41))
        self.regSintomas_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.regSintomas_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 208, 208);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/icons/sintomas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.regSintomas_btn.setIcon(icon9)
        self.stackedWidget.addWidget(self.sintomas_page)
        self.diagnostico = QWidget()
        self.diagnostico.setObjectName(u"diagnostico")
        self.label_6 = QLabel(self.diagnostico)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 220, 321, 141))
        self.label_6.setFont(font4)
        self.label_11 = QLabel(self.diagnostico)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 301, 31))
        self.label_11.setFont(font2)
        self.label_22 = QLabel(self.diagnostico)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 40, 251, 31))
        self.label_22.setFont(font3)
        self.regDiagnostico_btn = QPushButton(self.diagnostico)
        self.regDiagnostico_btn.setObjectName(u"regDiagnostico_btn")
        self.regDiagnostico_btn.setGeometry(QRect(10, 80, 181, 41))
        self.regDiagnostico_btn.setMinimumSize(QSize(0, 41))
        self.regDiagnostico_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 208, 208);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        self.regDiagnostico_btn.setIcon(icon5)
        self.diagnostico_tableWidget = QTableWidget(self.diagnostico)
        if (self.diagnostico_tableWidget.columnCount() < 6):
            self.diagnostico_tableWidget.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.diagnostico_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.diagnostico_tableWidget.setObjectName(u"diagnostico_tableWidget")
        self.diagnostico_tableWidget.setGeometry(QRect(10, 140, 1071, 441))
        self.diagnostico_tableWidget.setMinimumSize(QSize(1071, 0))
        self.diagnostico_tableWidget.setMaximumSize(QSize(1071, 16777215))
        self.diagnostico_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: rgb(231, 231, 231);\n"
"	background-color: white;\n"
"}")
        self.diagnostico_tableWidget.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.diagnostico)
        self.tratamiento_page = QWidget()
        self.tratamiento_page.setObjectName(u"tratamiento_page")
        self.label_7 = QLabel(self.tratamiento_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 220, 341, 141))
        self.label_7.setFont(font4)
        self.label_12 = QLabel(self.tratamiento_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 301, 31))
        self.label_12.setFont(font2)
        self.label_23 = QLabel(self.tratamiento_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 30, 251, 31))
        self.label_23.setFont(font3)
        self.regTratamiento_btn = QPushButton(self.tratamiento_page)
        self.regTratamiento_btn.setObjectName(u"regTratamiento_btn")
        self.regTratamiento_btn.setGeometry(QRect(10, 70, 191, 41))
        self.regTratamiento_btn.setMinimumSize(QSize(0, 41))
        self.regTratamiento_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 208, 208);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}")
        self.regTratamiento_btn.setIcon(icon5)
        self.tratamiento_tableWidget = QTableWidget(self.tratamiento_page)
        if (self.tratamiento_tableWidget.columnCount() < 5):
            self.tratamiento_tableWidget.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tratamiento_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tratamiento_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tratamiento_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tratamiento_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tratamiento_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        self.tratamiento_tableWidget.setObjectName(u"tratamiento_tableWidget")
        self.tratamiento_tableWidget.setGeometry(QRect(10, 130, 1071, 441))
        self.tratamiento_tableWidget.setMinimumSize(QSize(1071, 0))
        self.tratamiento_tableWidget.setMaximumSize(QSize(1071, 16777215))
        self.tratamiento_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #8bd0d0;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: rgb(231, 231, 231);\n"
"	background-color: white;\n"
"}")
        self.tratamiento_tableWidget.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.tratamiento_page)
        self.encabezado_widget = QWidget(self.centralwidget)
        self.encabezado_widget.setObjectName(u"encabezado_widget")
        self.encabezado_widget.setGeometry(QRect(180, 10, 1091, 51))
        self.label_2 = QLabel(self.encabezado_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(6, 4, 461, 41))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_3 = QLabel(self.encabezado_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(950, 16, 121, 20))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_3.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pacientes_btn.setText(QCoreApplication.translate("MainWindow", u" Pacientes", None))
        self.signos_btn.setText(QCoreApplication.translate("MainWindow", u" Signos", None))
        self.sintomas_btn.setText(QCoreApplication.translate("MainWindow", u" Sintomas", None))
        self.diagnostico_btn.setText(QCoreApplication.translate("MainWindow", u" Diagn\u00f3stico", None))
        self.tratamiento_btn.setText(QCoreApplication.translate("MainWindow", u" Tratamiento", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del Paciente", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Lista de Pacientes", None))
        self.search_paciente_apellidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por apellidos...", None))
        self.search_paciente_poliza.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bucar por poliza...", None))
        self.regPaciente_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar Paciente", None))
        self.expExcel_paciente_btn.setText(QCoreApplication.translate("MainWindow", u" Exportar a Excel", None))
        self.expPdf_paciente_btn.setText(QCoreApplication.translate("MainWindow", u" Exportar a PDF", None))
        ___qtablewidgetitem = self.paciente_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.paciente_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.paciente_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Poliza", None));
        ___qtablewidgetitem3 = self.paciente_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem4 = self.paciente_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None));
        ___qtablewidgetitem5 = self.paciente_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem6 = self.paciente_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Genero", None));
        ___qtablewidgetitem7 = self.paciente_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Opciones", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Signos Catalogo", None))
        self.regSignos_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar Signos", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Signos del Paciente", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Lista de signos", None))
        ___qtablewidgetitem8 = self.signos_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem9 = self.signos_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem10 = self.signos_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem11 = self.signos_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Estatura", None));
        ___qtablewidgetitem12 = self.signos_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sist\u00f3lica", None));
        ___qtablewidgetitem13 = self.signos_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Diast\u00f3lica", None));
        ___qtablewidgetitem14 = self.signos_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Oxigenaci\u00f3n", None));
        ___qtablewidgetitem15 = self.signos_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None));
        ___qtablewidgetitem16 = self.signos_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Frecuencia", None));
        ___qtablewidgetitem17 = self.signos_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Opciones", None));
        self.search_signos_paciente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por poliza o nombre...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sintomas del paciente", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Lista de sintomas", None))
        self.regSintomas_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar Sintomas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3stico Catalogo", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3stico del paciente", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Lista de diagn\u00f3sticos", None))
        self.regDiagnostico_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar Diagn\u00f3stico", None))
        ___qtablewidgetitem18 = self.diagnostico_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem19 = self.diagnostico_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Poliza", None));
        ___qtablewidgetitem20 = self.diagnostico_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem21 = self.diagnostico_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem22 = self.diagnostico_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3stico", None));
        ___qtablewidgetitem23 = self.diagnostico_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Opciones", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tratamiento Catalogo", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tratamiento del Paciente", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Lista de tratamientoa", None))
        self.regTratamiento_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar Tratamiento", None))
        ___qtablewidgetitem24 = self.tratamiento_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem25 = self.tratamiento_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Duracion", None));
        ___qtablewidgetitem26 = self.tratamiento_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Indicaciones", None));
        ___qtablewidgetitem27 = self.tratamiento_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Observaciones", None));
        ___qtablewidgetitem28 = self.tratamiento_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Opciones", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bienvenidos al servicio de urgencias", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario X (admin)", None))
    # retranslateUi

