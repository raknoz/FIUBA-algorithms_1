'''
Consigna:
    Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.
'''

def dibujar_domino_custom(limite):
    '''
        Función que imprime el dominó hasta el limite indicado.
    '''
    for x in range (0,limite + 1):
        for h in range (x,limite + 1):
            print(f'|{x}|{h}|')


def main():
    '''
        Función principal que le pide los datos al usuario.
    '''
    limite = int(input('Ingrese un número a fichas: '))
    dibujar_domino_custom(limite)
