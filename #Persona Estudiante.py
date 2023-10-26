#Persona Estudiante
from datetime import datetime

class Persona:
    def __init__(self, nombre, sexo, fecha_nacimiento):
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        self.calcular_edad()

    def calcular_edad(self):
        fecha_actual = datetime.now()
        self.edad = fecha_actual.year - self.fecha_nacimiento.year

class Estudiante(Persona):
    def __init__(self, nombre, sexo, fecha_nacimiento, matricula):
        super().__init__(nombre, sexo, fecha_nacimiento)
        self.matricula = matricula

    def mostrar_informacion(self):
        print("Nombre: " + self.nombre)
        print("Sexo: " + self.sexo)
        print("Edad: " + str(self.edad) + " años")
        print("Matrícula: " + self.matricula)

# Solicitar los datos del estudiante
nombre_estudiante = input("Ingresa el nombre del estudiante: ")
sexo_estudiante = input("Ingresa el sexo del estudiante (Hombre/Mujer/Otro): ")
fecha_nacimiento_estudiante = input("Ingresa la fecha de nacimiento del estudiante (YYYY-MM-DD): ")
matricula_estudiante = input("Ingresa la matrícula del estudiante: ")

# Crear una instancia de Estudiante
estudiante = Estudiante(nombre_estudiante, sexo_estudiante, fecha_nacimiento_estudiante, matricula_estudiante)

# Mostrar la información del estudiante
estudiante.mostrar_informacion()
