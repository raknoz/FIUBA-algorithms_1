'''
Consigna:
    Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios.
'''

def print_rush_mode(word):
    for x in range(1, 1000):
        print(word, end=' ')
    print('')

word = input("Ingrese una palabra: ")
print_rush_mode(word)