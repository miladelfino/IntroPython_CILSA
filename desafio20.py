"""Implementar una clase Calculadora que defina los métodos:
Sumar, Restar, Multiplicar y Dividir
En lo posible realice tratamiento de excepciones.
Crear a continuación un programa que pruebe la clase Calculadora"""

print('Las operaciones permiten sólo dos numeros enteros.')
num1=input('Ingrese un número entero: ')
num2=input('Ingrese otro número entero: ')
operacion=str(input('Ingrese la operación que desea realizar'+ '\n' + '(Sumar, Restar, Multiplicar o Dividir) -->  '))

class Calculadora:
    def Sumar(self, num1, num2):
        try:
            print(num1+num2)
        except:
            print("Solo pueden ser utilizados dos números enteros")

    def Restar(self, num1, num2):
        try:
            print(num1-num2)
        except:
            print("Solo pueden ser utilizados dos números enteros")

    def Multiplicar(self, num1, num2):
        try:
            print(num1*num2)
        except:
            print("Solo pueden ser utilizados dos números enteros")

    def Dividir(self, num1, num2):
        try:
            print(num1/num2)
        except:
            print("Solo pueden ser utilizados dos números enteros")


calculadora= Calculadora()
if operacion=='Sumar' or operacion=='sumar':
    calculadora.Sumar(num1, num2);
elif operacion=='Restar' or operacion=='restar':
    calculadora.Restar(num1, num2);
elif operacion=='Dividir' or operacion=='dividir':
    calculadora.Dividir(num1, num2);
elif operacion=='Multiplicar' or operacion=='multiplicar':
    calculadora.Multiplicar(num1, num2);

# SI QUISIERA PROBAR CON NUMEROS QUE DEFINO YO:
"""calculadora.Sumar(num1, num2);
calculadora.Restar(num1, num2);
calculadora.Dividir(num1, num2)
calculadora.Multiplicar(num1, num2)"""
#REEMPLAZO NUM1 Y NUM2 POR LOS NÚMEROS Y ELIMINO EL INPUT DE LOS MISMOS AL PRINCIPIO