'''
    Consigna:
    Escribir las clases Impresora y Oficina que permita modelar el funcionamiento de un conjunto de impresoras conectadas en red.

'''
from Cola import Cola

class Oficina:

    def __init__(self):
        ''' Constructor de la clase Oficina. '''
        self.impresoras = {}
    
    def agregar_impresora(self, _impresora):
        ''' Función que recibe una impresora y la agrega a la lista. '''
        self.impresoras[_impresora.nombre] = _impresora

    def quitar_impresora(self, n_impresora):
        ''' Función que recibe el nombre de un impresora y la quita a la lista. '''
        self.impresoras.pop(n_impresora)

    def impresora(self, n_impresora):
        ''' Función que devuelve una impresora de la lista. '''
        if n_impresora not in self.impresoras.keys():
            raise Exception('No existe la impresora buscada!')
        return self.impresoras.get(n_impresora)

    def obtener_impresora_libre(self):
        ''' Función que devuelve una impresora libre, o con menos impresiones encoladas.'''
        for nro, impresora in enumerate(self.impresoras.values()):
            if nro == 0:
                tmp = impresora
            elif impresora.trabajos_en_espera() < tmp.trabajos_en_espera():
                tmp = impresora
        return tmp

class Impresora:

    def __init__(self, nombre, nivel_tinta):
        ''' Constructor de la impresora, recibe el nombre y la capacidad de tinta máxima.'''
        self.nombre = nombre
        self.nivel_tinta = nivel_tinta
        self.tinta_actual = nivel_tinta
        self.trabajos = Cola()
        self.cantidad_trabajos = 0

    def encolar(self, documento):
        ''' Función que encola un documento en la impresora, NO LO IMPRIME '''
        self.trabajos.encolar(documento)
        self.cantidad_trabajos +=1
    
    def imprimir(self):
        ''' Función que imprime el primer trabajo encolado.
        Si está vacía la cola de impresión muestra un mensaje. '''

        if self.trabajos.esta_vacia():
            print('No hay documentos para imprimir!')
            return
        if self.tinta_actual == 0:
            print('No tengo tinta :(')
            return
        self.tinta_actual -= 1
        self.cantidad_trabajos -=1
        print(self.trabajos.desencolar())
    
    def cargar_tinta(self):
        ''' Función que recarga la tinta de la impresora. '''
        self.tinta_actual = self.nivel_tinta

    def trabajos_en_espera(self):
        ''' Función que devuelve la cantidad de trabajos en lista de espera. '''
        return self.cantidad_trabajos

    def __str__(self):
        return f'Impresora: {self.nombre} | cantidad de trabajos en espera: {self.trabajos_en_espera()} | tinta disponible: {self.nivel_tinta}'