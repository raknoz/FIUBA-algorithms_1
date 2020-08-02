'''
Consigna: 
    Escribir una función recursiva que simule el siguiente experimento: Se tiene una rata en una jaula con 3 caminos, 
    entre los cuales elige al azar (cada uno tiene la misma probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, 
    si elige el 2 luego de 5 minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. La rata no aprende,
    siempre elige entre los 3 caminos con la misma probabilidad, pero quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
    La función debe devolver el tiempo que tarda la rata en salir de la jaula.
'''
import random

DICT_DELAY = {1:3, 2:5, 3:7}

def escape(jaula):
    ''' Función que calcula el tiempo de salir de una rata.'''
    if jaula == 3:
        return 7
    else:
        return DICT_DELAY.get(jaula) + escape(random.randint(1,3))
