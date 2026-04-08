''' Ex 1 
    Escribir una funcion que reciba una lista de pedidos a un supermercado, donde cada pedido tiene la siguiente formato: { nombre_producto1: cant1, …, nombre_producto_n: cant_n }  y escriba un archivo que tenga el resumen de los pedidos con el siguiente formato:
    nombre_producto;cant_total

    donde cada producto está una única vez y la cantidad total es la cantidad de todas las peronas que compraron ese producto.
    Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
'''
def pre_procesa_pedidos(d_pedidos):
    ''' Funcion que procesa todos los pedidos y lo acumula por nombre de producto'''
    d_resultado = {}
    for nom_prod, cant_prod in d_pedidos.items():
        d_resultado[nom_prod] = d_resultado.get(nom_prod, 0) +cant_prod
    return d_resultado
    
def procesa_pedidos(d_pedidos):
    d_resultado = pre_procesa_pedidos(d_pedidos)
    with open('pedidos.txt', 'w') as pedidos:
        for nombre, cantidad in d_resultado.items():
            pedidos.write(f'{nombre};{cantidad}\n')


'''
    Ex 2
    2) Se tiene un archivo de texto que contiene un díálogo entre una cantidad de personas desconocida, de manera que cada línea del archivo 
    tiene este formato "PersonaN: una frase de cierta cantidad de palabras" (asumir que las frases contienen únicamente palabras, no contienen signos de puntuacion, 
    ni numeros, ni ningun caracter que no sean letras o espacios).
    Escribir una funcion que reciba la ruta a un archivo de este tipo y devuelva cuantas veces dijo cada palabra cada una de las personas involucradas en el díalogo 
    (es decir, debe devolver un diccionario con el siguiente formato: { persona_1: { palabra_1: cant_1, palabra_2: cant_2 }, persona_2: { ... } .. }
'''

def procesa_linea(linea, d_dialogo):
    ''' Función que procesa la linea de texto y devuelve un diccionario con las palabras que apareces '''
    tmp_datos = linea.rstrip('\n').split(':')
    nom_persona, palabras = tmp_datos[0], tmp_datos[1:]
    d_palabras = d_dialogo.get(nom_persona, {})

    for palabra in palabras.split(' '):
        d_palabras[palabra] = d_palabras.get(palabra, 0) + 1
    d_dialogo[nom_persona] = d_palabras
    
    return d_dialogo

def procesa_dialogo(archivo):
    ''' Función que procesa un archivo de dialogo y devuelve un mapa con la cantidad de palabras escritas por personas '''
    d_dialogo = {}
    with open(archivo, 'r') as dialogo:
        for linea in dialogo:
            procesa_linea(linea, d_dialogo)
    
    return d_dialogo


''' 
    Ex 3 
    Implementar la clase CajaFuerte que reproduzca el siguiente comportamiento:
    >>> caja = CajaFuerte(9158)
    >>> caja.esta_abierta()
    False
    >>> caja.guardar("pulsera")
    Exception: La caja fuerte está cerrada
    >>> caja.abrir(1234)
    Exception: La clave es inválida
    >>> caja.abrir(9158)
    >>> caja.esta_abierta()
    True
    >>> caja.guardar("pulsera")
    >>> caja.guardar("reloj de oro")
    Exception: No se puede guardar más de una cosa
    >>> caja.cerrar()
    >>> caja.sacar()
    Exception: La caja fuerte está cerrada
    >>> caja.abrir(9158)
    >>> caja.sacar()
    'pulsera'
    >>> caja.sacar()
    Exception: No hay nada para sacar
'''

class CajaFuerte():
    ''' Clase que representa una caja fuerte '''
    
    def __init__(self, clave):
        ''' Constructor de la clase que recibe la clave con la que se abre '''
        self.clave = clave
        self.abierta = False
        self.item = None

    def esta_abierta(self):
        ''' Funcion que devuelve true or false si la caja está abierta '''
        print(self.abierta)
    
    def abrir(self, psw=None):
        ''' Función que intenta abrir la caja fuerte con el PSW que se le pasa por parámetro '''
        if psw != self.clave:
            raise Exception('La clave es inválida')
        self.abierta = True        

    def cerrar(self):
        ''' Función que cierra la caja fuerte '''
        self.abierta = False

    def esta_vacia(self):
        ''' Función que retorna true o false si tiene algo guardado '''
        return self.item is None

    def sacar(self):
        ''' Función que retorna el elemento guardado, en caso de que no haya nada da un error'''
        if not self.esta_abierta():
            raise Exception('La caja fuerte está cerrada')
        if self.esta_vacia():
            raise Exception('No hay nada para sacar')
        aux = self.item
        self.item = None
        print(aux)
        return aux
    
    def guardar(self, item):
        if not self.esta_abierta():
            raise Exception('La caja fuerte está cerrada')
        if not self.esta_vacia():
            raise Exception('No se puede guardar más de una cosa')
        self.item = item

    