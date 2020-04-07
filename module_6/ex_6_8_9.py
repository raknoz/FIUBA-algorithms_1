'''
Consigna:
    Implementar la función pedir_entero(mensaje, min, max) , que debe imprimir el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
    número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, 
    la función lo debe devolver.
'''
def mostrar_mensaje(mensaje):
    return print(mensaje)

def pedir_numero(mensaje, min, max):
    z = input(f'{mensaje} [{min}..{max}]: ')

    # Si lo ingresado no es un dígito y está fuera del min y max vuelve a pedir el dato
    while (not z.isdigit() or (int(z) > max or int(z) < min)):
        mostrar_mensaje(f'Por favor ingresa un número entre [{min}..{max}].')
        z = input(f'{mensaje} [{min}..{max}]: ')

    return z


x = pedir_numero("¿Cuál es tu número favorito?", -50, 50)
print(x)
