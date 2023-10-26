#Materias
class Materia:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

class Estudiante:
    def __init__(self, nombre, matricula, fecha_nacimiento):
        self.nombre = nombre
        self.matricula = matricula
        self.fecha_nacimiento = fecha_nacimiento
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_promedio_final(self):
        total_calificaciones = 0
        cantidad_materias = 0
        for materia in self.materias:
            total_calificaciones += sum(materia.calificaciones)
            cantidad_materias += len(materia.calificaciones)
        if cantidad_materias == 0:
            return 0
        else:
            return total_calificaciones / cantidad_materias

# Crear materias para el estudiante
materia1 = Materia("Matemáticas", [90, 85, 88])
materia2 = Materia("Historia", [78, 92, 87])
materia3 = Materia("Ciencias", [95, 91, 89])

# Crear un estudiante con nombre, matrícula y fecha de nacimiento
estudiante = Estudiante("Kevin Alberto", "22IS011", "2005-07-09")
estudiante.agregar_materia(materia1)
estudiante.agregar_materia(materia2)
estudiante.agregar_materia(materia3)

# Obtener el promedio final del estudiante
promedio_final = estudiante.obtener_promedio_final()
print(f"Nombre: {estudiante.nombre}")
print(f"Matrícula: {estudiante.matricula}")
print(f"Fecha de Nacimiento: {estudiante.fecha_nacimiento}")
print(f"Promedio Final: {promedio_final}")