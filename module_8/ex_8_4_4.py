'''
Consigna:
    Sistema de facturación simplificado
        Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de 
        (identificador, descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste en una tupla de (identificador, cantidad).
        Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada producto comprado, y al final imprima el total general.
        Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.
'''

def generar_lista_productos():
    result = []
    result.append((1, 'prod 1', 1))
    result.append((2, 'prod 2', 3))
    result.append((3, 'prod 3', 4))
    return result

def generar_lista_pedido():
    result = []
    result.append((1, 1))
    result.append((2, 5))
    return result

def buscar_producto(id, l):
    for p in l:
        if p[0] == id:
            return p
    return -1

def imprimir_factura(l):
    total = 0
    for i in l:
        total += i[3]
        print(f'Cantidad: {i[0]} | Descripción: {i[1]} | Precio unitario: {i[2]} | Total: {i[3]}')
    print(f'Total factura: {total}')

def generar_factura(l_prod, l_pedido):
    factura = []
    for i in l_pedido:
        prod = buscar_producto(i[0], l_prod)
        if prod != -1:
            factura.append((i[1], prod[1], prod[2], i[1] * prod[2]))
    
    imprimir_factura(factura)

generar_factura(generar_lista_productos(), generar_lista_pedido())