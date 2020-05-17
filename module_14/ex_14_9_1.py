'''
Consigna:
    Mejorar la clase Rectangulo, agregando métodos para calcular las dimensiones alto y ancho, y las coordenadas del punto central.
'''
import Punto

class Rectangulo:
    '''
        Representa un rectángulo en el plano.
    '''

    def __init__(self, noroeste, sudeste):
        '''
            Crea un Rectangulo a partir de los Puntos correspondientes a las esquinas superior izquierda e inferior derecha.
        '''
        self.noroeste = noroeste
        self.sudeste = sudeste

    def calcular_ancho(self):
        '''
            Función que devuelve el ancho del rectángulo calculando la diferencia entre puntos.
        '''
        p = Punto(self.sudeste.x, self.noroeste.y)
        return p.distancia(self, self.noroeste)

    def calcular_alto(self):
        '''
            Función que devuelve el alto del rectángulo calculando la diferencia entre puntos.
        '''
        q = Punto(self.noroeste.x, self.sudeste.y)
        return q.distancia(self, self.noroeste)


