""" Un profesor debe cargar un conjunto de notas de exámenes.
Debemos realizar un programa que nos permita CARGAR un conjunto de notas 
de exámenes utilizando una LISTA.
Luego MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.
PD.: Usted define si el programa le solicita al usuario la cantidad de notas 
a cargar o que ingrese el valor 0 para finalizar la carga, por ejemplo."""

calificaciones=[]
nota=int(input("Ingrese la calificacion: "))

for num in range(nota):
    while nota <=10 and nota>=1:
        nota=int(input("Ingrese la calificacion: "))
        calificaciones.append(nota)

print("Las calificaciones de sus estudiantes son: ",calificaciones)


