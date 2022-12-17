"""Desarrollar una función que reciba el nombre de una persona y un valor entero.
Si el valor entero es 0, imprimirá: "hola" y el nombre
Si el valor entero es distinto de 0, imprimirá: "chau" y el nombre
La función debe contemplar el tratamiento de excepciones"""

nombre= str(input("Ingrese su nombre: "))
num= input("Ingrese un numero entero: ")

def saludo(num, nombre):
    try:
        if num == 0:  
            print("hola", nombre) 
        elif num > 0:
            print("chau", nombre)
    except:
        print("El valor ingresado no es válido, intentelo nuevamente.")

saludo(num, nombre)