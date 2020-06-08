'''
Consigna:
    Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y agregue a la lista actual los elementos que se encuentran en la lista recibida.
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_1 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
   
    def extend(self, o_lista):
        ''' Función que recibe una ListaEnlazada y agregua a la lista actual los elementos que se encuentran en la lista recibida '''
        n_ant = o_lista.prim
        for pos in range(0, o_lista.len):
            self.append(n_ant.dato)
            n_ant = n_ant.prox