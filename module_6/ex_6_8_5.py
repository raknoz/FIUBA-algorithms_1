'''
Consigna:
    Escribir una función que dada una cadena de caracteres, devuelva:
    a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB' .
    b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina' .
    c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer'
'''

def primera_letra(s):
    lista = s.split()
    result = ''

    for e in lista:
        result += e[0]

    return result

def letra_capital(s):
    lista = s.split()
    result = []

    for e in lista:
        result.append(e.capitalize())
    
    return ' '.join(result)

def letra_capital_a(s):
    lista = s.split()
    result = []

    for e in lista:
        result.append(e.capitalize() if e[0] == 'a' else e)
    
    return ' '.join(result)