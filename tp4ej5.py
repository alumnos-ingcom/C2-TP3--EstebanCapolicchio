#tp4ej5.py
def signo(numero):
    '''
    devuelve si el numero es "mayor a 0", "menor a 0" ó "igual a 0"
    '''
    if(numero < 0):
        return "numero negativo"
    elif(numero > 0):
        return "numero positivo"
    else:
        return "es el cero"
