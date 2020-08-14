'''
Consigna:
    1. Se cuenta con una clase ListaEnlanzada, cuya implementación contiene una referencia al primer nodo y la cantidad de elementos. 
    Implementar el método remover_todos(elemento) que recibe un elemento y remueve de la lista todas las apariciones del mismo. 
    Nota: por razones de eficiencia, no se debe usar pop(), remove() ni cualquier otro método de la lista que saque un elemento. 
    Ejemplo: LE: [1, 2, 3, 4, 3, 6, 3, 8] ,remover_todos(3) -> [1, 2, 4, 6, 8].
'''
from Pila import Pila
from Cola import Cola

def _remover_todos(lista, num):
    while lista.prim.dato == num:
        lista.prim = lista.prim.prox

    n_ant = lista.prim
    n_act = lista.prim.prox

    while n_act != None:
        if n_act.dato == num:
            n_ant.prox = n_act.prox

        n_act = n_act.prox

    return lista

def remover_todos(num):
    ''' función que elimina las repeticiones de num dentro de la lista enlazada pasada por parámetros.'''
    lista = ListaEnalazada()
    _remover_todos(lista, num)

'''
Consigna:
    Escribir una función reemplazar que tome una pila y dos valores, valor_nuevo y valor_viejo, y 
    reemplace en la pila todas las ocurrencias de valor_viejo por valor_nuevo. Al finalizar la ejecución, 
    los elementos de la pila deben quedar en el mismo orden en el que se encontraban originalmente. 
    Ejemplo: PILA: [1, 2, 1, 4, 5, 1, 7, 8], reemplazar(1,3) -> [3, 2, 3, 4, 5, 3, 7, 8].
'''

def reemplazar_recursivo(pila, valor_viejo, valor_nuevo):
    ''' Función que calcula recursivamente cuantos elemetos tiene una pila.'''
    
    if pila.esta_vacia():
        return 

    elemento = pila.desapilar()
    reemplazar_recursivo(pila, valor_viejo, valor_nuevo)
    pila.apilar(elemento if elemento != valor_viejo else valor_nuevo)
    return


def reemplazar(valor_viejo, valor_nuevo):
    pila = Pila()
    return reemplazar_recursivo(pila, valor_viejo, valor_nuevo)

'''
Consigna:
     Escribir una función que, dada una cola y un elemento E, devuelva cuántos elementos faltan para que salga E de la cola. Si E no está en la cola, 
     debe levantarse una excepción. Para cualquiera de los casos posibles, la cola debe quedar en su estado original al finalizar la ejecución. 
     Ejemplo: COLA: [1, 2, 3, 4, 5, 6, 7, 8]
   
    cuantos_faltan(1) -> 0
    cuantos_faltan(8) -> 7
    cuantos_faltan(19) -> Exception
'''

def _cuanto_falta(cola, buscado):
    ''' Función que calcula recursivamente cuantos elemetos faltan para llegar al elemento.'''
    
    if cola.esta_vacia():
        raise Exception('No se encontró el elemento')
    
    elemento = cola.desencolar()
    if elemento == buscado:
        return 1

    contador = 1 + _cuanto_falta(cola, buscado)
    cola.encolar(elemento)
    return contador


def cuanto_falta(cola, elemento):
    return _cuanto_falta(cola, elemento)