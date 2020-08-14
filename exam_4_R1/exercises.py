'''
Consigna:
    1. Dada una lista de Python que contiene únicamente números, implementar una función recursiva que elimine de dicha lista los números pares. 
'''

def _remover_pares(lista):
    if len(lista) == 0:
        return []
    
    elemento = lista.pop(0)
    #Sin parentesis, no anda
    return ([elemento] if elemento % 2 != 0 else []) + _remover_pares(lista)