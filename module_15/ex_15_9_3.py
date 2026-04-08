'''
Consigna:
    Implementar el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad
    de elementos removidos. La lista debe ser recorrida una sola vez.
'''
from IteradorListaEnlazada import IteradorListaEnlazada
from ex_15_9_1 import ListaEnlazada as ListaEnlazadaBase

class ListaEnlazada(ListaEnlazadaBase):
   
    def remover_todos(self, x):
        ''' Funcion que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos'''
        count = 0
        if self.len == 0:
            return count

        #Busco el elemento en la cabecera
        while self.prim is not None and self.prim.dato == x:
            self.prim = self.prim.prox
            count += 1
            self.len -= 1

        if self.prim is None:
            #Si no tiene primero, tampoco tiene último
            self.ult = None
            return count

        n_ant = self.prim
        n_act = self.prim.prox 
        while n_act is not None:
            if n_act.dato == x:    
                # Descartar el nodo
                n_ant.prox = n_act.prox
                self.len -= 1
                count += 1
            else:
                n_ant = n_act
            #Paso al siguiente
            n_act = n_act.prox

        self.ult = n_ant
        return count