"""Retomar el desafío anterior e indicar cuantos y que DNI 
superan el valor de 40 millones."""

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
    if int(dni) > 40000000:
        personas["Nombre"].append(nombre)
        personas["Apellido"].append(apellido)
        personas["DNI"].append(dni)

for i in range(len(personas["DNI"])):
    print("Los DNI mayores a 40millones son: ")
    print("Nombre: ", personas["Nombre"][i])
    print("Apellido: ", personas["Apellido"][i])
    print("DNI: ", personas["DNI"][i])
        