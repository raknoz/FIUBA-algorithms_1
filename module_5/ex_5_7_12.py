'''
Consigna:
    Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un
    grupo de examenes. 
    Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. 
    Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.
'''
 
def minimo_aprobado(t, p):
    '''
        Retorna el numero de ejercicios necesarios para aprobar.
    '''
    return (p * t) // 100

def porcentaje_aprobado(t, ta):
    '''
        Retorna el porcentaje de ejercicios resueltos
    '''
    return (ta * 100) / t

def cargar_ejercicio():
    '''
        Pide los ejercicios resultos por teclado
    '''
    return input('Ingrese la cantidad de ejercicios resueltos correctamente por el alumno (* para finalizar): ')

def evalua_examenes(t, p):
    alumnos_examenes = {}
    examen_aprobado = minimo_aprobado(t, p)
    ejercicios_ok = cargar_ejercicio()
    indice = 0

    while ejercicios_ok != '*':
        p_resuelto = porcentaje_aprobado(t, int(ejercicios_ok))
        estado_examen = 'Aprobado' if int(ejercicios_ok) >= examen_aprobado else 'No aprobado'
        
        #Armo la tupla de información para mostrar
        alumnos_examenes[indice] = [t, p_resuelto, estado_examen]
        
        indice += 1
        ejercicios_ok = cargar_ejercicio()

    

    for v in alumnos_examenes.values():
        print(f'El alumno realizó el {v[1]}% de {v[0]} ejercios y el estado es {v[2]}')


evalua_examenes(10, 70)






    