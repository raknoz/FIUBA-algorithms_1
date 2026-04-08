'''
Consigna:
    Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
        >>> analisis2 = Materia("61.03", "Análisis 2", 8)
        >>> fisica2 = Materia("62.01", "Física 2", 8)
        >>> algo1 = Materia("75.40", "Algoritmos 1", 6)
        >>> c = Carrera([analisis2, fisica2, algo1])
        >>> str(c)
        Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
        >>> c.aprobar("95.14", 7)
        ValueError: La materia 95.14 no es parte del plan de estudios
        >>> c.aprobar("75.40", 10)
        >>> c.aprobar("62.01", 7)
        >>> str(c)
        Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
        75.40 Algoritmos 1 (10)
        62.01 Física 2 (7)
'''

class Carrera:
    '''Constructor de la carrera, recibe una lista de Materias cómo parámetro'''

    def cargar_materias(self, materias):
        '''Función que recibe una lista de materias y devuelve un diccionario'''
        d_materias = {}
        for m in materias:
            d_materias[m.codigo] = m

        return d_materias

    def valida_materia(self, codigo):
        '''Valida si el código de la materia existe'''
        if codigo not in self.d_materias.keys():
            raise ValueError(f'La materia {codigo} no es parte del plan de estudios')

    def obtener_creditos(self):
        '''Función que devuelve la suma de los créditos de las materias aprobaas'''
        l_creditos = []
        for k in self.d_materias_aprobadas.keys():
            l_creditos.append(self.d_materias[k].creditos)
        return sum(l_creditos)

    def aprobar(self, codigo, nota):
        '''Función que se encarga de aprobar una materia, sino existe la materia da error'''
        self.valida_materia(codigo)
        self.d_materias_aprobadas[codigo] = nota

    def obtener_promedio(self):
        '''Función que devuelve el promedio de las materias aprobadas'''
        if len(self.d_materias_aprobadas) == 0:
            return 'N/A'

        return sum([n for n in self.d_materias_aprobadas.values()]) / len(self.d_materias_aprobadas)

    def __init__(self, materias):
        '''Constructor de la clase, recibe una lista de Materias'''
        self.d_materias = self.cargar_materias(materias)
        self.d_materias_aprobadas = {}

    def __str__(self):
        print (f'Créditos: {self.obtener_creditos()} -- Promedio: {self.obtener_promedio()} -- Materias aprobadas: ')
        for k, v in self.d_materias_aprobadas.items():
            print(f'{k} {self.d_materias[k].nombre} ({v})')
        return ''

class Materia:
    '''Constructor de la Materia, recibe un nombre, un código de identificación y créditos cómo parámetro'''
    def validar_cadena_no_vacia(self, valor):
        ''' Valida si la cadena está vacía y la devuelve. En caso contrario lanza TypeError.'''
        if not valor:
            raise TypeError(f"El nombre de la carrera está vacía")
        return valor
    
    def validar_numero_positivo(self, valor):
        ''' Si el valor es numérico y positivo, lo devuelve. En caso contrario lanza TypeError.'''
        if not isinstance(valor, (int, float, complex)) or valor < 0:
            raise TypeError(f'{valor} no es un valor numérico')
        return valor

    def __init__(self, codigo, nombre, creditos):
        '''Constructor de la clase'''
        self.nombre = self.validar_cadena_no_vacia(nombre)
        self.codigo = self.validar_cadena_no_vacia(codigo)
        self.creditos = self.validar_numero_positivo(creditos)

    def __eq__(self, value):
        return self.codigo == value