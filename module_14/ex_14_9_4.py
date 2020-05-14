'''
Consigna:
    a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se asignan en el constructor, y se imprimen como X/Y en el método __str__.
    b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción con la suma de ambas.
    c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción con el producto de ambas.
    d) Crear un método simplificar que modifica la fracción actual de forma que los valores del dividendo y divisor sean los menores posibles.
'''

class Fraccion:
    """Representa una Fracción: sus atributos son: dividendo y Divisor."""

    def obtener_mcd(self, m, n):
        ''' Función que devuelve el máximo común divisor entre m y n'''
        r = m % n
        while r != 0:
            m, n = n, r
            r = m % n
        return n

    def valida_numero(self, n, m):
        ''' Función que valida un número n y que sea mayor al minimo m'''
        if not isinstance(n, (int, float, complex)) or n < m:
            raise TypeError(f'{n} no es un valor numérico o es menos a {m}')
        return n

    def obterner_divisor(self, otro):
        '''Función que devuelve el mismo divisor si ambos son iguales o la multiplacación de ambos si son diferenctes.'''
        return self.divisor if self.divisor == otro.divisor else self.divisor * otro.divisor
    
    def obtener_dividendo(self, otro):
        '''Función que devuelve el dividendo de dos fracciones'''
        if otro.divisor == self.divisor:
            return self.dividendo + otro.dividendo
        return otro.dividendo * self.divisor + otro.divisor * self.dividendo

    def __init__(self, dividendo, divisor):
        '''Crea una Fracción. dividendo > 0 y divisor > 1.'''
        self.dividendo = self.valida_numero(dividendo, 1)
        self.divisor = self.valida_numero(divisor, 2)
    
    def __str__(self):
        '''Función que devuelve la fracción'''
        return f'{self.dividendo}/{self.divisor}'
    
    def __add__(self, otra):
        '''Función que recibe otra fracción y devuelve una nueva fracción con la suma de ambas.'''
        _divisor = self.obterner_divisor(otra)
        _dividendo = self.obtener_dividendo(otra)
        return Fraccion(_dividendo, _divisor)
    
    def __mul__(self, otra):
        ''' Función que recibe otra fracción y devuelve una nueva fracción con el producto de ambas.'''
        return Fraccion(self.dividendo * otra.dividendo, self.divisor * otra.divisor)

    def simplificar(self):
        '''
            Función que modifica la fracción actual de forma que los valores del dividendo y divisor sean los menores posibles.
        '''
        mcd = self.obtener_mcd(self.dividendo, self.divisor)
        while mcd != 1:
            self.dividendo = self.dividendo // mcd
            self.divisor = self.divisor // mcd
            mcd = self.obtener_mcd(self.dividendo, self.divisor)      