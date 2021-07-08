'''
Consigna:
    Escribir funciones que dada una cadena de caracteres:
    a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver 'lgrtms' .
    b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe devolver 'i ooae' .
    c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe devolver 'vistaerou' .
    d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

LETRAS_VOCALES = ['a', 'e', 'i', 'o', 'u']

def siguiente_vocal(v):
    '''
        Función que devuelve la siguiente vocal.
    '''
    if v.lower() == 'u':
        return 'a'
    #Obtengo la posición en la lista y retorno la sigueente
    return LETRAS_VOCALES[LETRAS_VOCALES.index(v) + 1]
    
def devolver_consonantes(s):
    '''
        Función que se encarga de retornar solo las constantes de la cadena s.
    '''
    result = ''
    for c in s.lower():
        if not c in LETRAS_VOCALES:
            result += c
    return result

def devolver_vocales(s):
    '''
        Función que devuelve solo las vocales de la cadena s.
    '''
    result = ''
    for c in s.lower():
        #Valido que sea vocal u otro caracter especial o espacio
        if c in LETRAS_VOCALES or not c.isalpha():
            result += c

    return result

def cambiar_vocales(s):
    '''
        Función que recorre una lista y cuando encuentra una vocal la cambia por la siguiente.
    '''
    result = ''

    for c in s.lower():
        if c in LETRAS_VOCALES:
            result += siguiente_vocal(c)
        else:
            result += c
    
    return result

def es_palindromo(s):
    '''
        Función que valida si una cadena es palindromo o no.
    '''
    #Le quito los espacios y pongo todo en minúscula
    s = s.replace(' ', '').lower()
    #Comparo la cadena original con el reverso
    if s == s[::-1]:
        return 'Es palindromo'
    
    return 'No es palindromo'