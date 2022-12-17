'''Utilizar el código del desafío anterior trabajando los datos a través de un diccionario
Generar un archivo JSON con los datos del diccionario planteado.
Luego verificar el trabajo a partir de la lectura de dicho archivo y 
mostrarlo en un diccionario, es decir, levantar el archivo JSON desde mi código, 
convertirlo en diccionario y mostrar sus datos.'''

import json

diccionario= {}
contador=0

archivo = open('personas.csv')

for linea in archivo:
    personas = linea.split(',')
    #armo el diccionario
    datos = {
        'nombre': personas[0],
        'apellido': personas[1],
        'edad': personas[2],
        'barrio': personas[3]
    }
    diccionario["persona_" + str(contador)] = datos
    contador = contador + 1

del personas['persona_0']
archivo.close()

print(diccionario)

#guardo el diccionario en un archivo json
file= open('archivo.json', 'w')
json.dump(diccionario, archivo)
file = archivo.close()

#leo el archivo json
leer = open('archivo.json')
resultado=json.load(file)

leer.close()

print(resultado)
print(type(resultado))

