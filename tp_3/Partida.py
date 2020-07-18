from Pila import Pila

class Partida():
    '''Objeto que contiene toda la información de la partida actual.'''
    def obtener_tablero_titulo(self, nivel):
        ''' Función que se encarga de obtener el tablero y el título. '''
        return nivel[1::], ' '.join(nivel[0])

    def copiar_tablero(self):
        ''' Función que copia todo el contido de una grilla. '''
        return [row[:] for row in self.tablero]

    def obtener_max_filas(self):
        ''' Obtengo la fila con más elementos del tablero. '''
        return len(self.tablero)

    def obtener_max_columnas(self):
        ''' Función que devuelve la cantidad de columnas del tablero.'''
        return len(max(self.tablero, key=len))

    def agregar_movimiento(self, tablero):
        ''' Función que agrega el movimiento realizado. '''
        if self.movimientos.esta_vacia():
            self.movimientos.apilar(self.original)
        self.movimientos.apilar(tablero)

    def obtener_ultimo_movimiento(self):
        ''' Función que devuelve el último movimiento realizado. Si no hay movimientos retorna el tablero original. '''
        if self.movimientos.esta_vacia():
            return self.tablero
        return self.movimientos.desapilar()

    def reiniciar_partida(self):
        ''' Función que reinicia los valores del nivel.'''
        self.tablero = self.original
        self.movimientos = Pila()

    def actualizar_tablero(self, _tablero):
        ''' Función que actualiza el moviento en el tablero. '''
        self.tablero = _tablero
    
    def obtener_tablero(self):
        ''' Función que devuelve el tablero de la partida. '''
        return self.tablero

    def __init__(self, esquema, nivel, total_niveles):
        self.tablero, self.titulo = self.obtener_tablero_titulo(esquema)
        self.nivel_actual = nivel
        self.original = self.copiar_tablero()
        self.max_filas = self.obtener_max_filas()
        self.max_columnas = self.obtener_max_columnas()
        self.total_niveles = total_niveles
        self.movimientos = Pila()
        