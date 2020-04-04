'''
Consigna:
    Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el programa le debe decir a qué signo corresponde.

Pre-requisitos:
    - Los días deben estar en 1 y 31
    - Los meses deben estar en 1 y 12
'''

def signo_horoscopo(d,m):
    clave = int(str(m) + '{:02d}'.format(d))
    if(clave > 320 and clave < 421):
        return 'Aries'
    if(clave > 420 and clave < 521):
        return 'Tauro'
    if(clave > 520 and clave < 622):
        return 'Geminis'
    if(clave > 621 and clave < 724):
        return 'Cancer'
    if(clave > 723 and clave < 823):
        return 'Leo'
    if(clave > 823 and clave < 924):
        return 'Virgo'
    if(clave > 923 and clave < 1023):
        return 'Libra'
    if(clave > 1022 and clave < 1123):
        return 'Escorpio'
    if(clave > 1122 and clave < 1222):
        return 'Sagitario'
    if(clave > 1221 and clave < 121):
        return 'Capricornio'
    if(clave > 120 and clave < 220):
        return 'Acuario'
    return 'Piscis'


d = int(input("Ingrese el día de su cumpleaños: "))
m = int(input("Ingrese el mes de su cumpleaños: "))
print('Para el día {} del mes {} el signo es: {}'.format(d, m ,signo_horoscopo(d, m)))