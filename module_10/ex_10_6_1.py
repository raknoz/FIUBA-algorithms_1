'''
Consigna:
    Analizar cada una de las siguientes funciones. ¿Cuál es el contrato de la función?
    ¿Cómo sería su documentación? ¿Es necesario agregar comentarios? ¿Se puede simplificar
    el código y/o mejorar su legibilidad? ¿Hay algún invariante de ciclo?
'''

#A
# ¿Cuál es el contrato de la función? -> Abs(i).
# ¿Cómo sería su documentación? -> Función que devuelve el valor absluto del parámetro i.
# ¿Es necesario agregar comentarios? -> No.
# ¿Se puede simplificar el código y/o mejorar su legibilidad? -> Es bastante simple.
# ¿Hay algún invariante de ciclo? -> No.
def Abs(i): 
    if i >= 0:
        return i
    else:
        return -i

#B
# ¿Cuál es el contrato de la función? -> emails(diccionario).
# ¿Cómo sería su documentación? -> Función que imprime el email de cada persona.
# ¿Es necesario agregar comentarios? -> No.
# ¿Se puede simplificar el código y/o mejorar su legibilidad? -> Es bastante simple.
# ¿Hay algún invariante de ciclo? -> No.
def emails(diccionario):
    for k, v in diccionario.items():
        print(f"El e-mail de {k} es {v}")

#C
# ¿Cuál es el contrato de la función? -> emails2(diccionario).
# ¿Cómo sería su documentación? -> Función que retorna la lista de personas que tienen si tiene emails.
# ¿Es necesario agregar comentarios? -> Si, explicando la funcionalidad.
# ¿Se puede simplificar el código y/o mejorar su legibilidad? -> Si, con el comprehension.
# ¿Hay algún invariante de ciclo? -> Si, solo devuelve los que contienen email.
def emails2(diccionario):
    buenos = {}
    for k, v in diccionario.items():
        if '@' in v:
            buenos[k] = v
    return buenos

#D
# ¿Cuál es el contrato de la función? -> emails3(nombres, direcciones).
# ¿Cómo sería su documentación? -> Función que busca por nombre en la lista de direcciones los emails y crea uno si no tienen.
# ¿Es necesario agregar comentarios? -> Si, explicando la funcionalidad.
# ¿Se puede simplificar el código y/o mejorar su legibilidad? -> Separando la creación del email en un método aparte. y usando comprehension.
# ¿Hay algún invariante de ciclo? -> Si, solo se hace el proceso con los que no tienen email.
def emails3(nombres, direcciones):
    for nom in range(len(nombres)):
        if direcciones[nom] == None:
            nombre, apellido = ' '.split(nombres[nom].lower())
            direcciones[nom] = nombre[0] + apellido + '@ejemplo.com'