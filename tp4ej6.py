#tp4ej6.py
def minimo(lista):
    '''
    devuelve el minimo de una lista de elementos enteros y/o punto flotante
    '''
    min_aux = list_aux[0]
    for i in range(1, len(lista)):
        if(min_aux > lista[i]):
            min_aux = lista[i]
    return min_aux
    
def maximo(lista):
    '''
    devuelve el maximo de una lista de elementos enteros y/o punto flotante
    '''
    max_aux = lista[0]
    for i in range(1, len(lista)):
        if(max_aux < lista[i]):
            max_aux = lista[i]
    return max_aux    
