'''
Consigna:
    a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos instantes de tiempo (números enteros expresados en segundos), 
    con la condición desde < hasta.
    b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
    c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección es nula.
    d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo intervalo resultante de la unión entre ambos.
'''

class Intervalo:
    """Representa un intervalo: sus atributos son: desde y hasta."""

    def validar_numero_positivo(self, valor):
        ''' Si el valor es numérico y positivo, lo devuelve. En caso contrario lanza TypeError. '''
        if not isinstance(valor, (int, float, complex)) or valor < 0:
            raise TypeError("{:r} no es un valor numérico".format(valor))
        return valor

    def valida_intervalo(self):
        ''' Valida si desde < hasta '''
        if not self.desde < self.hasta:
            raise TypeError(f"{self.desde} no es menor que {self.hasta}")
    
    def __init__(self, desde, hasta):
        """Crea un Intervalo. Desde y Hasta deben ser números positivos y Desde < Hasta."""
        self.desde = self.validar_numero_positivo(desde)
        self.hasta = self.validar_numero_positivo(hasta)
        self.valida_intervalo()

    def duracion(self):
        ''' Devuelve la duración en segundos del intervalo. '''
        return self.hasta - self.desde

    def hay_interseccion(self, otro):
        ''' Devuelve true o false si hay o no intersección '''
        return self.desde in range(otro.desde, otro.hasta + 1) or self.hasta in range(otro.desde, otro.hasta + 1)
    
    def son_adyacentes(self, otro):
        ''' Deveulve true o false si los intervalos son o no adyacentes '''
        return self.desde == otro.hasta + 1 or self.hasta == otro.desde -1

    def interseccion(self, otro):
        ''' 
            Recibe otro intervalo y devuelve un nuevo intervalo resultante de la intersección entre ambos, 
            o una excepción si la intersección es nula.
        '''
        if not self.hay_interseccion(otro):
            raise AssertionError(f'El rango {otro.desde} - {otro.hasta} no tiene intersección.')
        
        return [x for x in range(max(self.desde, otro.desde), min(self.hasta, otro.hasta) + 1)]

    def union(self, otro):
        '''
            Si los intervalos no son adyacentes ni intersectan, debe lanzar una excepción. 
            En caso contrario devuelve un nuevo intervalo resultante de la unión entre ambos.
        '''
        if  not self.hay_interseccion(otro):
             raise AssertionError(f'No hay intersección ni tampoco son adyacentes los intervalos.')

        return [x for x in range(min(otro.desde, self.desde), max(otro.hasta, self.hasta) + 1)]