def imprimir_datos_geometricos():
    pi = 3.14

    print('Calculos para un rectangulo')
    br = int(input("Ingrese la base: "))
    hr = int(input("Ingrese la altura: "))
    print(f'El perimetro es de: {(br * 2) + (hr * 2)} y el area es de: {br * hr}')

    x1 = int(input("Ingrese el valor de X1: "))
    x2 = int(input("Ingrese el valor de X2: "))
    y1 = int(input("Ingrese el valor de Y1: "))
    y2 = int(input("Ingrese el valor de Y2: "))
    

    print('Calculos para un circulo')
    rc = float(input("Ingrese el radio del circulo: "))
    print(f'El perimetro del circulo es {2 * pi * rc}')
    print(f'El area del circulo es {pi * (rc**2)}')

    print('Calculos para un triangulo rectangulo')
    ca = float(input("Ingrese un cateto del triangulo: "))
    cb = float(input("Ingrese otro cateto del triangulo: "))
    print(f'La hipotenusa es {(ca**2) + (cb**2)}')

imprimir_datos_geometricos()