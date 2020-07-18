'''
Consigna:
    Escribir una clase TorreDeControl que modele el trabajo de una torre de control de un aeropuerto con una pista de aterrizaje. 
    Los aviones que están esperando para aterrizar tienen prioridad sobre los que están esperando para despegar.
'''
from Cola import Cola

class TorreDeControl():
    def __init__(self):
        self.arribos = Cola()
        self.partidas =  Cola()
    
    def nuevo_arribo(self, avion):
        self.arribos.encolar(avion)
    
    def nueva_partida(self, avion):
        self.partidas.encolar(avion)

    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {self.arribos}')
        print(f'Vuelos esperando para despegar: {self.partidas}')

    def asignar_pista(self):
        ''' Asigna pista a los vuelos que están por arribar y después a los que están para partir.'''
        if not self.arribos.esta_vacia():
            avion = self.arribos.desencolar()
            print(f'El vuelo {avion} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            avion = self.partidas.desencolar()
            print(f'El vuelo {avion} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')

