'''
Consigna:
    a) Crear una clase Carta que contenga un palo y un valor.
    b) Crear una clase Solitario que permita apilar las cartas una arriba de otra, pero sólo
    permita apilar una carta si es de un número inmediatamente inferior y de distinto palo
    a la carta que está en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una
    excepción.
'''


class Solitario:

    def __init__(self):
        ''' Costructor de la clase, que crea una pila vacía de la clase Carta. '''
        self.cartas = []

    def apilar_carta(self, carta):
        ''' Función que recibe un carta y la apila solo si está es menor y de distinto palo, sino genera un error. '''
        ultima_carta = self.cartas.pop()
        
        if carta.valor + 1 == ultima_carta.valor and  ultima_carta.palo is not carta.palo:
            self.cartas.append(carta)
        else:
            raise Exception('La carta no se puede agregar a la pila.')

class Carta:
    ''' Representación de una carta.'''

    def __init__(self, valor, palo):
        ''' Constructor de la clase que recibe un valor y un palo.'''
        self.valor = valor
        self.palo = palo