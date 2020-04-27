'''
Consgina:
Ciclos definidos
    a) Escribir un ciclo definido para imprimir por pantalla todos los números entre 10 y 20.
    b) Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as.
    c) Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus cinco mejores amigos/as, y los salude.
    d) Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus seis mejores amigos/as, y los salude.
    e) Escribir un programa que use un ciclo definido con rango numérico, que averigue a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.
'''

def ciclo_definido():
    '''
        Función que imprime lo números entre 10 y 20
    '''
    for x in range(10, 21):
        print(x)
    
def saludo_amigos():
    '''
        Función que imprime el saludo a los 5 mejores amigos/as
    '''
    for f in range(1,6):
        print('Hola mejor amigo/a {}'.format(f))

def saludo_amigos_lista(total):
    '''
        Función que le pide a usuario una lista de nombres 
    '''
    amigos = []
    for a in range(total):
        amigos.append(input('Ingrese el nombre de su mejor amigo/a:'))
    
    for amigo in amigos:
        print('Hola {} !'.format(amigo))

def main():
    '''
        Función principal que invoca a las demás.
    '''
    total_amigos = int(input('A cuantos mejores amigos queres saludar?:'))
    saludo_amigos_lista(total_amigos)

main()