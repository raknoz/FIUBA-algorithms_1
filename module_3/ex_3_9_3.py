'''
Consigna:
    Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
    más grande que se puede obtener entre ellos (8 = −2 × −4).
'''
def procesa_datos(lista):
    '''
        Obtiene una lista y multiplica todos los elementos de la misma
    '''
    valores = []
    for x in range(len(lista)-1):
        for j in lista[x + 1::]:
            valores.append(lista[x] * j)
    
    print(max(valores))

procesa_datos([1, 5, -2, -4])

