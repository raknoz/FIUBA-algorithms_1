'''
Consigna:
    Escribir un método de la clase ListaEnlazada que invierta el orden de la lista (es decir, el primer elemento queda como último y viceversa).
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_1 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
   
    def invertir(self):
        ''' Función que invierte la lista actual '''

        n_act = self.prim
        for p in range(self.len):
            ''' '''
