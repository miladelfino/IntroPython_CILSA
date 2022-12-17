"""Retomar el ejercicio del desafío anterior pero solo CARGAR en la LISTA 
aquellas notas que estén entre 6 y 10 (inclusive).

MOSTRAR el contenido de cada uno de los valores que existen en la LISTA."""

nota=int(input("Ingrese la calificacion: "))
aprobados=[]

for num in range(nota): 
    while nota <=10 and nota >=6: 
        nota=int(input("Ingrese la calificacion: ")) 
        aprobados.append(nota)
    else:
        print("Este alumno no está aprobado")

print("Las calificaciones de sus estudiantes APROBADOS son: ",aprobados)
