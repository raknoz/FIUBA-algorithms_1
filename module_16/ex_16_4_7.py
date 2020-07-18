'''
Consigna:
    Escribir una función llamada tail que recibe un archivo y un número N e imprime las últimas N líneas del archivo. 
    Durante el transcurso de la función no puede haber más de N líneas en memoria.
'''
from Cola import Cola

def tail(arch, n):
    ''' recibe un archivo y un número N e imprime las últimas N líneas del archivo. '''
    fila = Cola()

    with open(arch, 'r') as f:
        limite = 0
        print(f'inicio -> {limite}')
        for linea in f:
            if limite < n:
                fila.encolar(linea)
                limite +=1
                print(f'if -> {limite}')
            else:
                print('Else')
                fila.desencolar()
                fila.encolar(linea)
    
    print(fila)