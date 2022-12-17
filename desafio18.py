"""El desafío será realizar un pequeño filtrado de información, en el cual el usuario podrá filtrar los datos de las personas, al menos, por la edad.
Para esto vamos a tener que leer nuestro archivo personas.csv y se le pedirá al usuario que ingrese el rango de edades, es decir, la edad menor y la edad mayor, para que luego devuelva los datos completos de las personas entre esa edad.

Tener en cuenta:
El archivo personas.csv tiene en su primera fila los encabezados de los datos, así que quítelos al momento de trabajarlo en Python. Por ejemplo, si voy a manejar listas, utilizando el nombre.pop(0) elimino ese encabezado."""

nombres = []
apellidos = []
edades = []
barrios = []

#puedo agregr el try aca para manejo de excepciones
# abro el archivo
archivo = open("personas.csv","r")

for linea in archivo:
    personas = linea.split(",")
    nombres.append(personas[0])
    apellidos.append(personas[1])
    edades.append(personas[2])
    barrios.append(personas[3].strip("\n"))

archivo.close()

nombres.pop(0)
apellidos.pop(0)
edades.pop(0)
barrios.pop(0)

#ingreso datos del rango
min= int(input("Ingrese la edad mínima: "))
max= int(input("Ingrese la edad máxima: "))

print("Las personas que se encuentran dentro de ese rango son: ")
for i in range(len(edades)):
    edad = int(edades[i])
    if min <= edad <= max:
        print("Nombre:", nombres[i])
        print("Apellido:", apellidos[i])
        print("Edad:", edades[i])
        print("Barrio:", barrios[i]+ "\n")

#agrego except para cuando el archivo no es correcto, o el dano no es num entero, etc.

