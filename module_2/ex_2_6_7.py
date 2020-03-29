'''
Consigna:
    Escribir un programa que tome una cantidad m de valores ingresados por el usuario, a cada uno le calcule el factorial e imprima el resultado junto con el número de orden
    correspondiente.

Pre-requisitos:
    - Se deben ingresar numero enteros positivos mayores a 0.
    - El valor de corte es ingresando -1
'''

def calcularFactorial(num):
    if(num == 1):
        return 1    
    return num * calcularFactorial(num -1)

def procesaLista(valores):
    if(len(valores) == 0):
        return print('Sin numeros para calcular!')
    
    for pos in range(len(valores)):
        print('Posicion {} => el factorial de {} es {} '.format(pos, valores[pos], calcularFactorial(valores[pos])))
            
def cargaValores():
    valores = []
    num = int(input('Ingrese un número para calcular factorial (-1 para salir): '))
    while(num > -1 and num > 0):
        valores.append(num)
        num = int(input('Ingrese otro número para calcular factorial (-1 para salir): '))
    
    procesaLista(valores)
        
    
cargaValores()