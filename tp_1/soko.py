PARED = '#'
CAJA = '$' 
JUGADOR = '@' 
OBJETIVO = '.'
OBJETIVO_CAJA = '*'
OBJETIVO_JUGADOR = '+'
VACIO = ' '

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
    return grilla[f][c] in (OBJETIVO, OBJETIVO_CAJA, OBJETIVO_JUGADOR)

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return  grilla[f][c] in (CAJA, OBJETIVO_CAJA)

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] in (JUGADOR, OBJETIVO_JUGADOR)

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for r in grilla:
        if CAJA in r or OBJETIVO_JUGADOR in r:
            return False
    return True

def buscar_jugador(grilla):
    '''
        Función que devuelve la posición del jugador en la grilla.
    '''
    for i, f in enumerate(grilla):
        for k, c in enumerate(f):
            if hay_jugador(grilla, k, i):
                return grilla[i][k], i, k

def copiar_grilla(grilla):
   return [row[:] for row in grilla]

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
    n_grilla = copiar_grilla(grilla)
    # 1 - busco y retorno jugador, fila y columna.
    j, f, c = buscar_jugador(n_grilla)
    # 2 - obtengo nueva posición + direccion.
    nf, nc = f + direccion[1], c + direccion[0]
   
    # Si la posición a moverme es una pared retorno la misma grilla.
    if hay_pared(n_grilla, nc, nf):
        return n_grilla
    
    if hay_caja(n_grilla, nc, nf):
        cf, cc = nf + direccion[1], nc + direccion[0]
        if hay_pared(n_grilla, cc, cf) or hay_caja(n_grilla, cc, cf):
            return n_grilla
        
        caja = n_grilla[nf][nc]        
        if n_grilla[cf][cc] == VACIO:
            n_grilla[cf][cc] = CAJA
        elif n_grilla[cf][cc] == OBJETIVO:
            n_grilla[cf][cc] = OBJETIVO_CAJA
        
        n_grilla[nf][nc] = OBJETIVO if caja == OBJETIVO_CAJA else VACIO

    e = n_grilla[nf][nc]
    # Si la posición a moverme está vacia me muevo.
    if e == VACIO:
        n_grilla[nf][nc] = JUGADOR
        # Si soy jugador actualizo con vacío sino en su lugar pongo un objetivo.
        n_grilla[f][c] = VACIO if j == JUGADOR else OBJETIVO
        return n_grilla
    
    if hay_objetivo(n_grilla, nc, nf):
        n_grilla[nf][nc] = OBJETIVO_JUGADOR
        # Si soy jugador actualizo con vacío sino en su lugar pongo un objetivo.
        n_grilla[f][c] = VACIO if j == JUGADOR else OBJETIVO
        return n_grilla

    return n_grilla
