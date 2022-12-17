"""Realizar un programa en el cual se ingresen números enteros 
y se obtenga el mayor de ellos.
Se desconoce cuántos números serán ingresados, pero se sabe que cuando 
se ingrese el valor 0, el programa finalizará indicando el máximo número cargado.
USANDO SOLO WHILE"""

mayor= 1 
num= int(input("Ingrese un número entero: "))
while num!=0:
    num=int(input("Ingrese un número entero: "))
    if num>mayor:
        mayor=num
        num=int(input("Ingrese un número entero: "))
    
print("El mayor numero ingresado es: ", mayor)