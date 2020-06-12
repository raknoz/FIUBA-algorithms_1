from tkinter import *
import gamelib
import soko
import pprint

#Diccionarios de información
D_MOVIMIENTOS = {}
D_NIVELES = {}
D_DIRECCIONES = {'NORTE':(0, -1), 'SUR':(0, 1), 'ESTE':(1, 0), 'OESTE':(-1, 0)}
D_OPCIONES = {}
LIMITE_NIVELES = 2
NIVEL_INICIAL = 1

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
    return switcher.get(argument, 'img_v2/ground.gif')

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

    D_NIVELES[2] = [ 
        'Level 154',
        '############################',
        '#                          #',
        '# ######################## #',
        '# #                      # #',
        '# # #################### # #',
        '# # #                  # # #',
        '# # # ################ # # #',
        '# # # #              # # # #',
        '# # # # ############ # # # #',
        '# # # # #            # # # #',
        '# # # # # ############ # # #',
        '# # # # #              # # #',
        '# # # # ################ # #',
        '# # # #                  # #',
        '##$# # #################### #',
        '#. @ #                      #',
        '#############################']

def juego_actualizar(partida, tecla):
    ''' Actualizar el estado del juego x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda del tablero; 
    en ese caso determina el nuevo estado del juego y lo devuelve.'''
    
    t_coordenadas = D_DIRECCIONES.get(D_MOVIMIENTOS.get(tecla))
    partida.tablero = soko.mover(partida.tablero, t_coordenadas)
    if soko.juego_ganado(partida.tablero):
        return siguiente_nivel(partida.nivel)
    return partida

def juego_mostrar(tablero):
    ''' Función que se encarga de dibujar en pantalla el tablero '''
    for ir, row in enumerate(tablero):
        for ic, col in enumerate(row):
            img = path_to_img(col)
            gamelib.draw_image(img, ic * IMG_PX, ir * IMG_PX)

def siguiente_nivel(nivel_actual):
    '''Función que se encarga de cargar el siguiente nivel'''
    prox_nivel = nivel_actual + 1
    if nivel_actual == LIMITE_NIVELES:
        gamelib.say("Finalizó el juego!!!")
        prox_nivel = NIVEL_INICIAL 
    return _Partida(soko.crear_grilla(D_NIVELES.get(prox_nivel)))

def main():
    #1 Carga los niveles
    cargar_configuracion_niveles()

    #2 Carga de teclas
    cargar_configuracion_teclas()
    
    #3 Inicio de partida nivel 1
    partida = _Partida(soko.crear_grilla(D_NIVELES.get(NIVEL_INICIAL)))
    
    while gamelib.is_alive():
        gamelib.resize(partida.max_columnas * IMG_PX, partida.max_filas * IMG_PX)
        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(partida.tablero)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        # Actualizar el estado del juego, según la `tecla` presionada

        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'SALIR':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'REINICIAR':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            partida.tablero = partida.original

        if tecla in D_MOVIMIENTOS.keys():
            partida = juego_actualizar(partida, tecla)
    

class _Partida():
    '''Objeto que contiene toda la información de la partida actual.'''
    LETRAS_AZ = ['abcdefghijklmnopqrstuvwxyz']

    def obtener_tablero_titulo(self, nivel):
        ''' Función que se encarga de obtener el tablero y el título. '''
        return nivel[1::], nivel[:1]

    def copiar_tablero(self):
        ''' Función que copia todo el contido de una grilla. '''
        return [row[:] for row in self.tablero]

    def obtener_max_filas(self):
        ''' Obtengo la fila con más elementos del tablero. '''
        return len(self.tablero)

    def obtener_max_columnas(self):
        ''' Función que devuelve la cantidad de columnas del tablero.'''
        return len(max(self.tablero, key=len))

    def actualizar_tablero(self, n_tablero):
        self.tablero = n_tablero

    def __init__(self, nivel):
        self.tablero, self.titulo = self.obtener_tablero_titulo(nivel)
        self.nivel = 1
        self.original = self.copiar_tablero()
        self.max_filas = self.obtener_max_filas()
        self.max_columnas = self.obtener_max_columnas()
        self.juego_ganado = False

gamelib.init(main)