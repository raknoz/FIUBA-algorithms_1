'''
Consigna:
    Escribir funciones que permitan encontrar:
    a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a , b y c), indicando si es un máximo o un mínimo.
    b) Las raíces (reales o complejas) de un polinomio de segundo grado.
    Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raíz de un número negativo).
    c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
    Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
'''

def calular_vertice_x(a, b, c):
    x = (-1) * (b / (2 * a))
    return x

def calular_vertice_y(a, b, c, x):
    y = (a * (x**2)) + (b * x) + c
    return y

def evalua_raiz(a, b, c):
    return (b**2) - (4 * a * c)

def calcula_raiz(a, b, c):
    x1 = (calular_vertice_x(a, b, c) + ((evalua_raiz(a, b, c)** 0.2)/(2*a)))
    x2 = (calular_vertice_x(a, b, c) - ((evalua_raiz(a, b, c)** 0.2)/(2*a)))
    return x1, x2 

def vertice(a, b, c):
    '''
        Calcula el máximo o mínimo de un polinomio de segundo grado.
    '''
    if a == 0:
        return print('el valor a no puede ser 0')
    
    xv = calular_vertice_x(a, b, c)
    yv = calular_vertice_y(a, b, c, xv)

    if (a > 0):
        return print('Las coordenadas del vértice mínimo de la función es X = {} | Y = {}'.format( xv, yv ))
    
    return print('Las coordenadas del vértice máximo de la función es X = {} | Y = {}'.format(xv, yv ))

def raices(a, b, c):
    '''
        Calcula las raíces (reales o complejas) de un polinomio de segundo grado.
    '''
    if a == 0:
        return 'el valor a no puede ser 0'
    
    r = evalua_raiz(a, b, c)

    if r < 0:
        return print('La ecuación posee raíces complejas')
    elif r == 0:
        return print('La ecuación posee una raíz doble y es: {}'.format(calular_vertice_x(a, b, c)))
    else:
        x1, x2 = calcula_raiz(a, b, c)
        return print('La ecuación posee raíz doble y son: {} | {}'.format(x1, x2))

def interseccion(x1, t1, x2, t2):
    '''
        La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
    '''
    if( x1 == x2):
        return print('Las pendientes no pueden ser iguales.')
    
    valor_x = (t2 - t1) / (x1 - x2)
    valor_y = (x1 * valor_x) + t1

    return print('El punto de intersercción es en las coordenadas ({} , {})'.format(valor_x, valor_y))


vertice(1, -6, 5)
raices(2, 4, 3)
interseccion(5, 8, 3, -4)