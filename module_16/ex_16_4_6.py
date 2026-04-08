'''
Consgina:
    Escribir una función que recibe una expresión matemática (en forma de cadena) y 
    devuelve True si los paréntesis ( '()' ), corchetes ( '[]' ) y llaves ( '{}' ) están correctamente balanceados, False en caso contrario.
'''
from Pila import Pila

def es_expresion_balanceada(s):
    pila = Pila()

    for x in s:
        if x in '{[(':
            pila.apilar(x)
        elif x in ')]}':

            if len(pila) == 0:
                return False

            # Seteo que expresión busco
            tmp = '('
            if x == ']':
                tmp = '['
            elif x == '}':
                tmp = '{'

            #Desapilo el ultimo
            ult = pila.desapilar()
            if ult != tmp:
                return False

    return True