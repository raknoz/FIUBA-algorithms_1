class Punto:
    '''
        Representación de un punto en el plano en coordenadas cartesianas (x, y)
    '''

    def validar_numero(self, valor):
        '''
            Si el valor es numérico, lo devuelve. En caso contrario lanza TypeError.
        '''
        if not isinstance(valor, (int, float, complex)):
            raise TypeError("{:r} no es un valor numérico".format(valor))
        return valor

    def __init__(self, x, y):
        '''
            Constructor de Punto. x e y deben ser numéricos, de no ser así, se levanta una excepción TypeError
        '''
        self.x = validar_numero(self, x)
        self.y = validar_numero(self, y)

    def distancia(self, otro):
        '''
            Devuelve la distancia entre ambos puntos.
        '''
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx * dx + dy * dy) ** 0.5

    def restar(self, otro):
        '''
            Devuelve el Punto que resulta de la resta entre dos puntos.
        '''
        return Punto(self.x - otro.x, self.y - otro.y)
    
    def norma(self):
        '''
            Devuelve la norma del vector que va desde el origen hasta el punto.
        '''
        return (self.x * self.x + self.y * self.y) ** 0.5
    
    def __str__(self):
        '''
            Devuelve la representación del Punto como cadena de texto.
        '''
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        '''
            Devuelve la representación formal del Punto como cadena de texto.
        '''
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, otro):
        '''
            Devuelve la suma de ambos puntos.
        '''
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        '''
            Devuelve la resta de ambos puntos.
        '''
        return Punto(self.x - otro.x, self.y - otro.y)