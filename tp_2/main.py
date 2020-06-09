from tkinter import *
import gamelib
import soko

D_TECLAS = {}
D_NIVELES = {}

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)
SALIR = ''
REINICIAR = ''
#Tamaño de la imagen
IMG_PX = 64

def path_to_img(argument): 
    switcher = { 
        '#': 'img/wall.gif', 
        '*': 'img/box.gif', 
        '@': 'img/player.gif', 
        ' ': 'img/ground.gif',
        '$': 'img/goal.gif',
    }
    return switcher.get(argument, 'img/ground.gif')

def cargar_configuracion_teclas():
    ''' Función que se encarga de cargar la configuración de las teclas '''
    #Lectura del archivo de teclas
    D_TECLAS['Up'] = NORTE
    D_TECLAS['Left'] = OESTE
    D_TECLAS['Down'] = SUR
    D_TECLAS['Right'] = ESTE

def cargar_configuracion_mapas():
    ''' Función que se encarga de cargar la configuración de las teclas '''
    D_NIVELES[1] = [
        ['Level 1'], 
        ['#','#','#','#'], 
        ['#',' ','.','#'], 
        ['#',' ',' ','#','#','#'], 
        ['#','*','@',' ',' ','#'], 
        ['#',' ',' ','$',' ','#'], 
        ['#',' ',' ','#','#','#'], 
        ['#','#','#','#']]
            
def juego_actualizar(juego, tecla):
    ''' Actualizar el estado del juego x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda del tablero; 
    en ese caso determina el nuevo estado del juego y lo devuelve.'''
    return True

def juego_mostrar(juego):
    ''' Función que se encarga de dibujar en pantalla el tablero '''

    #tablero = juego['tablero']
    tablero =  D_NIVELES.get(1)[1::]

    for ir, row in enumerate(tablero):
        for ic, col in enumerate(row):
            img = path_to_img(col)
            print(f'{ic} : {col} -> {img}')
            gamelib.draw_image(img, ic * IMG_PX, ir * IMG_PX)


def main():
    # Inicializar el estado del juego

    # 1 Carga de mapas
    cargar_configuracion_mapas()

    # 2 Carga de niveles


    gamelib.resize(400, 500)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(None)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        # Actualizar el estado del juego, según la `tecla` presionada
        '''
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego,tecla)
            '''

gamelib.init(main)