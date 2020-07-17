'''
    Consigna:
        la parada del colectivo 130 pueden ocurrir dos eventos diferentes:
            • Llega una persona
            • Llega un colectivo con n asientos libres, y se suben al mismo todas las personas que están
        esperando, en orden de llegada, hasta que no quedan asientos libres.
        Cada evento se representa con una tupla que incluye:
            • El instante de tiempo (cantidad de segundos desde el inicio del día)
            • El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
            • En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos libres.
        Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuelva el promedio de tiempo de espera 
        de los pasajeros en la parada.
        ---> (43,'p'), (80,'c',1) <---
'''
from cola import Cola

def promedio_espera(eventos):
    ''' Función que recibe una lista de eventos ordenada cronológicamente y y devuelva el promedio de tiempo de espera de los pasajeros. '''
    tiempos = []
    pasajeros = Cola()

    for evento in eventos:
        if evento[1] == 'c':
            cont = 0
            while not pasajeros.esta_vacia() and cont < evento[2]:
                tiempos.append(evento[0] - pasajeros.desencolar())
                cont +=1
        else:
            pasajeros.encolar(evento[0])

    return sum(tiempos) / len(tiempos)            