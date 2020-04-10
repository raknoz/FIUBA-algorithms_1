'''
Consigna:
    Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.

Pre-requisito:
    - Se deben ingresar solo número enteros positivos
'''

def dibujar_domino_custom(limite):
    for x in range (0,limite + 1):
        for h in range (x,limite + 1):
            print(f'|{x}|{h}|')


limite = int(input('Ingrese un número a fichas: '))
dibujar_domino_custom(limite)