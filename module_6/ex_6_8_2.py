'''
Consigna:
    Escribir funciones que dada una cadena y un caracter:
    a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'
    b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'
    c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'
    d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'
'''

def insertar_separador(s, c):
    return c.join(s)

def reemplazar_caracteres(s, r):
    return s.replace(' ', r)

def reemplazar_digitos(s, r):
    return ''.join(r if c.isdigit() else c for c in s)

def insertar_separador_custom(s, r):
    result = ''
    for x in range(0, len(s), 3):
        result += s[x:x + 3] + r

    #Quito el último punto que se agrega
    print(result[:-1])



#print(insertar_separador('separador', ','))
#print(reemplazar_caracteres('mi archivo de texto.txt', '_'))
#print(reemplazar_digitos('su clave es: 1540', 'X'))

insertar_separador_custom('255255255012', '.')