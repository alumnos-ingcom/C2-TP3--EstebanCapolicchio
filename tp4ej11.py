#tp4ej11.py
def es_palindromo(texto):
    '''
    devuelve True si es texto es palindromo, False sino.
    con texto palindromo se refiere a un texto cuya lectura es igual de izquierda a derecha que de derecha a izquierda
    '''
    texto = str(texto)
    longitud = len(texto)
    mitad_longitud = int(longitud/2)
    for i in range(0, mitad_longitud):
        if(texto[i] != texto[longitud -1 - i]):
            return False
    return True


def prueba():
    texto = str(input("ingrese texto para analizar si es o no un palindromo"))
    if(es_palindromo(texto)):
        print(f"{texto} es un palindromo")
    else:
        print(f"{texto} NO es un palindromo")

if __name__ == "__main__":
    prueba()
