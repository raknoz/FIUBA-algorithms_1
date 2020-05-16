'''
Consigna:
    Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio, desglosado por tipo de billete 
    (por ejemplo, en el quiosco de la esquina hay 6 billetes de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos).
    Las denominaciones permitidas son 1, 2, 5, 10, 20, 50, 100, 200, 500 y 1000 pesos.
'''

class Caja:
    DENOMINACIONES = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

    def valida_billetes(self, d_billetes):
        '''Función que se encarga de validar que las denominaciones sean las permitidas, sino da error'''
        for k, v in d_billetes.items():
            if k not in self.DENOMINACIONES:
                raise ValueError(f'Denominación {k} no permitida')
    
    def valida_quitar(self, d_quitar):
        '''Valida que haya la cantidad de billetes de cada denominación, sino da error'''
        for k, v in d_quitar.items():
            if self.billetes[k] < v:
                raise ValueError(f'No hay suficientes billetes de denominación {k}')

    def __init__(self, d_billetes):
        '''Constructor de la caja, recibe un diccionario<denominacion:cantidad> cómo parámetro'''
        self.valida_billetes(d_billetes)
        self.billetes = d_billetes

    def __str__(self):
        '''Función que devuelve la representación en string'''
        return f'Caja {self.billetes} total: {sum([k * v for k, v in self.billetes.items()])} pesos'
    
    def agregar(self, d_agregar):
        '''Función que agrega billetes a la caja Valida que sean de denominación permitida'''
        self.valida_billetes(d_agregar)
        for k, v in d_agregar.items():
            if k in self.billetes:
                self.billetes[k] += v
            else:
                self.billetes[k] = v
    
    def quitar(self, d_quitar):
        '''Función que quita billetes de la caja'''
        self.valida_billetes(d_quitar)
        self.valida_quitar(d_quitar)

        for k, v in d_quitar.items():
            if k in self.billetes:
                self.billetes[k] -= v

        return print(sum([k * v for k, v in d_quitar.items()]))