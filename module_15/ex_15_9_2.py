'''
Consigna:
    Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y agregue a la lista actual los elementos que se encuentran en la lista recibida.
'''
from IteradorListaEnlazada import IteradorListaEnlazada

class ListaEnlazada:
    '''Modela una lista enlazada.'''
    def __init__(self):
        '''Crea una lista enlazada vacía.'''
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # referencia al último nodo (None si la lista está vacía)
        self.ult = None
        # cantidad de elementos de la lista
        self.len = 0

    def __iter__(self):
        return IteradorListaEnlazada(self)

    def __str__(self):
        ''' Imprime el contenido de la lista enlazada en el mismo formato que las lista e pyhon. ''' 
        l = []
        for dato in self:
            l.append(str(dato))
        return f'[{", ".join(l)}]'
    
    def pop(self, i=None):
        ''' Elimina el nodo de la posición i, y devuelve el dato contenido. Si i está fuera de rango, se levanta la excepción IndexError.
            Si no se recibe la posición, devuelve el último elemento.'''

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(i-1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox      
        self.len -= 1
        return dato

    def remove(self, x):
        ''' Borra la primera aparición del valor x en la lista.Si x no está en la lista, levanta ValueError'''
        
        if self.len == 0:
            raise ValueError('Lista vacía')

        if self.prim.dato == x:
        # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
        # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
                if n_act == None:
                    raise ValueError('El valor no está en la lista.')
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def insert(self, i, x):
        '''Inserta el elemento x en la posición i. Si la posición es inválida, levanta IndexError'''
        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')
        
        nuevo = self._Nodo(x)
        if i == 0:
        # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
        # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        
        if i == self.len:
             self.ult = nuevo
        self.len += 1

    def append(self, x):
        ''' Función que se encarga de insertar x en la última posicion de la lista'''
        self.insert(self.len, x)

    def extend(self, o_lista):
        ''' Función que recibe una ListaEnlazada y agregua a la lista actual los elementos que se encuentran en la lista recibida '''
        n_ant = o_lista.prim
        for pos in range(0, o_lista.len):
            self.append(n_ant.dato)
            n_ant = n_ant.prox

    class _Nodo:
        def __init__(self, dato=None, prox=None):
            self.dato = dato
            self.prox = prox
        
        def __str__(self):
            return str(self.dato)