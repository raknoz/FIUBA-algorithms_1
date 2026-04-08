'''
Consigna:
    Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un elemento y duplica todas las apariciones del mismo.
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_1 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
    
    def duplicar(self, e):
        ''' Función que recibe un elemento e y duplica todos las ocurrencia es la lista. '''
        n_act = self.prim
        pos = 0
        while pos  < self.len:
            if n_act.dato == e:
                self.insert(pos, e)
                pos+=1
            pos+=1
            n_act = n_act.prox