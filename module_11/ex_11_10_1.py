'''
Consigna:
    Escribir una función, llamada head que reciba un archivo y un número N e imprima las primeras N líneas del archivo.
'''

def abrir(_file, _mode):
    '''
        Función que abre un archivo en el modo en que se le indique.
    '''
    return open(_file, _mode)

def head(n, arch):
    '''
        Función que recibe el nombre de un archivo y un N e imprime los N números de línea de ese archivo.
        Pre: El archivo (arch) tiene que existir.
    '''
    with abrir(arch, "w") as f:
        for i, linea in enumerate(arch):
            linea = linea.rstrip('\n')
            print(f'{i}: {linea}')
