'''
Consigna:
    Agenda simplificada
    Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
    la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.
'''

def genera_lista_agenda():
    result = []
    result.append(['Jose Perez', '11-12345667'])
    result.append(['Maria Alfonso', '11-12345667'])
    result.append(['Pedro Gutierrez', '11-12345667'])
    result.append(['Matin Alvarez', '11-12345667'])
    result.append(['Diego Aquino', '11-12345667'])
    return result

def busca_en_agenda(l, c):
    result = []
    for t in l:
        if c.upper() in t[0].upper():
            result.append(t)

    print(result)

busca_en_agenda(genera_lista_agenda(), 're')

