'''
Consigna:
    Una lista circular es una lista cuyo último nodo está ligado al primero, de modo que es posible 
    recorrerla infinitamente. Escribir la clase ListaCircular, incluyendo los métodos insert, append, remove y pop.
'''
from IteradorListaEnlazada import IteradorListaEnlazada

class ListaCircular():
    '''Clase que representa la lista circular. '''

    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # referencia al último nodo
        self.ult = None
        # cantidad de elementos de la lista
        self.len = 0

    def __iter__(self):
        return None

    def append(self, x):
        ''' Función que inserta la final de la lista el elemento x. '''
        self.insert(self.len, x)
    
    def pop(self, i=None):
        ''' Elimina el nodo de la posición i, y devuelve el dato contenido. Si i está fuera de rango, se levanta la excepción IndexError.
            Si no se recibe la posición, devuelve el último elemento.'''

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')

        dato = None

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
            self.ult.prox = self.prim
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
            self.ult = n_ant
        self.len -= 1
        return dato

    def remove(self, x):
        ''' Borra la primera aparición del valor x en la lista.Si x no está en la lista, levanta ValueError'''
        
        if self.len == 0:
            raise ValueError("Lista vacía")

        if self.prim.dato == x:
        # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
            self.ult.prox = self.prim
        else:
        # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            idx = 1
            while idx < self.len:
                if n_act.dato == x:
                    break
                n_ant = n_act
                n_act = n_ant.prox
                idx += 1
                if idx == self.len:
                    raise ValueError("El valor no está en la lista.")
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def insert(self, i, x):
        '''Inserta el elemento x en la posición i. Si la posición es inválida, levanta IndexError'''

        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        
        nuevo = _Nodo(x)
        if i == 0:
        # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
            if self.len == 0:
                self.ult = nuevo
            self.ult.prox = nuevo
        # Caso particular para el último 
        elif i == self.len:
            nuevo.prox = self.prim
            n_ant = self.ult
            n_ant.prox = nuevo
            self.ult = nuevo
        else:
        # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
                # Intercalar el nuevo nodo
                nuevo.prox = n_ant.prox
                n_ant.prox = nuevo
        self.len += 1

    def imprimir(self):
        ''' Función que se encarga de imprimir el contenido de la lista. '''
        n_act = self.prim

        if self.len == 0:
            print('No hay elementos')
        else:
            for e in range(0, self.len):
                print(f'{n_act.dato} -> {n_act.prox.dato}')
                n_act = n_act.prox

class _Nodo():
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return str(self.dato)