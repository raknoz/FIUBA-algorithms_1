from IteradorListaEnlazada import IteradorListaEnlazada

class Cola:
    def __init__(self):
        '''Crea una cola vacía.'''
        self.primero = None
        self.ultimo = None
        self.elementos = 0
    
    def __iter__(self):
        return IteradorListaEnlazada(self)

    def __str__(self):
        ''' Imprime el contenido de la lista enlazada en el mismo formato que las lista e pyhon. ''' 
        l = []
        for dato in self:
            l.append(str(dato))
        return f'[{", ".join(l)}]'

    def encolar(self, x):
        '''Encola el elemento x.'''
        nuevo = Nodo(x)
        if self.ultimo is not None:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo
        self.elementos += 1

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor. Si la cola está vacía, levanta ValueError.'''
        if self.primero is None:
            raise ValueError('La cola está vacía')
        valor = self.primero.dato
        self.primero = self.primero.prox
        if not self.primero:
            self.ultimo = None
        self.elementos -= 1
        return valor

    def esta_vacia(self):
        '''Devuelve True si la cola esta vacía, False si no.'''
        return self.primero is None

    #  Se agrega la funcion para evitar tener que recorrerla para saber cuantos elementos tiene. 
    def __len__(self):
        ''' Retorna la longitud de la cola. '''
        return self.elementos


class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return str(self.dato)