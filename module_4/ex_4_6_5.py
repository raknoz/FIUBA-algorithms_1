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
DIC_MESES_DIAS = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def es_bisiesto(y):
    '''
        Función que retorna True o False si un año es o no bisiesto.
    '''
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        
def contador_dias(m, y):
    '''
        Función que devuelve el total de días transcurridos hasta un mes determinado.
    '''
    total_dias = 0  
    for x in range(1, m + 1):
        total_dias+= DIC_MESES_DIAS.get(x)

    if es_bisiesto(y) and m > 1:
        total_dias+=1
    return total_dias

def evalua_fecha(d, m, y):
    '''
        Comprueba si una fecha pasada por parámetro es vádida.
    '''
    if  (d < 1 or d > 31) or (m < 1 or m > 12) or (y < 1):
        return False
    elif(m == 2 and not es_bisiesto(y) and d > 28):
        return False
    elif(m != 2 and d > DIC_MESES_DIAS.get(m)):
        return False
    return True

def dias_hasta_fin_de_mes(d, m, y):
    '''
        Retorna la cantidad de días que faltan hasta fin de mes de la fecha pasada por parámetros.
    '''
    dias_total = DIC_MESES_DIAS.get(m)
    if (m == 2 and es_bisiesto(y)):
        dias_total +=1
    return dias_total - d

def dias_hasta_fin_de_anio(d, m, y):
    '''
        Retorna la cantidad de días que faltan hasta fin de año de la fecha pasada por parámetros.
    '''
    total_dias_anio = sum(DIC_MESES_DIAS.values())
    if(es_bisiesto(y)):
        total_dias_anio+= 1
    return total_dias_anio - (contador_dias(m - 1 , y) + d)

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
def valida_bisiesto(y):
    '''
        Recibe un año y valida si es bisiesto o no.
    '''
    if es_bisiesto(y):
        print('El año {} es biciesto'.format(y))
    else:
        print('El año {} no es biciesto'.format(y))

def contar_dias_hasta_fecha(m, y):
    '''
        Dado un mes y año determinado calcula la cantidad de días que hay desde el primero de Enero hasta esa fecha.
    '''
    if m < 1 or m > 12:
       return print('El valor del mes tiene que estar entre 1 y 12')
       
    if y < 1:
        return print('El valor del año tiene que ser mayor a 1')

    return print('La cantidad de días para la fecha {} / {} es de {} días'.format(m, y, contador_dias(m, y)))

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
    print('Faltan {} días para fin de mes'.format(dias_hasta_fin_de_mes(d, m, y)))

def falta_fin_de_anio(d ,m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha invalida!')
    print('Desde {}/{}/{} Para fin de año faltan {} días'.format(d, m, y, dias_hasta_fin_de_anio(d, m, y)))

def dias_transcurridos_hasta_fecha(d, m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha inválida')
    print('Hasta el {}/{}/{} transcurrieron {} días'.format(d, m, y, contador_dias(m - 1, y) + d))

def días_entre_fechas(d1, m1, y1, d2, m2, y2):
    '''
        Determina cuántos días transcurrieron entre las fechas.
    '''
    if not evalua_fecha(d1, m1, y1):
        return print('Fecha inválida')
    if not evalua_fecha(d2, m2, y2):
        return print('Fecha inválida')

    result  = dias_hasta_fin_de_anio(d1, m1, y1) + contador_dias(m2 - 1, y2) + d2 
    print('Entre las fechas transcurrieron: {} días'.format(result))
