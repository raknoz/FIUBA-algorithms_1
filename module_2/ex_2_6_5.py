'''
Consigna:
    Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
'''
def pares_entre_valores(n1, n2):
    '''
        Función que le recibe dos valores n1 y n2 e imprime los valore pares entre ambos.
    '''
    for n in range(n1, n2 + 1):
        if(n%2 == 0):
            print(n)

def main(): 
    '''
        Función principal que se encargar de pedirle los datos al usuario para procesarlos.
    '''
    n1 = int(input('Ingrese el limite inferior: '))
    n2 = int(input('Ingrese el limite superior: '))
    pares_entre_valores(n1, n2)

main()
