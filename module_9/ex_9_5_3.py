'''
Consigna:
    Continuación de la agenda.
    Escribir un programa que vaya solicitando al usuario que ingrese nombres.
    a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
    el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
    b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
    El usuario puede utilizar la cadena ”*”, para salir del programa.
'''

def pide_nombre():
    return input('Ingrese un nombre (* para salir): ')

def pide_numero_tel(n):
    return input(f'Ingrese el número de teléfono para {n}: ')

def cambia_numero_tel(n, t_old):
    return input(f'Ingrese el número de teléfono para {n} (actual {t_old}): ')

def valida_cambio_tel(n, t_old):
    opc = input(f'Desea actualizar el número de teléfono {t_old} de {n} (S/N): ')
    while opc.upper() not in ('S', 'N'):
        opc = input(f'Desea actualizar el número de teléfono {t_old} de {n} (S/N): ')
    return True if opc.upper() == 'S' else False 

def completa_agenda():
    agenda = {}
    n = pide_nombre()
    #Flag que avisa si hay para agregar un teléfino.
    flag = False
    while n != '*':
        if n in agenda:
            #Si existe en la agenda pregunto si lo desea actualizar.
            if valida_cambio_tel(n, agenda.get(n)):
                t = cambia_numero_tel(n,  agenda.get(n))
                flag = True
        else:
            t = pide_numero_tel(n)
            flag = True

        #Si se cambió el número o se agregó uno nuevo, lo guardo. 
        if flag: 
            agenda[n] = t
        
        flag = False
        n = pide_nombre()
    return agenda

print(completa_agenda())


