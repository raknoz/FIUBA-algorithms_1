import vectores

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    '''
        Calcula el producto vectorial de los 3 puntos
    '''
    ab1, ab2, ab3 = vectores.diferencia(x1, y1, z1, x2, y2, z2)
    ac1, ac2, ac3 = vectores.diferencia(x1, y1, z1, x3, y3, z3)
    pv1, pv2, pv3 = vectores.producto_vectorial(ab1, ab2, ab3, ac1, ac2, ac3)
    ' Calculo la norma del producto vectorial'
    norma_abac = vectores.norma(pv1, pv2, pv3)

    'Divido por dos'
    return norma_abac / 2

assert round(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0), 3) == 195316.00
assert round(area_triangulo(-2, 0, 2, -5, 2, 0, 6, -3, 7), 3) == 8.516
assert round(area_triangulo(1, 2, -3, 2, 3, 1, 0, -2, 1), 3) == 10.874