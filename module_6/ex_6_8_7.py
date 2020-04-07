'''
Consigna:
    Escribir funciones que dadas dos cadenas de caracteres:
    a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena' es una subcadena de 'subcadena' .
    b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome' .
'''

def es_subcadena(s, t):
    '''
        Devuelve mensaje si la segunda cadena es una sub-cadena de la primera.
    '''
    return 'Es subacadena' if t in s else 'No es subcadena'

def devolver_por_orden(s, t):
    '''
        Devuelve la cadena más chica por orden alfabético.
    '''
    return s if s < t else t

#print(es_subcadena('subcadena', 'cadena'))
print(devolver_por_orden('kde', 'Gnome' ))


