#tp4ej2.py
def suma_lenta(numero, otro_numero):
    '''
    esta funcion hace una suma pero no como suma directa sino de a 1 unidad por vez
    '''
    aux = numero
    for i in range(0, otro_numero):
        aux += 1
    return aux
