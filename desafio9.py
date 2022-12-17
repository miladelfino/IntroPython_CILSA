"""Implementar control de excepciones a partir 
del programa desarrollado en el desafío anterior."""


mayor= 1 

num= int(input("Ingrese un número entero: "))
try:
    while num!=0:
        num=int(input("Ingrese un número entero: "))
        if num>mayor:
            mayor=num  
    print("El mayor numero ingresado es: ", mayor)
except:
    print("El numero ingresado no es válido, intente de nuevo.")