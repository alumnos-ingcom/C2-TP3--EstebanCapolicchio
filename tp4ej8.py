def ordenar_mayor_a_menor(uno, dos, tres):
    '''
    devuelve una lista con los tres elementos ordenada de mayor a menor
    '''
    lista_aux = [uno, dos, tres]
    for i in range(0, len(lista_aux)-1):
        if(lista_aux[i] < lista_aux[i+1]):
            #cambia elementos de lugar
            elem_aux = lista_aux[i+1]
            lista_aux[i+1] = lista_aux[i]
            lista_aux[i] = elem_aux
    return lista_aux
    
def ordenar_menor_a_mayor(uno, dos, tres):
    '''
    devuelve una lista con los tres elementos ordenada de menor a mayor
    '''
    lista_aux = [uno, dos, tres]
    for i in range(0, len(lista_aux)-1):
        if(lista_aux[i] > lista_aux[i+1]):
            #cambia elementos de lugar
            elem_aux = lista_aux[i+1]
            lista_aux[i+1] = lista_aux[i]
            lista_aux[i] = elem_aux
    return lista_aux 
