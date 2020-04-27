'''
Consigna:
    a) Escribir una función que reciba las coordenadas de un vector en R 3 ( x,y,z ) y devuelva la norma del vector.
    b) Escribir una función que reciba las coordenadas de dos vectores en R 3 ( x1,y1,z1,x2, y2,z2 ) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
    Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)
    c) Escribir una función que reciba las coordenadas de dos vectores en R 3 y devuelva las coordenadas del producto vectorial
    d) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de 3 puntos en R 3 y devuelva el área del triángulo que conforman. es × AC
    Ayuda: Si A, B y C son 3 puntos en el espacio, la norma del producto vectorial AB
    igual al doble del área del triángulo ABC.
    Ejemplo: area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) → 19.4551
    e) Escribir una función que reciba las coordenadas de 4 puntos en el plano R 2 ( x1, y1, x2, y2, x3, y3, x4, y4 )
    que conforman un cuadrilátero convexo, y devuelva el área del mismo.
    Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados están en R 3 con coordenada z = 0.
    Ejemplo: area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) → 65
'''

def norma(v1, v2, v3):
    '''
        Módulo o longitud de un vector en el plano R3 (x , y, z) 
    '''
    vector = [v1, v2, v3]
    return (sum([x**2 for x in vector])) ** 0.5

def diferencia(x1, y1, z1, x2, y2, z2):
    '''
        Función que retorna la diferencia entre dos vectores de R3
    '''
    return (x1-x2), (y1-y2), (z1-z2)

def producto_vec(x1, y1, z1, x2, y2, z2):
    '''
        Función que calcula el producto vectoriano de 2 vectores en R3
    '''
    #return (y1 * z2)-(z1 * y2), (z1 * x2)-(x1 * z2), (x1 * y2)-(y1 * x2)
    return diferencia((y1 * z2), (z1 * x2), (x1 * y2), (z1 * y2), (x1 * z2), (y1 * x2))

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    '''
        Calcula el producto vectorial de los 3 puntos
    '''
    ab1, ab2, ab3 = diferencia(x1, y1, z1, x2, y2, z2)
    ac1, ac2, ac3 = diferencia(x1, y1, z1, x3, y3, z3)
    pv1, pv2, pv3 = producto_vec(ab1, ab2, ab3, ac1, ac2, ac3)

    ' Calculo la norma del producto vectorial'
    norma_abac = norma(pv1, pv2, pv3)

    'Divido por dos'
    return norma_abac / 2

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
        Calcula el área de un cuadrilatero pasandole por parámetro sus puntos en el plano R2
    '''
    ab1, ab2, ab3 = producto_vec(x1, y1, 0, x2, y2, 0)
    bc1, bc2, bc3 = producto_vec(x2, y2, 0, x3, y3, 0)
    cd1, cd2, cd3 = producto_vec(x3, y3, 0, x4, y4, 0)
    da1, da2, da3 = producto_vec(x4, y4, 0, x1, y1, 0)

    suma_norma = norma(ab1, ab2, ab3) + norma(bc1, bc2, bc3) + norma(cd1, cd2, cd3) + norma(da1, da2, da3)

    return suma_norma / 2