'''
Consigna:
    Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
    • 1 es impar.
    • Si un número es impar, su antecesor es par; y viceversa.
'''

def par(n):
    if n == 1:
        return False
    return True and impar(n - 1)

def impar(n):
    if n == 1:
        return True
    return True and par(n - 1)