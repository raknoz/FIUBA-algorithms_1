from ex_3_9_1 import a_segundos, a_hms
'''
Consigna:
    Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y mues-
    tre por pantalla la duración total en horas, minutos y segundos.
'''   

def pedir_horario():
    h = int(input("¿Cuántas horas?: "))
    m = int(input("¿Cuántos minutos?: "))
    s = int(input("¿Cuántos segundos?: "))

    return h, m, s

def main():
    '''
        Función principal que se encargar de pedirle los datos al usuario.
    '''
    h1, m1, s1 = pedir_horario()
    h2, m2, s2 = pedir_horario()
    
    ht, mt, st =  a_hms(a_segundos(h1, m1, s1) + a_segundos(h2, m2, s2))
    print('Duracion:', ht, ' horas | ', mt, ' minutos | ', st, ' segundos')

main()
