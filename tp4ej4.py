from tp4ej1 import ingrese_numero

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


def prueba():
    num1 = ingrese_numero("primer numero")
    num2 = ingrese_numero("segundo numero")
    rta = compara(num1, num2)
    if(rta < 0):
        print("el primer numero es menor al segundo")
    elif(rta > 0):
        print("el primer numero es mayor al segundo")
    else:
        print("el primer numero es igual al segundo")

if __name__ == "__main__":
    prueba()

