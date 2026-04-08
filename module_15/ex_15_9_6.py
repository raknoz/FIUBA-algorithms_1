'''
Consigna:
    Escribir un método de la clase ListaEnlazada que invierta el orden de la lista (es decir, el primer elemento queda como último y viceversa).
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_3 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
   
    def invertir(self):
        ''' Función que invierte la lista actual '''
        nodos = []
        n_act = self.prim
        while n_act is not None:
            nodos.append(n_act.dato)
            n_act = n_act.prox      

        for dato in nodos:
            self.remover_todos(dato)

        #Inserto los datos invertidos
        for dato in nodos[::-1]:
            self.insert(self.len, dato)