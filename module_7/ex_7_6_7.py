'''
Consigna:
    Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
    nombre, luego la inicial con un punto, y luego el apellido.
'''

def procesa_lista_nombres(l):
    result = []

    for n, a, i in l:
        result.append(f'{n} {i}. {a}')

    return result

def imprime_nombres_formato(l):
    '''
        Recibe una lista de tuplas y formatea el contenido.
    '''
    for e in procesa_lista_nombres(l):
        print(e)
    

imprime_nombres_formato([('David', 'Gomez', 'H')])