from tkinter import *
from Partida import Partida
import gamelib
import soko
import os

#Diccionarios de información
D_MOVIMIENTOS = {}
D_NIVELES = {}
D_COORDENADAS = {'NORTE':(0, -1), 'SUR':(0, 1), 'ESTE':(1, 0), 'OESTE':(-1, 0)}
L_OPCIONES = ['SALIR', 'REINICIAR', 'CARGAR', 'GUARDAR', 'DESHACER', 'PISTAS']
D_OPCIONES = {}
NIVEL_INICIAL = 1

#Tamaño de la imagen
IMG_PX = 40

def es_titulo(cadena):
    ''' Función que valida si una cadena determinada contiene caracteres alfanuméricos'''
    for chr in cadena:
        if chr.isalnum():
            return True
    return False

def path_to_img(argument):
    switcher = { 
        '#': 'img_40/wall.png', 
        '*': 'img_40/box_goal.png', 
        '@': 'img_40/ground_player.png', 
        ' ': 'img_40/ground.png',
        '$': 'img_40/box.png',
        '.': 'img_40/ground_goal.png',
        '+': 'img_40/player_goal.png',
    }
    return switcher.get(argument, 'img_40/wall.png')

def guardar_partida(n_file, nivel_actual=0):
    ''' Función que se encarga de guarda el último nivel ganado. '''
    with open(n_file, 'w') as f:
        f.write(str(nivel_actual - 1))

def cargar_partida(n_file):
    '''Función que lee un archivo y carga el último nivel guardado.'''
    nivel = 0
    if os.path.exists(n_file):
        with open(n_file, 'r') as f:
            for linea in f:
                linea = linea.rstrip('\n').rstrip()
            nivel = int(linea) if linea.isdigit() else nivel
    return siguiente_nivel(nivel, len(D_NIVELES))

def cargar_configuracion_teclas(n_file):
    ''' Función que se encarga de cargar la configuración de las teclas '''
    #Lectura del archivo de teclas y armado del diccionario
    ''' Función que lee un archivo con la configuración  de teclas y devuelve un mapa con los datos obtenidos. '''
    with open(n_file, "r") as f:
        lines = (line.rstrip() for line in f) 
        lines = list(line.replace(' ', '') for line in lines if line) # Non-blank lines in a list
        l_keys = D_COORDENADAS.keys()
        for line in lines:
            key, mov = line.split('=')
            if mov in l_keys:
                D_MOVIMIENTOS[key] = D_COORDENADAS.get(mov)
            elif mov in L_OPCIONES:
                D_OPCIONES[key] = mov

def cargar_configuracion_niveles(n_file):
    ''' Función que se encarga de cargar la configuración de los niveles '''
    with open(n_file, 'r') as f:
        l_nivel = []
        nivel = 1
        titulo_nivel = []
        for linea in f:
            linea = linea.rstrip('\n').rstrip() #Limpio la línea de espacios y del caracter final de salto de línea
            if linea:
                if es_titulo(linea): #Es parte del título
                    titulo_nivel.append(linea)
                else: #Es parte del nivel
                    l_nivel.append(linea)
            elif len(l_nivel) > 0:
                l_nivel.insert(0, ' - '.join(titulo_nivel))
                D_NIVELES[nivel] = l_nivel
                titulo_nivel = []
                l_nivel = []
                nivel+=1
        if len(l_nivel) > 0:
            l_nivel.insert(0, ' - '.join(titulo_nivel))
            D_NIVELES[nivel] = l_nivel
   
def juego_actualizar(partida, tecla):
    ''' Actualizar el estado del juego tecla es el botón que se presionó. 
        obtiene el movimiento hacia donde moverse y determina el nuevo estado del juego y lo devuelve.'''
    #Guardo el estado anterior para luego comparar con el movimiento.
    tablero_tmp = partida.obtener_tablero()
    partida.actualizar_tablero(soko.mover(partida.obtener_tablero(), D_MOVIMIENTOS.get(tecla)))

    #Si el tablero sufrió cambios, lo guardo
    if tablero_tmp != partida.obtener_tablero():
        partida.agregar_movimiento(tablero_tmp)

    if soko.juego_ganado(partida.obtener_tablero()):
        juego_mostrar(partida.obtener_tablero())
        return siguiente_nivel(partida.nivel_actual, partida.total_niveles)
    return partida

def juego_mostrar(tablero):
    ''' Función que se encarga de dibujar en pantalla el tablero '''
    for ir, row in enumerate(tablero):
        for ic, col in enumerate(row):
            img = path_to_img(col)
            gamelib.draw_image(img, ic * IMG_PX, ir * IMG_PX)

def siguiente_nivel(nivel_actual, total_niveles):
    '''Función que se encarga de cargar el siguiente nivel'''
    prox_nivel = nivel_actual + 1
    if nivel_actual == total_niveles:
        gamelib.say("Finalizó el juego!!!")
        prox_nivel = NIVEL_INICIAL 
    return Partida(soko.crear_grilla(D_NIVELES.get(prox_nivel)), prox_nivel, len(D_NIVELES))

def main():
    #1 Carga los niveles
    cargar_configuracion_niveles('niveles.txt')

    #2 Carga de teclas
    cargar_configuracion_teclas('teclas.txt')
    
    #3 Inicio de partida nivel 1
    partida = Partida(soko.crear_grilla(D_NIVELES.get(NIVEL_INICIAL)), NIVEL_INICIAL, len(D_NIVELES))
    
    while gamelib.is_alive():
        gamelib.resize(partida.max_columnas * IMG_PX, partida.max_filas * IMG_PX)
        gamelib.title(partida.titulo)
        gamelib.draw_begin()
        # Dibujar la pantalla 
        juego_mostrar(partida.obtener_tablero())
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
            # El usuario presionó la tecla r, reinicia la aplicación.
            partida.reiniciar_partida()            
        
        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'CARGAR':
            # El usuario presionó la tecla l, carga el último nivel completo.
            partida = cargar_partida('sokoban_save.txt')

        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'GUARDAR':
            # El usuario presionó la tecla g, guarda el último nivel completo.
            guardar_partida('sokoban_save.txt', partida.nivel_actual)

        if ev.type == gamelib.EventType.KeyPress and D_OPCIONES.get(ev.key) == 'DESHACER':
            # El usuario presionó la tecla q, carga el último movimiento.
            partida.tablero = partida.obtener_ultimo_movimiento()

        if tecla in D_MOVIMIENTOS.keys():
            partida = juego_actualizar(partida, tecla)


gamelib.init(main)