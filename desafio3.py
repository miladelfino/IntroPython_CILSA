"""Realizar un programa en el cual se ingrese un número entero e informe si es par.
En caso de que no sea par, también deberá informar al respecto."""

numero = int(input("Por favor ingrese un número:"))
if numero % 2 == 0:
    print(numero,"es un numero par")
else:
    print(numero,"no es un numero par");