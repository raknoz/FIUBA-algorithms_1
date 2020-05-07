OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

PARED = '#'
CAJA = '$' 
JUGADOR = '@' 
OBJETIVO = '.'
OBJ_CAJA = '*'
OBJ_JUGADOR = '+'

def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''
    matrix = []
    for r in desc:
        row = []
        for e in r:
            row.append(e)
        matrix.append(row)
    
    return matrix

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    if len(grilla) == 0:
        return (0, 0)
    return len(grilla[0]), len(grilla)
    
def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return PARED == grilla[f][c]

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] in (OBJETIVO, OBJ_CAJA, OBJ_JUGADOR)

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return  grilla[f][c] in (CAJA, OBJ_CAJA)

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] in (JUGADOR, OBJ_JUGADOR)

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for r in grilla:
        if CAJA in r or OBJ_JUGADOR in r:
            return False
    return True

def buscar_jugador(grilla):
    '''
        Función que devuelve la posición del jugador en la grilla.
    '''
    for f in range(1, grilla):
        for c in range(1, f):
            if grilla[f][c] in (JUGADOR, OBJ_JUGADOR):
                return f, c


def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    return grilla