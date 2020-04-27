'''
Consigna:
    Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.
'''

def insertar_separador(s, c, l):
    indice = 0
    result = ''
    while indice < l:
        result +=s[indice] + c
        indice += 1
    
    result += s[indice:]
    
    return result

def reemplazar_caracteres(s, r, l):
    return s.replace(' ', r, l)

def reemplazar_digitos(s, r, l):
    indice = 0
    reemplazos = 0
    result = ''
    while indice < len(s) and reemplazos < l:
        if(s[indice].isdigit()):
            result += r
            reemplazos += 1
        else:        
            result += s[indice]
        indice += 1

    result += s[indice:]

    return result

def insertar_separador_custom(s, r, l):
    result = ''
    reemplazos = 0
    indice = 1

    while reemplazos < l and indice < len(s):
        if(indice % 3 == 0):
            result += s[indice -1] + r
            reemplazos += 1
        else:
            result += s[indice -1]
        
        indice += 1
    
    result += s[(indice-1):]
    print(result)