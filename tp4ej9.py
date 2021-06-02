from tp4ej1 import ingrese_numero
#tp4ej9.py    
def es_primo(numero):
    '''
    devuelve True si es un numero primero, False sino.
    con numero primo se refiere a un numero cuyos unicos divisores son 1 y el propio numero
    '''
    #para numeros menores a 0 le quitamos el signo
    if(numero < 0):
        numero = -numero
    
    #para el 0 y el 1
    if(numero < 2):
        return False
    
    #para numero mayores a 2
    for i in range(2,numero):
        if(numero%i == 0):
            return False
    return True

def prueba():
    numero = ingrese_numero()
    if(es_primo(numero)):
        print(f"{numero} es un numero primo")
    else:
        print(f"{numero} NO es un numero primo")
    

if __name__ == "__main__":
    prueba()
