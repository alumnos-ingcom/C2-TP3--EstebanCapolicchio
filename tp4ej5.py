from tp4ej1 import ingrese_numero
from tp4ej4 import compara

#tp4ej5.py
def signo(numero):
    '''
    devuelve si el numero es "mayor a 0", "menor a 0" ó "igual a 0" realizando una comparacion con el 0
    '''
    return compara(numero,0)

    
def prueba():
    numero = ingrese_numero()
    signo_numero = signo(numero)
    if(signo_numero < 0):
        print("el numero es negativo (menor a 0)")
    elif(signo_numero > 0):
        print("el numero es positivo (mayor a 0)")
    else:
        print("el numero es igual a 0")

if __name__ == "__main__":
    prueba()
