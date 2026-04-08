'''
    2. Implementar la función merge en forma recursiva. 
    La función recibe dos listas ordenadas y devuelve una nueva lista con los elementos intercalados ordenadamente.
'''

listaAux = []

def merge(listaA, listaB):
    '''' La función recibe dos lista ordenadas y devuelve una nueva con los elementos ordenados de ambas. Ambas listas tienen el mismo tamaño'''
    
    indexA = 0
    indexB = 0

    while len(listaA) > indexA and len(listaB) > indexB:
        if listaA[indexA] < listaB[indexB]:
            listaAux.append(listaA[indexA])
            indexA+=1

        else:
            listaAux.append(listaB[indexB])
            indexB+=1
    
    if indexA < len(listaA):
        listaAux.extend(listaA)
    
    if indexB < len(listaB):
        listaAux.extend(listaB)
    
    return listaAux


#SIN TERMINAR!