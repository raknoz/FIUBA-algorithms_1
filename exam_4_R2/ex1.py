'''
Consgina:
    La suma digital de un número n es la suma de sus dígitos. Escribir la función recursiva suma_digital(n) que recibe un número entero positivo 
    y devuelve su suma digital. No se permite convertir el número a cadena. Ejemplo: suma_digital(2019) → 12 (porque 2+0+1+9 = 12)
'''


def suma_digital(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digital(n // 10)
