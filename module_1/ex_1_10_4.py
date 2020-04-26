'''
Consigna:
    Implementar algoritmos que permitan:
        a) Calcular el perímetro de un rectángulo dada su base y su altura.
        b) Calcular el área de un rectángulo dada su base y su altura.
        c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2.
        d) Calcular el perímetro de un círculo dado su radio.
        e) Calcular el área de un círculo dado su radio.
        f) Calcular el volumen de una esfera dado su radio.
        g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''
PI = 3.14

def imprimir_datos_geometricos():
    '''
        Función que calcula áreas y perímetros de figuras geométricas en base a los datos pedidos al usuario.
        Todos los valores pedidos, deben ser positivos y mayores a 0.
    '''
    
    print('Calculos para un rectangulo')
    br = int(input("Ingrese la base: "))
    hr = int(input("Ingrese la altura: "))
    print(f'El perimetro es de: {(br * 2) + (hr * 2)} y el area es de: {br * hr}')

    x1 = int(input("Ingrese el valor de X1: "))
    x2 = int(input("Ingrese el valor de X2: "))
    y1 = int(input("Ingrese el valor de Y1: "))
    y2 = int(input("Ingrese el valor de Y2: "))

    base = abs( x2 - x1)
    altura = abs(y2 - y1)
    print(f'El area es de: {base * altura}')
    
    print('Calculos para un circulo')
    rc = float(input("Ingrese el radio del circulo: "))
    print(f'El perimetro del circulo es {2 * PI * rc}')
    print(f'El area del circulo es {PI * (rc**2)}')

    print('Calculos para un triangulo rectangulo')
    ca = float(input("Ingrese un cateto del triangulo: "))
    cb = float(input("Ingrese otro cateto del triangulo: "))
    print(f'La hipotenusa es {(ca**2) + (cb**2)}')

imprimir_datos_geometricos()