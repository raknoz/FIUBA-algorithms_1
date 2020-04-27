'''
Consigna:
    Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.
'''

def convertir_a_decimal(b):
    '''
        Convierte un valor binario en decimal
    '''
    result = 0
    #Invierto la cadena
    b = b[::-1]
    #Recorro cada elemento y lo multiplico por la potencia de 2 correspondiente
    for x in range(0, len(b)):
        result += int(b[x]) * (2 ** x)
    
    return result