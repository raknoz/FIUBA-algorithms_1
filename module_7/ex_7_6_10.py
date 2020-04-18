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
    '''
        Dada la matriz:
        r1 -> | X1 | Y1 | Z1 |
        r2 -> | X2 | Y2 | Z2 |
        r3 -> | X3 | Y3 | Z3 |

        Se piensa cómo una lista con renglones (r1-r2-r3)
        Se calcula la matriz triangular superior donde debe quedar cómo resultado:
        | X1' |  0  | 0   |
        | 0   | Y2' | 0   |
        | 0   | 0   | Z3' |

    '''

    #Matriz resultado
    m_result = []
    # Obetengo el renglón 1
    r1 = m1[0]
    # Obetengo el renglón 2
    r2 = m1[1]
    # Obtengo el renglón 3 
    r3 = m1[2]

    # Inicio cálculo triangular inferior izquierdo

    #Multiplico R3 * X1 y R1 * X3 => para obtener el 1er 0 y el nuevo valor del R3
    r3 = resta_vectores(multiplica_vector(r3, r1[0]), multiplica_vector(r1, r3[0]))

    #Multiplico R2 * X1 y R1 * X2 => para obtener el 2do 0 y el nuevo valor del R2
    r2 = resta_vectores(multiplica_vector(r2, r1[0]), multiplica_vector(r1, r2[0]))
    
    #Multiplico R3 * Y2 y R2 * Y3 => para obtener el 3er 0 de r3
    r3 = resta_vectores(multiplica_vector(r3, r2[1]), multiplica_vector(r2, r3[1]))

    # Inicio cálculo triangular superior derecha

    #Multiplico R1 * Z3 y R3 * Z1 => para obtner el 4to 0 y nuevo valor de R1
    r1 = resta_vectores(multiplica_vector(r1, r3[2]), multiplica_vector(r3, r1[2]))
    
    #Multiplico R2 * Z3 y R1 * Z2 => para obtner el 5to 0 y nuevo valor de R2
    r2 = resta_vectores(multiplica_vector(r2, r3[2]), multiplica_vector(r3, r2[2]))

    #Multiplico R1 * Y2 y R2 * Y1 => para obtner el 6to 0 y nuevo valor de R1
    r1 = resta_vectores(multiplica_vector(r1, r2[1]), multiplica_vector(r2, r1[1]))

    m_result.append(r1)
    m_result.append(r2)
    m_result.append(r3)

    dibujar_matriz(m_result)
    

#suma_matriz([[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]])
#producto_matriz([[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]])
#matriz_triangular_sup_3_x_3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_triangular_sup_3_x_3([[2, -1, 1], [3, 1, -2], [-1, 2, 5]])