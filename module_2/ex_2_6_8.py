'''
Consigna:
    Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.
'''

def dibujaDomino():
    for x in range (0,7):
        for h in range (x,7):
            print(f'|{x}|{h}|')

dibujaDomino()