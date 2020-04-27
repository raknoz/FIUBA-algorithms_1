'''
Consigna:
    Escribir un programa que tome una cantidad m de valores ingresados por el usuario, a cada uno le calcule el factorial e imprima el resultado junto con el número de orden
    correspondiente.
'''

def calcular_factorial(num):
    '''
        Función que hace el cálculo del factorial recursivamente.
    '''
    if num == 1:
        return 1    
    return num * calcular_factorial(num -1)

def procesa_lista(valores):
    '''
        Procedimiento que procesa los datos ingresados por paŕametro.
    '''
    if not len(valores):
        return print('Sin numeros para calcular!')
    
    for pos, val in enumerate(valores):
        print(f'Posicion {pos} => el factorial de {val} es {calcular_factorial(val)} ')
            
def carga_valores():
    '''
        Procedimiento que pide los datos para procesar al usuario.
    '''
    valores = []
    num = int(input('Ingrese un número para calcular factorial (-1 para salir): '))
    while num > -1 and num > 0:
        valores.append(num)
        num = int(input('Ingrese otro número para calcular factorial (-1 para salir): '))
    
    procesa_lista(valores)
        
carga_valores()