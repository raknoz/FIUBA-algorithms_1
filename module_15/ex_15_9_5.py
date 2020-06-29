'''
Consigna:
    Implementar el método filter(f) de ListaEnlazada, que recibe una función
    y devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f devuelve True. 
    La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se puede llamar a append).
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_1 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
       
    def filter(self, f):
        ''' Función que recibe un filtro f y devuelve una nueva lista con todos los elementos que coinciden con ese filtro. '''
        l_aux = ListaEnlazada()
        n_act = self.prim
        for pos in range(0, self.len):
            if f(n_act.dato):
                nuevo = _Nodo(n_act.dato)
                l_aux.append(nuevo)
            n_act = n_act.prox
        return l_aux

class _Nodo():
    def __init__(self, dato=None, prox=None, ant=None):
        self.dato = dato
        self.prox = prox
        self.ant = ant
    
    def __str__(self):
        return str(self.dato)