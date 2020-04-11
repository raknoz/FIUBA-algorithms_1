'''
Consigna: 
    Matrices.
    a) Escribir una función que reciba dos matrices y devuelva la suma.
    b) Escribir una función que reciba dos matrices y devuelva el producto.
    c) * Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una matriz triangular superior.
    d) * Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son linealmente independientes o no.
'''

def dibujar_matriz(m):
    '''
        Función que se encarga de dibuhar una matriz
    '''
    rows = len(m)
    columns = len(m[0])
    for r in range(rows):
        for c in range(columns):
            print(f' {m[r][c]:6}', end= '|')
        print()
    return



def multiplica_vector(vec, p):
    '''
        Función que retorna el vector multiplicador por un número p
    '''
    return [p * x for x in vec]


def resta_vectores(vec1, vec2):
    '''
        Función que recibe dos vectores, los resta y devuelve el vector ressultado.
        vec1 y vec2 -> Tienen que tener la misma cantidad de elementos.
    '''
    result = []
    for i, vec in enumerate(vec1):
        result.append(vec - vec2[i])
    return result

def suma_matriz(m1, m2):
    '''
        Función que calcula la suma de dos matrices de igual tamaño.
    '''
    m_result = []
    rows = len(m1)
    columns = len(m1[0])

    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(m1[r][c] + m2[r][c])
        m_result.append(row)
        
    print(f'La suma de las matrices es: {m_result}')

def producto_matriz(m1, m2):
    '''
        Función que calcula el producto de dos matrices de igual tamaño.
    '''
    m_result = []
    rows = len(m1)
    columns = len(m1[0])

    for r in range(rows):
        row = []
        for c in range(columns):
            #print(f'r = {r} | c = {c}')
            row.append(m1[r][c] * m2[r][c])
        m_result.append(row)
        
    print(f'El producto de las matrices es: {m_result}')

def matriz_triangular_sup_3_x_3(m1):
    #Matriz resultado
    m_result = []
    # Obetengo el renglón 1
    r1 = m1[0]
    # Obetengo el renglón 2
    r2 = m1[1]
    # Obtengo el renglón 3 
    r3 = m1[2]

    # Inicio cálculo triangular inferior izquierdo

    #Multiplico el 3er renglón  con X1 del renglón 1 para obtener el primer 0 y el nuevo valor del r3
    r3 = resta_vectores(multiplica_vector(r3, r1[0]), multiplica_vector(r1, r3[0]))

    #Multiplico el 2do renglón con X1 para obtener el segundo 0 y el nuevo valor del r2
    r2 = resta_vectores(multiplica_vector(r2, r1[0]), multiplica_vector(r1, r2[0]))
    
    #Multiplico el 3er renglón con Y2 para obtner el tercer 0 y nuevo valor de r3
    r3 = resta_vectores(multiplica_vector(r3, r2[1]), multiplica_vector(r2, r3[1]))

    # Inicio cálculo triangular superior derecha

    #Multiplico el 1er renglón con Z3 para obtner el cuarto 0 y nuevo valor de r1
    r1 = resta_vectores(multiplica_vector(r1, r3[2]), multiplica_vector(r3, r1[2]))
    
    #Multiplico el 2er renglón con Z3 para obtner el quinto 0 y nuevo valor de r2
    r2 = resta_vectores(multiplica_vector(r2, r3[2]), multiplica_vector(r3, r2[2]))

    #Multiplico el 2er renglón con Y1 para obtner el quinto 0 y nuevo valor de r2
    r1 = resta_vectores(multiplica_vector(r1, r2[1]), multiplica_vector(r2, r1[1]))

    m_result.append(r1)
    m_result.append(r2)
    m_result.append(r3)

    dibujar_matriz(m_result)
    

#suma_matriz([[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]])
#producto_matriz([[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]])
#matriz_triangular_sup_3_x_3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_triangular_sup_3_x_3([[2, -1, 1], [3, 1, -2], [-1, 2, 5]])