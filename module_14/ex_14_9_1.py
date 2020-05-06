'''
Consigna:
    Mejorar la clase Rectangulo, agregando métodos para calcular las dimensiones alto y ancho, y las coordenadas del punto central.
'''

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

    def desplazar(self, dx, dy):
        '''
            Desplaza el punto según dx y dy.
        '''
        self.x += dx
        self.y += dy
