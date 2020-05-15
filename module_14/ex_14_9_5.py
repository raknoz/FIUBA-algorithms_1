'''
Consigna:
    a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán sus coordenadas. 
    En el método __str__ se imprime su contenido con el formato [x,y,z]
    b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma cantidad de elementos 
    y devuelva un nuevo vector con la suma de ambos. Si no tienen la misma cantidad de elementos debe levantar una excepción.
    c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con los elementos multiplicados por ese número.
'''

class Vector:
    '''Representa una Fracción: su atributo es: Una lista.'''

    def __init__(self, arr):
        '''Constructor del vector, recibe una lista cómo parámetro'''
        self.elementos = arr

    def __str__(self):
        '''Función que imprime el contenido del vector'''
        return f'{self.elementos}'
    
    def __add__(self, otro):
        '''Suma dos vectores del mismo tamaño, sino da error'''
        if len(otro.elementos) != len(self.elementos):
            raise ValueError('Ingreso un vector de diferente tamaño.')

        return [e + self.elementos[i] for i, e in enumerate(otro.elementos)]
    
    def __mul__(self, valor):
        '''Retorna un nuevo vector con todos sus elementos multiplicados por valor'''
        return [x * valor for x in self.elementos]

        


    
