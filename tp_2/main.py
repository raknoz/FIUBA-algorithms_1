from tkinter import *
import gamelib
import soko
import pprint

#Diccionarios de información
D_MOVIMIENTOS = {}
D_NIVELES = {}
D_DIRECCIONES = {'NORTE':(0, -1), 'SUR':(0, 1), 'ESTE':(1, 0), 'OESTE':(-1, 0)}
D_OPCIONES = {}

#Tamaño de la imagen
IMG_PX = 64

def path_to_img(argument): 
    switcher = { 
        '#': 'img_v2/wall.png', 
        '*': 'img_v2/box_goal.png', 
        '@': 'img_v2/ground_player.png', 
        ' ': 'img_v2/ground.png',
        '$': 'img_v2/box.png',
        '.': 'img_v2/ground_goal.png',
        '+': 'img_v2/player_goal.png',
    }
    return switcher.get(argument, 'img/ground.gif')

def cargar_configuracion_teclas():
    ''' Función que se encarga de cargar la configuración de las teclas '''
    #Lectura del archivo de teclas y armado del diccionario
    D_MOVIMIENTOS['Up'] = 'NORTE'
    D_MOVIMIENTOS['Left'] = 'OESTE'
    D_MOVIMIENTOS['Down'] = 'SUR'
    D_MOVIMIENTOS['Right'] = 'ESTE'
    D_OPCIONES['Escape'] = 'SALIR'
    D_OPCIONES['r'] = 'REINICIAR'

def cargar_configuracion_niveles():
    ''' Función que se encarga de cargar la configuración de los niveles '''
    D_NIVELES[1] = [
        'Level 1', 
        '####', 
        '# .#', 
        '#  ###', 
        '#*@  #', 
        '#  $ #', 
        '#  ###', 
        '####']
            
def juego_actualizar(tablero, tecla):
    ''' Actualizar el estado del juego x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda del tablero; 
    en ese caso determina el nuevo estado del juego y lo devuelve.'''
    
    t_coordenadas = D_DIRECCIONES.get(D_MOVIMIENTOS.get(tecla))
    tablero = soko.mover(tablero, t_coordenadas)
    if soko.juego_ganado(tablero):
        gamelib.title('Ganó!!!!!!!!!!!!!')
    return tablero

def juego_mostrar(tablero):
    ''' Función que se encarga de dibujar en pantalla el tablero '''
    #tablero =  D_NIVELES.get(1)[1::]
    for ir, row in enumerate(tablero):
        for ic, col in enumerate(row):
            img = path_to_img(col)
            gamelib.draw_image(img, ic * IMG_PX, ir * IMG_PX)

def main():
  
    #1 Carga los niveles
    cargar_configuracion_niveles()

    #2 Carga de teclas
    cargar_configuracion_teclas()
    
    #3 Inicio de partida
    tablero = soko.crear_grilla(D_NIVELES.get(1)[1::])
    original = soko.copiar_grilla(tablero)
    gamelib.resize(400, 500)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(tablero)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        # Actualizar el estado del juego, según la `tecla` presionada
        
        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'REINICIAR':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            tablero = original

        if tecla in D_MOVIMIENTOS.keys():
            tablero = juego_actualizar(tablero, tecla)

gamelib.init(main)