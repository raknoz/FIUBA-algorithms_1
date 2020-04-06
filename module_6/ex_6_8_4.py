'''
Consigna:
    Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
    '1234567890' , debe devolver '1.234.567.890'
'''

def insertar_separador_custom(s, r):
    result = ''
    for x in range(0, len(s), 3):
        result += s[x:x + 3] + r

    #Quito el último punto que se agrega
    print()

def separador_miles(s):
    s = s[::-1]
    result = ''
    
    for x in range(0, len(s), 3):
        result += s[x:x + 3] + '.'

    return result[:-1][::-1]

separador_miles('1234567890')