'''
Consigna:
    Escribir un programa que pregunte al usuario:
        a) su nombre, y luego lo salude.
        b) dos números, y luego muestre el producto.
'''
def imprimir_saludo():
    '''
        Función que pide por teclado el nombre de un usuario y lo saluda.
        Luego calcula el producto de dos números pedidos por teclado.
    '''

    name = input("Ingrese su nombre: ")
    print(f'Hola {name}')

def imprimir_producto():
    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))
    print(f'el producto de {n1} y {n2} es { n1 * n2}') 

imprimir_saludo()
imprimir_producto()