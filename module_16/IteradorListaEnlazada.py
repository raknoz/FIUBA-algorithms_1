class IteradorListaEnlazada:
    '''Almacena el estado de una iteración sobre la ListaEnlazada.'''

    def __init__(self, lista):
        '''Crea un iterador para la lista dada'''
        self.lista = lista
        self.anterior = None
        self.actual = lista.primero

    def avanzar(self):
        ''' Avanza la iteración un paso hacia adelante. 
        Pre: la iteración no debe haber llegado al final. '''
        self.anterior = self.actual
        self.actual = self.actual.prox
    
    def dato_actual(self):
        ''' Devuelve el elemento en la posición actual de iteración.
        Pre: la iteración no debe haber llegado al final.'''
        return self.actual.dato

    def esta_al_final(self):
        ''' Devuelve verdadero si la iteración llegó al final de la lista.'''
        return self.actual is None

    def insertar(self, x):
        ''' Insertar un elemento en el lugar de la iteración actual.
            Una vez insertado, el nuevo elemento será el actual de la iteración,
            y el elemento que antes era el actual será el siguiente. '''
        nuevo = self._Nodo(x)
        if self.anterior:
            nuevo.prox = self.anterior.prox
            self.anterior.prox = nuevo
        else:
            nuevo.prox = self.lista.primero
            self.lista.primero = nuevo
        
        self.actual = nuevo

    def eliminar(self):
        dato = self.dato_actual()
        if self.anterior:
            self.anterior.prox = self.actual.prox
            self.actual = self.anterior.prox
        else:
            self.lista.primero = self.actual.prox
            self.actual = self.lista.primero
        
        return dato
    
    def __next__(self):
        if self.esta_al_final():
            raise StopIteration("No hay más elementos en la lista")
        dato = self.dato_actual()
        self.avanzar()
        return dato
    
    class _Nodo:
        def __init__(self, dato=None, prox=None):
            self.dato = dato
            self.prox = prox
        
        def __str__(self):
            return str(self.dato)