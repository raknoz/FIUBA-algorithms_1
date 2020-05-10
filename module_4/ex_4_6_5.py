'''
Consignas:
    Escribir funciones que resuelvan los siguientes problemas:
    a) Dado un año indicar si es bisiesto.
    Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
    b) Dado un mes y un año, devolver la cantidad de días correspondientes.
    c) Dada una fecha (día, mes, año), indicar si es válida o no.
    d) Dada una fecha, indicar los días que faltan hasta fin de mes.
    e) Dada una fecha, indicar los días que faltan hasta fin de año.
    f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
    g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
    Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
'''
MESES_DIAS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def es_bisiesto(y):
    '''
        Función que retorna True o False si un año es o no bisiesto.
    '''
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0
        
def contador_dias(m, y):
    '''
        Función que devuelve el total de días transcurridos hasta un mes determinado.
    '''
    total_dias = 0  
    for x in range(1, m + 1):
        total_dias+= MESES_DIAS[x]

    if es_bisiesto(y) and m > 1:
        total_dias+=1
    return total_dias

def evalua_fecha(d, m, y):
    '''
        Comprueba si una fecha pasada por parámetro es vádida.
    '''
    if  (d < 1 or d > 31) or (m < 1 or m > 12) or (y < 1):
        return False
    
    if m == 2 and not es_bisiesto(y) and d > 28:
        return False
    
    return not (m != 2 and d > MESES_DIAS[m])

def dias_hasta_fin_de_mes(d, m, y):
    '''
        Retorna la cantidad de días que faltan hasta fin de mes de la fecha pasada por parámetros.
    '''
    dias_total = MESES_DIAS[m]
    if m == 2 and es_bisiesto(y):
        dias_total +=1
    return dias_total - d

def dias_hasta_fin_de_anio(d, m, y):
    '''
        Retorna la cantidad de días que faltan hasta fin de año de la fecha pasada por parámetros.
    '''
    total_dias_anio = sum(MESES_DIAS)
    if es_bisiesto(y):
        total_dias_anio+= 1
    return total_dias_anio - contador_dias(m - 1 , y) + d

def dias_transcurridos(d, m, y):
    ''''
        Retorna la cantidad de días transcurridos hasta la fecha pasada por parámetros.
    '''
    return contador_dias(m, y) + d

def dias_entre_fechas(d1, m1, y1, d2, m2, y2):
    '''
        Valida cuántos días transcurrieron entre las fechas pasadas por parámetros.
    '''
    df = dias_hasta_fin_de_anio(d1, m1, y1)
    dt = dias_transcurridos(d2, m2, y2)
    return df + dt

#=====================================
def contar_dias_hasta_fecha(m, y):
    '''
        Dado un mes y año determinado calcula la cantidad de días que hay desde el primero de Enero hasta esa fecha.
    '''
    if m < 1 or m > 12:
       return print('El valor del mes tiene que estar entre 1 y 12')
       
    if y < 1:
        return print('El valor del año tiene que ser mayor a 1')

    return print(f'La cantidad de días para la fecha {m} / {y} es de {contador_dias(m, y)} días')

def valida_fecha(d, m, y):
    '''
        Evalúa si la fecha ingredasa es válida.
    '''
    if  not evalua_fecha(d, m, y):
        return print('Fecha invalida!')
    print('Fecha válida')    
        
def falta_fin_de_mes(d ,m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha invalida!')
    print(f'Faltan {dias_hasta_fin_de_mes(d, m, y)} días para fin de mes')

def falta_fin_de_anio(d ,m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha invalida!')
    print(f'Desde {d}/{m}/{y} Para fin de año faltan {dias_hasta_fin_de_anio(d, m, y)} días')

def dias_transcurridos_hasta_fecha(d, m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha inválida')
    print(f'Hasta el {d}/{m}/{y} transcurrieron {contador_dias(m - 1, y) + d} días')

def días_entre_fechas(d1, m1, y1, d2, m2, y2):
    '''
        Determina cuántos días transcurrieron entre las fechas.
    '''
    if not evalua_fecha(d1, m1, y1):
        return print('Fecha inválida')
    if not evalua_fecha(d2, m2, y2):
        return print('Fecha inválida')

    result  = dias_hasta_fin_de_anio(d1, m1, y1) + contador_dias(m2 - 1, y2) + d2 
    print(f'Entre las fechas transcurrieron: {result} días')
