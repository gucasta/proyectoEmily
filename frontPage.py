from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton, QFileDialog, QMessageBox
from PySide6.QtGui import QAction, QIcon
from ui_principal import Ui_MainWindow

import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from pacienteFormularioUpdate import Ui_PacienteDialogUpdate

class MenuBarraLateral(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("Sistema Integral de Urgencias")
    
    # Conectamos los botones a las diferentes paginas
    self.pacientes_btn.clicked.connect(self.cambiar_a_pagina_pacientes)
    self.signos_btn.clicked.connect(self.cambiar_a_pagina_signos)
    self.sintomas_btn.clicked.connect(self.cambiar_a_pagina_sintomas)
    self.diagnostico_btn.clicked.connect(self.cambiar_a_pagina_diagnostico)
    self.tratamiento_btn.clicked.connect(self.cambiar_a_pagina_tratamiento)
    
    # Creamos una conexion a sqlite3
    self.crear_conexion()
    
    # Creamos las tablas
    self.crear_tabla_pacientes()
    self.crear_tabla_signos()
    self.crear_tabla_diagnostico()
    
    # Cargamos informacion en el QTable
    self.cargar_datos_pacientes()
    self.cargar_signos_pacientes()
    self.cargar_diagnostico_pacientes()
    
    # Filtros de busqueda pacientes
    self.search_paciente_apellidos.textChanged.connect(self.buscar_paciente_apellidos)
    self.search_paciente_poliza.textChanged.connect(self.buscar_paciente_poliza)
    
    # Ajustamos ancho de celdas de la tabla pacientes
    self.paciente_tableWidget.setColumnWidth(0, 40)
    self.paciente_tableWidget.setColumnWidth(1, 80)
    self.paciente_tableWidget.setColumnWidth(2, 80)
    self.paciente_tableWidget.setColumnWidth(3, 200)
    self.paciente_tableWidget.setColumnWidth(4, 200)
    self.paciente_tableWidget.setColumnWidth(5, 100)
    self.paciente_tableWidget.setColumnWidth(6, 100)
    self.paciente_tableWidget.setColumnWidth(7, 135)
    
    # Exportar a Excel
    self.expExcel_paciente_btn.clicked.connect(self.exportar_a_excel_pacientes)
    
    # Exportar a PDF
    self.expPdf_paciente_btn.clicked.connect(self.exportar_a_pdf_pacientes)

    # Vinculamos el boton de registro para abrir formulario
    self.regPaciente_btn.clicked.connect(self.abrir_formulario_paciente)
    self.regSignos_btn.clicked.connect(self.abrir_formulario_signos)
    self.regDiagnostico_btn.clicked.connect(self.abrir_formulario_diagnostico)
    
  # Funciones o metodos para cambiar de pagina
  def cambiar_a_pagina_pacientes(self):
    self.stackedWidget.setCurrentIndex(0)
  def cambiar_a_pagina_signos(self):
    self.stackedWidget.setCurrentIndex(1)
  def cambiar_a_pagina_sintomas(self):
    self.stackedWidget.setCurrentIndex(2)
  def cambiar_a_pagina_diagnostico(self):
    self.stackedWidget.setCurrentIndex(3)
  def cambiar_a_pagina_tratamiento(self):
    self.stackedWidget.setCurrentIndex(4)
    
  # Funcion o metodo para crear BD
  def crear_conexion(self):
    con = sqlite3.connect("hospital.db")
    
    self.mydb = con
    
    return self.mydb
  
  # Funcion o metodo para crear tabla
  def crear_tabla_pacientes(self):
    # Creamos un cursor para ejecutar consultar SQL
    cur = self.crear_conexion().cursor()

  def crear_tabla_signos(self):
    cur = self.crear_conexion().cursor()

  def crear_tabla_diagnostico(self):
    cur = self.crear_conexion().cursor()
    
    consulta_crear_tabla_pacientes = f"""
      CREATE TABLE IF NOT EXISTS pacientes(
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        poliza TEXT,
        nombre TEXT,
        apellidos TEXT,
        edad INT,
        genero TEXT
      )
    """
  
    cur.execute(consulta_crear_tabla_pacientes)
    
    consulta_crear_tabla_signos = f"""
      CREATE TABLE IF NOT EXISTS signos(
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        peso INT,
        estatura INT,
        sistolica INT,
        diastolica INT,
        oxigenacion INT,
        temperatura INT,
        frecuencia INT
      )
    """
  
    cur.execute(consulta_crear_tabla_signos)

    # TODO: Para Emily, no repetir datos que ya estan en otras tablas: "poliza", "nombre", "apellido" ya existen en la tabla paciente
    # porque rompe con la formas normales de la teoria de las Bases de Datos
    consulta_crear_tabla_diagnostico = f"""
      CREATE TABLE IF NOT EXISTS signos(
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        fecha INT,
        poliza INT,
        nombre INT,
        apellido INT,
        diagnostico INT
      )
    """
    
    self.mydb.commit()
    self.mydb.close()
  
  # Funcion o metodo para abrir formulario
  def abrir_formulario_paciente(self):
    # Importamos el formulario
    from pacienteFormulario import Ui_PacienteDialog

    # Creamos una instancia y mostramos el formulario
    paciente_formulario = Ui_PacienteDialog(self)
    resultado = paciente_formulario.exec()
    
    # Si el registro del paciente se hizo correctamente recargamos la tabla de paciente
    if resultado == Ui_PacienteDialog.Accepted:
      self.recargar_datos_pacientes()

  def abrir_formulario_signos(self):
    from signosFormulario import Ui_SignosDialog

    signos_formulario = Ui_SignosDialog(self)
    resultado = signos_formulario.exec()
  
  def abrir_formulario_diagnostico(self):
    from diagnosticoFormulario import Ui_DiagnosticoDialog

    diagnostico_formulario = Ui_DiagnosticoDialog(self)
    resultado = diagnostico_formulario.exec()
    
  # Funcion o metodo para recargar datos despues de un registro
  def recargar_datos_pacientes(self):
    self.cargar_datos_pacientes()

  def recargar_datos_signos(self):
    pass

  def recargar_datos_diagnostico(self):
    pass
  
  # Funcion o metodo para cargar datos de los pacientes
  def cargar_datos_pacientes(self):
    # Limpiamos los datos existentes en la tabla
    self.paciente_tableWidget.setRowCount(0)
    
    datos = self.obtener_datos_tabla_pacientes()
    
    # Alimentamos la tabla
    for row_index, row_data in enumerate(datos):
      self.paciente_tableWidget.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        elemento = QTableWidgetItem(str(cell_data))
        self.paciente_tableWidget.setItem(row_index, col_index, elemento)
        
        # Widget personalizado con los botones de accion de editar y borrar
        botones_acciones_widget = BotonesAccionWidgetPaciente(row_index, row_data, self)
        
        # Insertamos los botones en la celda de acciones
        self.paciente_tableWidget.setCellWidget(row_index, 7, botones_acciones_widget)
        self.paciente_tableWidget.setRowHeight(row_index, 50)
        
  # Funcion para busqueda de paciente por apellidos
  def buscar_paciente_apellidos(self):
    # Borramos los resultados anteriores
    self.paciente_tableWidget.setRowCount(0)
    
    # Obtenemos la consulta de busqueda del QLineEdit
    consulta_busqueda = self.search_paciente_apellidos.text()
    
    # Ejecutamos la consulta SQL
    cur = self.crear_conexion().cursor()
    sql_query = f"""
      SELECT * FROM pacientes WHERE apellidos LIKE '%{consulta_busqueda}%'
    """
    
    cur.execute(sql_query)
    resultados = cur.fetchall()
    
    # Alimentamos la tabla con los datos de la busqueda
    for row_index, row_data in enumerate(resultados):
      self.paciente_tableWidget.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        elemento = QTableWidgetItem(str(cell_data))
        self.paciente_tableWidget.setItem(row_index, col_index, elemento)
        
        # Widget personalizado con los botones de accion de editar y borrar
        botones_acciones_widget = BotonesAccionWidgetPaciente(row_index, row_data, self)
        
        # Insertamos los botones en la celda de acciones
        self.paciente_tableWidget.setCellWidget(row_index, 7, botones_acciones_widget)
        self.paciente_tableWidget.setRowHeight(row_index, 50)
        
  # Funcion para busqueda de paciente por poliza
  def buscar_paciente_poliza(self):
    # Borramos los resultados anteriores
    self.paciente_tableWidget.setRowCount(0)
    
    # Obtenemos la consulta de busqueda del QLineEdit
    consulta_busqueda = self.search_paciente_poliza.text()
    
    # Ejecutamos la consulta SQL
    cur = self.crear_conexion().cursor()
    sql_query = f"""
      SELECT * FROM pacientes WHERE poliza LIKE '%{consulta_busqueda}%'
    """
    
    cur.execute(sql_query)
    resultados = cur.fetchall()
    
    # Alimentamos la tabla con los datos de la busqueda
    for row_index, row_data in enumerate(resultados):
      self.paciente_tableWidget.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        elemento = QTableWidgetItem(str(cell_data))
        self.paciente_tableWidget.setItem(row_index, col_index, elemento)
        
        # Widget personalizado con los botones de accion de editar y borrar
        botones_acciones_widget = BotonesAccionWidgetPaciente(row_index, row_data, self)
        
        # Insertamos los botones en la celda de acciones
        self.paciente_tableWidget.setCellWidget(row_index, 7, botones_acciones_widget)
        self.paciente_tableWidget.setRowHeight(row_index, 50)
  
  # Funcion para exportar a Excel
  def exportar_a_excel_pacientes(self):
    # Convertimos de QTableWidget a DataFrame de pandas
    datos = []
    
    self.headers = [self.paciente_tableWidget.horizontalHeaderItem(col).text() for col in range(self.paciente_tableWidget.columnCount())]
    
    for row in range(self.paciente_tableWidget.rowCount()):
      # Checamos si el elemento no es None antes de acceder al texto
      row_data = [self.paciente_tableWidget.item(row, col).text() if self.paciente_tableWidget.item(row, col) is not None else "" for col in range(self.paciente_tableWidget.columnCount())]
      datos.append(row_data)
    
    # Creamos un DataFrame de pandas con los datos y los encabezados
    df = pd.DataFrame(datos, columns=self.headers)
    
    # Guardamos el DataFrame a un archivo de Excel
    # Exlcuimos la ultima columna antes de exportar
    df_filtrado = df.iloc[:1, :-1]
    
    # Abrimos QFileDialog para obtener la ruta de guardado
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getSaveFileName(self, "Guardar Archivo de Excel", "", "Archivo de Excel (*.xlsx);;Todos los archivos(*)")
      
    if file_path:
      # Guardamos el DataFrame filtrado a un archivo de excel en la ruta especificado
      df_filtrado.to_excel(file_path, index=False)

  # Funcion para exportar a PDF
  def exportar_a_pdf_pacientes(self):
    # Abrimos QFileDialog para obtener la ruta de guardado
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getSaveFileName(self, "Guardar Archivo PDF", "", "Archivo PDF (*.pdf);;Todos los archivos(*)")
    
    if file_path:
      # Creamos el documento PDF
      documento_pdf = SimpleDocTemplate(file_path, pagesize=letter)
      
      # Asumiendo que n es el numero total de columnas in el widget QTable
      n = self.paciente_tableWidget.columnCount()
      
      # Extraemos los encabezados de QTableWidget menos uno (acciones)
      headers = [self.paciente_tableWidget.horizontalHeaderItem(col).text() for col in range(n-1)]
      
      # Extrarmos los datos de QTableWidget, excluyendo la ultima columna (acciones)
      datos = [headers]
      
      for row in range(self.paciente_tableWidget.rowCount()):
        row_data = [self.paciente_tableWidget.item(row, col).text() if self.paciente_tableWidget.item(row, col) is not None else "" for col in range(n-1)]
        datos.append(row_data)
        
      # Creamos una tabla para PDF
      tabla_pdf = Table(datos)
      
      # Aplicamos estilos a la tabla
      estilo = TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
      ])
      
      tabla_pdf.setStyle(estilo)
      
      # Construimos el documento PDF
      documento_pdf.build([tabla_pdf])

  def cargar_signos_pacientes(self):
    self.signos_tableWidget.setRowCount(0)
    
    datos = self.obtener_datos_tabla_signos()
    
    for row_index, row_data in enumerate(datos):
      self.diagnostico_tableWidget.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        elemento = QTableWidgetItem(str(cell_data))
        self.diagnostico_tableWidget.setItem(row_index, col_index, elemento)

  #TODO: Para Emily, implementar bien la funcion de obtener_datos_tabla_diagnostico
  def cargar_diagnostico_pacientes(self):
    pass
    # self.diagnostico_tableWidget.setRowCount(0)
    
    # datos = self.obtener_datos_tabla_diagnostico()
    
    # for row_index, row_data in enumerate(datos):
    #   self.signos_tableWidget.insertRow(row_index)
    #   for col_index, cell_data in enumerate(row_data):
    #     elemento = QTableWidgetItem(str(cell_data))
    #     self.signos_tableWidget.setItem(row_index, col_index, elemento)
    
  # Separar las consultas por cada tabla
  def obtener_datos_tabla_pacientes(self):
    cur = self.crear_conexion().cursor()
    
    # Construimos la consulta SQL
    consulta = f"""
      SELECT * FROM pacientes
    """
    
    cur.execute(consulta)
    datos = cur.fetchall()
    return datos
  
  def obtener_datos_tabla_signos(self):
    cur = self.crear_conexion().cursor()

    consulta = f"""
      SELECT peso, estatura, sistolica, diastolica, oxigenacion, temperatura, frecuencia FROM signos
    """
    
    cur.execute(consulta)
    datos = cur.fetchall()
    return datos
  
  # TODO: Para Emily, corregir el codigo de la consulta
  def obtener_datos_tabla_diagnostico(self):
    pass
    # cur = self.crear_conexion().cursor()
    
    # consulta = f"""
    #   SELECT fecha, poliza, nombre, apellido, diagnostico FROM diagnostico
    # """
    
    # cur.execute(consulta)
    # datos = cur.fetchall()
    # return datos
    
# Clase de botones de accion de editar y borrar
class BotonesAccionWidgetPaciente(QWidget):
  def __init__(self, row_index, row_data, barraLateral):
    super().__init__()
    
    # Almacenamos el indice de fila y sus datos como una instancia en variables
    self.row_index = row_index
    self.row_data = row_data
    self.barraLateral = barraLateral # Almacenamos una referencia a MenuBarraLateral
    
    # Obtenemos el numero de poliza del paciente
    self.paciente_id = self.row_data[0]
    self.paciente_poliza = self.row_data[2]
    
    layout = QHBoxLayout(self)
    
    # Creamos el boton de editar
    self.boton_editar = QPushButton("", self)
    self.boton_editar.setStyleSheet("background-color: rgb(0, 170, 255);")
    self.boton_editar.setFixedSize(61, 31)
    self.boton_editar.clicked.connect(self.click_editar)
    
    # Creamos el boton de borrar
    self.boton_borrar = QPushButton("", self)
    self.boton_borrar.setStyleSheet("background-color: rgb(255, 92, 95);")
    self.boton_borrar.setFixedSize(61, 31)
    self.boton_borrar.clicked.connect(self.click_borrar)
    
    # Añadimos iconos para los botones
    icono_editar = QIcon(":/iconos/icons/edit.png")
    self.boton_editar.setIcon(icono_editar)
    
    icono_borrar = QIcon(":/iconos/icons/delete.png")
    self.boton_borrar.setIcon(icono_borrar)

    layout.addWidget(self.boton_editar)
    layout.addWidget(self.boton_borrar)
    
  # Funcion o metodo para crear BD
  def crear_conexion(self):
    con = sqlite3.connect("hospital.db")
    
    self.mydb = con
    
    return self.mydb
  
  def click_editar(self):
    # Creamos una instancia de PacienteFormularioDialog
    self.editar_dialog = Ui_PacienteDialogUpdate(self.row_index, self.row_data)
    
    # Conectamos la señal de editar para recargar los datos de la tabla de paciente
    self.editar_dialog.datos_editados.connect(self.barraLateral.recargar_datos_pacientes)
    
    # Executamos el dialogo (formulario)
    self.editar_dialog.exec()

  def click_borrar(self):
    cur = self.crear_conexion().cursor()
    
    # Creamos un dialogo de confirmacion
    mensaje = QMessageBox.question(
      self, 'Confirmación',
      '¿Estas seguro que quieres borrar el paciente con poliza ' + self.paciente_poliza + '?',
      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    
    if mensaje == QMessageBox.StandardButton.Yes:
      consulta_borrar = f"DELETE FROM pacientes WHERE id='{self.paciente_id}'"
      cur.execute(consulta_borrar)
      self.mydb.commit()
      self.mydb.close()
      
      # Emitimos una señal (signal) para informar el cambio
      self.barraLateral.recargar_datos_pacientes()