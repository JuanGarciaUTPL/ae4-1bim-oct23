"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from base_datos import client

# Se obtiene la colección general
db = client.tarea04

# Se crea la colección "MatriculaEstudiante"
coleccion_matricula_estudiante = db.matriculas_estudiantes

# Se crea la colección "MatriculaVehiculo"
coleccion_matricula_vehiculo = db.matriculas_vehiculos

# Se agregan datos a la colección "MatriculaEstudiante"
data_matricula_estudiante_01 = {
  "nombre": "Melissa",
  "apellidos": "Cortez",
  "cedula": "0987654321",
  "fecha_nacimiento": "1982-10-09",
  "carrera": "Comunicadora",
  "año_ingreso": 2000
}

coleccion_matricula_estudiante.insert_one(data_matricula_estudiante_01)

# Se agregan datos a la colección "MatriculaVehiculo"
data_matricula_vehiculo_01 = {
  "placa": "GFD0987",
  "marca": "Volswagen",
  "modelo": "gol",
  "año_fabricacion": 2011,
  "propietario": "Melissa Cortez",
  "cedula": "0987654321"
}

coleccion_matricula_vehiculo.insert_one(data_matricula_vehiculo_01)
