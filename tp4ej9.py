#tp4ej9.py    
def es_primo(numero):
    '''
    devuelve True si es un numero primero, False sino.
    con numero primo se refiere a un numero cuyos unicos divisores son 1 y el propio numero
    '''
    for i in range(2,numero):
        if(numero%i == 0):
            return False
    return True
