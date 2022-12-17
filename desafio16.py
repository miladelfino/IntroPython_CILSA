"""Desarrollar una función que realice la división de dos números, 
en caso de ser posible devuelve el resultado.
La función debe contemplar el tratamiento de excepciones para cuando 
ingrese una letra en lugar de un número y para cuando la división sea por 0.
Realizar un programa que valide el comportamiento de la función."""


"""dividendo=input("Ingrese el número que desea dividir: ")
divisor= input("Ingrese el número por el que quiere dividirlo: ")"""

def div (dividendo, divisor):
    try:
        result= dividendo/divisor
        print("El resultado de la division es: ",result)
    except ZeroDivisionError: 
        print("No pueden realizarse divisiones por 0.")
    except TypeError:
        print ("El valor ingresado no es válido, intentelo nuevamente.")

div(12, 6)
div(12, 0)
div("a", 6)