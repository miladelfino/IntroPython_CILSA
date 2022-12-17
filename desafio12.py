"""A partir del desafío anterior, modificar el programa para que pueda 
cargar el nombre y la nota de cada alumno.
Luego debo informar el nombre y la nota tanto de los aprobados como de los desaprobados.

Si es posible utilizar Diccionario."""

alumnos={
    "Nombre":[],
    "Calificacion":[]
    }

cantidad=3
i=0

for i in range(cantidad):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    calificacion= input("Calificacion: ")
    alumnos["Nombre"].append(nombre)
    alumnos["Calificacion"].append(calificacion)

for i in range(cantidad):
    print("Nombres: ", alumnos["Nombre"][i])
    print("Calificacion: ", alumnos["Calificacion"][i])
