"""Realizar un programa que cargue 4 personas con sus datos: nombre, apellido y edad.
Se debe almacenar en un diccionario y luego, recorrer ese diccionario y 
escribir en un archivo con extensión txt o csv.
Los datos de cada Persona, debe estar separado por comas. 
Por Ejemplo: juan,perez,19"""

personas={}

for i in range(4):
    datos=[]
    nombre=input("Ingrese el nombre de la persona: ")
    apellido=input("Ingrese el apellido de la persona: ")
    edad=input("Ingrese la edad de la persona: ")
    datos.append(nombre)
    datos.append(apellido)
    datos.append(edad)
    personas[nombre+","+apellido+","+edad]= datos

archivo = open("datos.txt", "w")

for persona in personas:
    archivo.write(",".join(personas[persona]) + "\n" )

archivo.close()

"""para leer los datos dentro del archivo"""
archivo = open("datos.txt", "r")

contador=1
for datos in personas:
    print("Persona",contador,": ", datos)
    contador= contador+1

archivo.close()
