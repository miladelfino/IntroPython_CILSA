"""Desarrollar un 
programa que cree un diccionario con nombres, apellidos y DNIs.

A continuación, se deberá ingresar 3 personas con los datos y 
al final informar su contenido por cada persona."""

personas={
    "Nombre":[],
    "Apellido":[],
    "DNI":[]
    }

cantidad=3
i=0

for i in range(cantidad):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    apellido= input("Apellido: ")
    dni=input("DNI: ")
    personas["Nombre"].append(nombre)
    personas["Apellido"].append(apellido)
    personas["DNI"].append(dni)

for i in range(cantidad):
    print("Nombre: ", personas["Nombre"][i])
    print("Apellido: ", personas["Apellido"][i])
    print("DNI: ", personas["DNI"][i])

