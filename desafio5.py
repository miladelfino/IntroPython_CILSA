""" Realizar un programa en el cual se ingrese:
1) El límite inferior de un intervalo
2) El límite superior del mismo intervalo
3) Un valor entero
Indicar si el valor entero ingresado en el punto 3 se encuentra 
dentro del intervalo definido por los valores del punto (1) y del punto (2)."""

limiteInferior= int(input("Ingrese el límite inferior del intervalo: "));
limiteSuperior= int(input("Ingrese el límite superior del intervalo: "));
numero= int(input("Ingrese un número entero a evaluar: "));

if numero<=limiteSuperior and numero>=limiteInferior:
    print("El número ingresado se encuentra dentro del intervalo")
else:
    print("El número ingresado NO se encuentra dentro del intervalo");