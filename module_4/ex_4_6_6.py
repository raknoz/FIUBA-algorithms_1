'''
Consigna:
    Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
    si recibe '3' debe devolver 'miércoles' , si recibe '9' debe devolver 'martes' .
'''
DIAS_SEMANA = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado' ]

def dia_de_la_semana(num):
    '''
        Retorna el día de la semana que cae el número pasado por parámetro.
    '''
    if(num < 1 or num > 366):
        print('Error, no es un día válido del año!')
    print('El número {} cae el día: {}'.format(num, DIAS_SEMANA[num % 7]))