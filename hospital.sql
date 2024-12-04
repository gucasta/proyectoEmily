-- ----------------------------
-- Table structure for diagnosticos
-- ----------------------------
DROP TABLE IF EXISTS "diagnosticos";
CREATE TABLE "diagnosticos" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "diagnostico" TEXT,
  "observaciones" TEXT,
  "idPaciente" integer(11) NOT NULL,
  CONSTRAINT "fk_diagnostico_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------
-- Table structure for pacientes
-- ----------------------------
DROP TABLE IF EXISTS "pacientes";
CREATE TABLE "pacientes" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fecha" TEXT,
  "poliza" TEXT,
  "nombre" TEXT,
  "apellidos" TEXT,
  "edad" INT,
  "genero" TEXT
);

-- ----------------------------
-- Table structure for pacientes_sintomas
-- ----------------------------
DROP TABLE IF EXISTS "pacientes_sintomas";
CREATE TABLE "pacientes_sintomas" (
  "idPaciente" integer(11) NOT NULL,
  "idSintoma" integer(11) NOT NULL,
  CONSTRAINT "fk_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "fk_sintoma" FOREIGN KEY ("idSintoma") REFERENCES "sintomas" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------
-- Table structure for signos
-- ----------------------------
DROP TABLE IF EXISTS "signos";
CREATE TABLE "signos" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "peso" INT,
  "estatura" INT,
  "sistolica" INT,
  "diastolica" INT,
  "oxigenacion" INT,
  "temperatura" INT,
  "frecuencia" INT,
  "idPaciente" integer(11) NOT NULL,
  CONSTRAINT "fk_signos_paciente" FOREIGN KEY ("idPaciente") REFERENCES "pacientes" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------
-- Table structure for sintomas
-- ----------------------------
DROP TABLE IF EXISTS "sintomas";
CREATE TABLE "sintomas" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "nombre" TEXT,
  "valor" integer
);

-- ----------------------------
-- Records of sintomas
-- ----------------------------
INSERT INTO "sintomas" VALUES (1, 'tos', 3);
INSERT INTO "sintomas" VALUES (2, 'fatiga', 4);
INSERT INTO "sintomas" VALUES (3, 'vomito', 5);
INSERT INTO "sintomas" VALUES (4, 'dolor_garganta', 6);
INSERT INTO "sintomas" VALUES (5, 'diarrea', 7);
INSERT INTO "sintomas" VALUES (6, 'dolor_cabeza', 8);
INSERT INTO "sintomas" VALUES (7, 'fiebre', 9);
INSERT INTO "sintomas" VALUES (8, 'dolor_abdominal', 10);
INSERT INTO "sintomas" VALUES (9, 'contusion', 11);
INSERT INTO "sintomas" VALUES (10, 'deshidratacion', 12);
INSERT INTO "sintomas" VALUES (11, 'perdida_vision', 15);
INSERT INTO "sintomas" VALUES (12, 'quemadura', 18);
INSERT INTO "sintomas" VALUES (13, 'dificultad_respirar', 25);
INSERT INTO "sintomas" VALUES (14, 'dolor_pecho', 30);
INSERT INTO "sintomas" VALUES (15, 'hemorragia', 35);
INSERT INTO "sintomas" VALUES (16, 'perdida_concienta', 40);

-- ----------------------------
-- Table structure for tratamientos
-- ----------------------------
DROP TABLE IF EXISTS "tratamientos";
CREATE TABLE "tratamientos" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fecha" TEXT,
  "duracion" integer,
  "indicaciones" TEXT,
  "observaciones" TEXT,
  "idDiagnostico" integer NOT NULL,
  CONSTRAINT "fk_tratamiento_diagnostico" FOREIGN KEY ("idDiagnostico") REFERENCES "diagnosticos" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
