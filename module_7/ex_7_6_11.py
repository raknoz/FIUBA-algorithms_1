'''
Consigna:
    ⋆ Plegado de un texto. Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas
    correctamente en los espacios (sin cortar las palabras).
'''

# Está incompleto

def texto_plegado(texto, limite):
    result = []
    palabras = texto.split()
    frase = ''

    for index, palabra in enumerate(palabras):        
        if len(palabra) <= limite:
            if len(frase) + len(palabra) <= limite:
                frase += f'{palabra} '
            elif frase != '':
                #Remuevo espacio final
                frase = frase[:-1]
                result.append(frase)
                frase = f'{palabra} '
        
        if index == len(palabras) - 1:
            frase = frase[:-1]
            result.append(frase)

    print(result)

texto_plegado('welc come to the jungle my loves yeah a', 6)