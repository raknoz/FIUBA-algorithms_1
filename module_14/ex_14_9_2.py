'''
Consigna:
    Modificar el método __lt__ de Hotel para poder ordenar de menor a mayor las listas de hoteles según el criterio: 
    primero por ubicación, en orden alfabético y dentro de cada ubicación por la relación calidad-precio.
'''

class Hotel:
    """Representa un hotel: sus atributos son: nombre, ubicacion, puntaje y precio."""

    def validar_cadena_no_vacia(self, valor):
        '''
            Valida si la cadena está vacía y la devuelve. En caso contrario lanza TypeError.
        '''
        if not valor:
            raise TypeError(f"La cadena ingresada está vacía")
        return valor

    def validar_numero_positivo(self, valor):
        '''
            Si el valor es numérico y positivo, lo devuelve. En caso contrario lanza TypeError.
        '''
        if not isinstance(valor, (int, float, complex)) or valor < 0:
            raise TypeError("{:r} no es un valor numérico".format(valor))
        return valor

    def __init__(self, nombre, ubicacion, puntaje, precio):
        """Crea un Hotel. nombre y ubicacion deben ser cadenas no vacías, puntaje y precio son números."""
        self.nombre = self.validar_cadena_no_vacia(nombre)
        self.ubicacion = self.validar_cadena_no_vacia(ubicacion)
        self.puntaje = self.validar_numero_positivo(puntaje)
        self.precio = self.validar_numero_positivo(precio)

    def __str__(self):
        """Conversión a cadena de texto."""
        return "{} de {} - Puntaje: {} - Precio: {} pesos".format(self.nombre, self.ubicacion, self.puntaje, self.precio)

    def ratio(self):
        """Calcula la relación calidad-precio de un hotel"""
        return ((self.puntaje ** 2) * 10) / self.precio

    #Less than
    def __lt__(self, otro):
        """Compara dos hoteles según sus ratios."""
        return self.ubicacion < otro.ubicacion and self.ratio() < otro.ratio()