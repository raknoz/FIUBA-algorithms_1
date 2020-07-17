'''
Consgina:
    Escribir una función que recibe una expresión matemática (en forma de cadena) y 
    devuelve True si los paréntesis ( '()' ), corchetes ( '[]' ) y llaves ( '{}' ) están correctamente balanceados, False en caso contrario
'''

def es_expresion_balanceada(s):
    pila = []

    for x in s:
        if x in '{[(':
            pila.append(x)
        else:
            tmp = pila.pop()

