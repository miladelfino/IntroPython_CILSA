"""Realizar un programa en el cual se ingresen dos números e informe 
si el primero es múltiplo del segundo.
En caso contrario deberá generar un mensaje adecuado."""

numero1 = int(input("Ingrese un número:"))
numero2 = int (input("Ingrese otro número:"))

if numero1%numero2 != 0: 
    print(numero1,"no es multiplo de",numero2)
else:
    print(numero1,"es multiplo de",numero2)