'''
Consigna:
    Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y mues-
    tre por pantalla la duración total en horas, minutos y segundos.

'''

def a_segundos(horas, minutos, segundos):
    '''
        Transforma en segundos una medida de tiempo expresada en horas, minutos y segundos
    '''
    return 3600 * horas + 60 * minutos + segundos

def a_hms(segundos):
    '''Dada una duración entera en segundos se la convierte a horas, minutos y segundos'''
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60

    return h, m, s

def proceso_intervalos(h1, m1, s1, h2, m2, s2):
    ht, mt, st =  a_hms(a_segundos(h1, m1, s1) + a_segundos(h2, m2, s2))
    print('Duracion:', ht, ' horas | ', mt, ' minutos | ', st, ' segundos')

h1 = int(input("¿Cuántas horas?: "))
m1 = int(input("¿Cuántos minutos?: "))
s1 = int(input("¿Cuántos segundos?: "))

h2 = int(input("¿Cuántas horas?: "))
m2 = int(input("¿Cuántos minutos?: "))
s2 = int(input("¿Cuántos segundos?: "))

proceso_intervalos(h1, m1, s1, h2, m2, s2)
