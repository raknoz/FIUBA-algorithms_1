from tkinter import *
import gamelib

CASILLERO_VACIO = ' '
TOTAL_FILAS = 10
TOTAL_COLUMNAS = 10
JUGADOR_X = 'X'
JUGADOR_O = 'O'

# Inicio funciones propias #

def obtener_tablero(juego):
    '''Devuelve el tablero de la matriz'''
    return juego['tablero']

def obtener_jugador(juego):
    '''Devuelve el jugador de la matriz'''
    return juego['jugador']

def obtener_siguiente(juego):
    '''Devuelve el siguiente jugador de acuerdo a cual fue el anterior'''
    return JUGADOR_X if obtener_jugador(juego) == JUGADOR_O else JUGADOR_O

def casillero_vacio(juego, x, y):
    '''Devuelve True or False dependiendo de si el casillero está vacío o no'''
    return obtener_tablero(juego)[y][x] == CASILLERO_VACIO

def es_posicion_valida(x, y):
    '''Devuelve que los parámetros x e y estén dentro de los límites'''
    return x < TOTAL_COLUMNAS and y < TOTAL_FILAS

# Fin funciones propias #

def juego_crear():
    """Inicializar el estado del juego"""
    juego = {}
    tablero = []
    for f in range(TOTAL_FILAS):
        fila = []
        for c in range(TOTAL_COLUMNAS):
            fila.append(CASILLERO_VACIO)
        tablero.append(fila)
    
    juego['tablero'] = tablero
    juego['jugador'] = JUGADOR_X
    return juego

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    return juego

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(300, 300)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)