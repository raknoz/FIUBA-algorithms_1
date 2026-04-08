'''
Consigna:
    Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el programa le debe decir a qué signo corresponde.
'''

signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

def signo_horoscopo(d, m):
    '''
        Función que devuelve el signo del zodíaco de acuerdo al día y mes pasado cómo parametro.
    '''
    m -= 1
    if d > fechas[m]:
        m += 1
    if m == 12:
        mes = 0
    return signo[m]

def main():
    d = int(input("Ingrese el día de su cumpleaños: "))
    m = int(input("Ingrese el mes de su cumpleaños: "))
    print(f'Para el día {d} del mes {m} el signo es: {signo_horoscopo(d, m)}')

main()