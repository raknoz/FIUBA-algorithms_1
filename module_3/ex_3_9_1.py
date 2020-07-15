'''
Consigna:
    Escribir dos funciones que permitan calcular:
        a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
        b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
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
