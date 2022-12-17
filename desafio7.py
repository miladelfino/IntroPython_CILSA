"""Realizar un programa en el cual se ingresen números enteros 
y se obtenga el mayor de ellos.
Se desconoce cuántos números serán ingresados, pero se sabe que cuando 
se ingrese el valor 0, el programa finalizará indicando el máximo número cargado."""  

array=list()
i=0
max=0
num=int(input("Ingrese un número entero: "))
while num != 0:
    array.insert(i, num)
    num=int(input("Ingrese un número entero: ")) 
    i= i+1

for num in array:
    if num>max:
        max=num

print("El mayor numero ingresado es: ", max)
