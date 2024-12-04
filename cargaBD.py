import sqlite3

class CargaBD():
  def __init__(self):
    self.crea_tablas()
    self.carga_tabla_sintomas()
    
  def conexion_sqlite(self):
    con = sqlite3.connect("hospital.db")
    
    self.mydb = con
    
    return self.mydb
    
  def crea_tablas(self):
    cur = self.conexion_sqlite().cursor()
    
    consulta_crear_tabla_pacientes = """
      CREATE TABLE IF NOT EXISTS "pacientes" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "fecha" TEXT,
        "poliza" TEXT,
        "nombre" TEXT,
        "apellidos" TEXT,
        "edad" INT,
        "genero" TEXT
      );
    """
    
    cur.execute(consulta_crear_tabla_pacientes)
    
    consulta_crear_tabla_signos = f"""
    CREATE TABLE IF NOT EXISTS "signos" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "peso" REAL,
      "estatura" REAL,
      "sistolica" INT,
      "diastolica" INT,
      "oxigenacion" INT,
      "temperatura" REAL,
      "frecuencia" INT,
      "idPaciente" integer(11) NOT NULL,
      CONSTRAINT "fk_signos_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE
    );
    """
    
    cur.execute(consulta_crear_tabla_signos)
    
    consulta_crear_tabla_sintomas = f"""
      CREATE TABLE IF NOT EXISTS "sintomas" (
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nombre" TEXT,
        "valor" integer
      );
    """
    
    cur.execute(consulta_crear_tabla_sintomas)
    
    consulta_crear_tabla_pacientes_sintomas = f"""
      CREATE TABLE IF NOT EXISTS "pacientes_sintomas" (
        "idPaciente" integer(11) NOT NULL,
        "idSintoma" integer(11) NOT NULL,
        CONSTRAINT "fk_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT "fk_sintoma" FOREIGN KEY ("idSintoma") REFERENCES "sintomas" ("id") ON DELETE CASCADE ON UPDATE CASCADE
      );
    """
    
    cur.execute(consulta_crear_tabla_pacientes_sintomas)
    
    consulta_crear_tabla_diagnostico = f"""
      CREATE TABLE IF NOT EXISTS "diagnosticos" (
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "diagnostico" TEXT,
        "observaciones" TEXT,
        "idPaciente" integer(11) NOT NULL,
        CONSTRAINT "fk_diagnostico_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE
      );
    """
    
    cur.execute(consulta_crear_tabla_diagnostico)
    
    consulta_crear_tabla_tratamiento = f"""
      CREATE TABLE IF NOT EXISTS "tratamientos" (
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "fecha" TEXT,
        "duracion" integer,
        "indicaciones" TEXT,
        "observaciones" TEXT,
        "idDiagnostico" integer NOT NULL,
        CONSTRAINT "fk_tratamiento_diagnostico" FOREIGN KEY ("idDiagnostico") REFERENCES "diagnosticos" ("id") ON DELETE CASCADE ON UPDATE CASCADE
      );
    """
    
    cur.execute(consulta_crear_tabla_tratamiento)
    
    self.mydb.commit()
    self.mydb.close()
    
  def carga_tabla_sintomas(self):
    con = self.conexion_sqlite()
    cur = con.cursor()
    
    consulta_existen_sintomas = f"""
      SELECT * FROM sintomas LIMIT 1
    """
    
    cur.execute(consulta_existen_sintomas)
    existe = cur.fetchall()
    
    if not existe:
      consulta_carga_datos_sintomas = f"""
        INSERT INTO sintomas (id, nombre, valor) 
        VALUES 
          (1, 'tos', 3),
          (2, 'fatiga', 4),
          (3, 'vomito', 5),
          (4, 'dolor_garganta', 6),
          (5, 'diarrea', 7),
          (6, 'dolor_cabeza', 8),
          (7, 'fiebre', 9),
          (8, 'dolor_abdominal', 10),
          (9, 'contusion', 11),
          (10, 'deshidratacion', 12),
          (11, 'perdida_vision', 15),
          (12, 'quemadura', 18),
          (13, 'dificultad_respirar', 25),
          (14, 'dolor_pecho', 30),
          (15, 'hemorragia', 35),
          (16, 'perdida_concienta', 40);
      """
      
      cur.execute(consulta_carga_datos_sintomas)
      con.commit()
      
    con.close()
    
class ObtenerDatosBD():
  def conexion_sqlite(self):
    con = sqlite3.connect("hospital.db")
    
    self.mydb = con
    
    return self.mydb
  
  def obtener_pacientes(self):
    con = self.conexion_sqlite()
    cur = con.cursor()
    
    consulta_obtener_pacientes = f"""
      SELECT id, poliza, nombre, apellidos FROM pacientes
    """
    
    cur.execute(consulta_obtener_pacientes)
    registros = cur.fetchall()
    
    return registros