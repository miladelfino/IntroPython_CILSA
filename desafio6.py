""" Realizar un programa donde se ingresen 5 números e informe el 
promedio de los números ingresados.
Nota: utilizar estructuras repetitivas."""

datos=0
sum=0
while datos<=5: 
    datos=int(input("Ingrese un número: "))
    datos=datos+1
    sum= sum+datos
print("El promedio de los datos ingresados es ",sum/5)
