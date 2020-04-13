'''
Consigna:
    ⋆ Plegado de un texto. Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas
    correctamente en los espacios (sin cortar las palabras).
'''

# Está incompleto

def texto_plegado(texto, limite):
    result = []
    palabras = texto.split()
    largo_palabras = len(palabras)
    frase = ''
    index = 0

    while index < largo_palabras:
        palabra = palabras[index]
        #print(f'entrada => index: {index} | Palabra: {palabra} | frase: {frase} | largo frase:{len(frase)} | result: {result}')
        
        if len(palabra) <= limite:
            if len(frase) + len(palabra) <= limite:
                frase += f'{palabra} '
            elif frase != '':
                #Remuevo espacio final
                frase = frase[:-1]
                result.append(frase)
                frase = f'{palabra} '
            
                
            #print(f'salida => index: {index} | Palabra: {palabra} | frase: {frase} | largo frase:{len(frase)} | result: {result}')
        index += 1

    # Si coincide hay que evaluar la palabra
    # Si no coincide hay que guardar la frase y trabajar la palabra por separado
    print(f'(corte) index: {index} | Palabra: {palabra} | frase: {frase} | largo frase:{len(frase)} | result: {result}')


texto_plegado('welc come to the jungle my loves', 6)