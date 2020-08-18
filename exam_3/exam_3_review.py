from Cola import Cola
from Pila import Pila

'''
1) Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva. 
Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0.
La implementación de LE contiene una referencia al primer nodo y un atributo con la longitud.
    Ejemplos: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (len = 8)
    le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
    le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
    le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
    le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]
'''



'''
2) Se quiere escribir una función que sea capaz de sumar dos números que se encuentran representados como pilas de sus dígitos. Los números a sumar pueden tener cualquier cantidad de dígitos, y a su vez, no tener la misma cantidad de dígitos uno que el otro. La función debe devolver una pila con los dígitos del resultado.
Por ejemplo, para realizar la suma 641 + 789 se tendrían las siguientes pilas:
p1 = | 6 | (tope) y p2 = | 7 | (tope). La función debería devolver la siguiente pila | 1 | (tope), que representa al número 1430.
     | 4 |               | 8 |                                                       | 4 |
     | 1 |               | 9 |                                                       | 3 |
     |---|               |---|                                                       | 0 |
                                                                                     |---|
'''

def invertir_pila(pila):
    ''' Función que recibe una pila y la invierte. '''
    aux = Pila()
    while not pila.esta_vacia():
        aux.apilar(pila.desapilar())
    return aux


def sumar_pilas(pila1, pila2):
    ''' Dadas dos pilas suma todos los elementos y devuelve una nueva. '''
    pila_result = Pila()
    pila1 = invertir_pila(pila1)
    pila2 = invertir_pila(pila2)
    resto = 0

    while not pila1.esta_vacia() and not pila2.esta_vacia():
        resultado = pila1.desapilar() + pila2.desapilar() + resto
        pila_result.apilar(resultado % 10)
        resto = (resultado // 10) if resultado >= 10 else 0

    #Se valida si alguna de las pilas tiene elementos.
    while not pila1.esta_vacia():
        resultado = pila1.desapilar() + resto
        pila_result.apilar(resultado % 10)
        resto = (resultado // 10) if resultado >= 10 else 0

    while not pila2.esta_vacia():
        resultado = pila2.desapilar() + resto
        pila_result.apilar(resultado % 10)
        resto = (resultado // 10) if resultado >= 10 else 0

    #Si queda resto lo apilo
    if resto != 0:
        pila_result.apilar(resto)

    return invertir_pila(pila_result)


'''
3) Se encontraron incongruencias en los planes preventivos de la pandemia de COBID20. 
El plan del país lleva una serie de fases a cumplir las cuales estan insertadas en una cola de menor a mayor. 
De alguna manera hay fases intercaladas que no estaban en el plan y se nos exige removerlas. 
Se pide entonces escribir una funcion que dada dicha cola de fases, la modifique de forma que sólo quede una serie de fases ordenadas.
Ejemplo:

Para la cola:
sale <| 1 2 6 3 5 4 5 6 7 |< entra
debería quedar la cola:
sale <| 1 2 6 7 |< entra

Para la cola:
sale <| 1 5 4 3 2 8 |< entra
debería quedar la cola:
sale <| 1 5 8 |< entra
'''

def depurar_fases(c_fases):
    ant = None
    n_fases = len(c_fases)
    posicion = 0
    while posicion < n_fases:
        fase = c_fases.desencolar()
        #Separación del primer caso
        if ant == None or fase > ant:
            c_fases.encolar(fase)
            ant = fase
        posicion += 1
    return c_fases
