'''
Consigna:
    Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula
    a utilizar es: C * ((1 + (X/100)) ** N)

Pre-requesitos: 
    - Los numeros ingresados deben ser positivos.
'''

def calculoInteres(capital, tasa, tiempo):
    print('El monto final a obtener es: {}'.format(capital * ((1 + (tasa/100)) ** tiempo)))

capital = float(input('Ingrese el monto del capital: '))
tasa = float(input('Ingrese el monto del tasa de interes: '))
tiempo = float(input('Ingrese el tiempo a calcular: '))
calculoInteres(capital, tasa, tiempo)