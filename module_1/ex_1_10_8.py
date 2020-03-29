'''
Consigna:
    Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios.
'''

def printRushMode(word):
    for x in range(1, 1000):
        print(word, end=' ')
    print('')

word = input("Ingrese una palabra: ")
printRushMode(word)