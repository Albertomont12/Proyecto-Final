#Datos que recopilan para saber tu edad
# Solicitar los datos del usuario
nombre = input("Por favor, ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (Hombre/Mujer/Otro): ")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")

# Calcular la edad
from datetime import datetime

fecha_actual = datetime.now()
fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
edad = fecha_actual.year - fecha_nacimiento.year

# Determinar si es mayor de edad
mayor_de_edad = edad >= 18

# Imprimir los resultados
print("Nombre: " + nombre)
print("Sexo: " + sexo)
print("Edad: " + str(edad) + " años")

if mayor_de_edad:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")