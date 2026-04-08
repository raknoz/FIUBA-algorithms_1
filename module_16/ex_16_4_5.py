'''
Consigna:
    Crear una clase PilaConMaximo que soporte las operaciones de Pila( apilar(elemento) y desapilar() ), 
    y además incluya el método obtener_maximo() en tiempo constante. 
    Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos.
'''

class PilaConMaximo:

    def __init__(self):
        ''' Constructor de la clase pila con mámixo. '''
        self.elementos = []
        self.maximos = []
        self.cantidad = 0

    def esta_vacia(self):
        ''' Función que retorna true o False si hay o no elementos. '''
        return self.cantidad == 0

    def apliar(self, elemento):
        ''' Función que recibe un elemento y lo apila. '''
        if self.esta_vacia():
            self.maximos.append(elemento)
        else:
            tmp = self.elementos.pop()
            self.elementos.append(tmp)
            if tmp < elemento:
                self.maximos.append(elemento)
        self.elementos.append(elemento)
        self.cantidad += 1

    def desapilar(self):
        ''' Función que desapila el último elemento. '''
        return self.elementos.pop()

    
    def obtener_maximo(self):
        ''' Funcion que devuelve el máximo de una pila. '''
        return self.maximos.pop()
