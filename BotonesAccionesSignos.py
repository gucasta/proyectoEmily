from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QMessageBox)

import sqlite3
from signosFormularioUpdate import Ui_SignosDialogUpdate

# Clase de botones de accion de editar y borrar
class BotonesAccionWidgetSignos(QWidget):
  def __init__(self, row_index, row_data, barraLateral):
    super().__init__()
    
    # Almacenamos el indice de fila y sus datos como una instancia en variables
    self.row_index = row_index
    self.row_data = row_data
    self.barraLateral = barraLateral # Almacenamos una referencia a MenuBarraLateral
    
    # Obtenemos el numero de poliza del paciente
    self.signos_id = self.row_data[0]
    
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
    
    self.editar_dialog = Ui_SignosDialogUpdate(self.row_index, self.row_data)
    
    # Conectamos la señal de editar para recargar los datos de la tabla de signos
    self.editar_dialog.datos_editados.connect(self.barraLateral.recargar_datos_signos)
    
    # Executamos el dialogo (formulario)
    self.editar_dialog.exec()

  def click_borrar(self):
    cur = self.crear_conexion().cursor()
    
    # Creamos un dialogo de confirmacion
    mensaje = QMessageBox.question(
      self, 'Confirmación',
      '¿Estas seguro que quieres borrar los signos del paciente?',
      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    
    if mensaje == QMessageBox.StandardButton.Yes:
      consulta_borrar = f"DELETE FROM signos WHERE id='{self.signos_id}'"
      cur.execute(consulta_borrar)
      self.mydb.commit()
      self.mydb.close()
      
      # Emitimos una señal (signal) para informar el cambio
      self.barraLateral.recargar_datos_signos()