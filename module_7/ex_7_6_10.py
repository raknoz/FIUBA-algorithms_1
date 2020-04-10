'''
Consigna: 
    Matrices.
    a) Escribir una función que reciba dos matrices y devuelva la suma.
    b) Escribir una función que reciba dos matrices y devuelva el producto.
    c) Escribir una función que opere sobre una matriz y mediante eliminación gaussiana de vuelva una matriz triangular superior.
    d) Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son linealmente independientes o no.
'''

def suma_matriz(m1, m2):
    m_result = [] * len(m1)

    for c in range(len(m1)):
        
        for f in range(len(m1[c])):
            print(f'c = {c}')
            print(f'f = {f}')
        
    print(m_result)



suma_matriz([[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]])