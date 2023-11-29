"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from base_datos import client

#Colección general
db = client.tarea04

#Colecciones necesarias
coleccion_matricula_estudiante = db.matriculas_estudiantes
coleccion_matricula_vehiculo = db.matriculas_vehiculos

#Consultas
#Colección "MatriculaEstudiante"
data_matricula_estudiante_01 = coleccion_matricula_estudiante.find_one({'nombre':'Juan'})

#Colección "MatriculaVehiculo"
data_matricula_vehiculo_01 = coleccion_matricula_vehiculo.find_one({'propietario':'Melissa Cortez'})

print(data_matricula_estudiante_01)
print(data_matricula_vehiculo_01)
