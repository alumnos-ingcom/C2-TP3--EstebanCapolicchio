#tp4ej4.py
def compara(numero, otro_numero):
    '''
    compara dos numero A y B:
    retorna -1 si A < B
    retorna  1 si A > B
    retorna  0 si A == B
    '''
    if(numero < otro_numero):
        return -1
    elif(numero > otro_numero):
        return 1
    else:
        return 0
    
def compara_eficiente(numero, otro_numero):
    '''
    compara dos numero A y B:
    retorna "menor a 0" si A < B
    retorna "mayor a 0" si A > B
    retorna "0" si A == B
    '''
    return numero - otro_numero
