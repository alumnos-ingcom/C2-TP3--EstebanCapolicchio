from tp4ej1 import ingrese_numero

#tp4ej2.py
def suma_lenta(numero, otro_numero):
    '''
    esta funcion hace una suma pero no como suma directa sino de a 1 unidad por vez
    '''
    aux = numero
    if(otro_numero >= 0):
        for i in range(0, otro_numero):
            aux += 1
    else:
        for i in range(otro_numero, 0, -1):
            aux -= 1
    return aux


def prueba():
    num1 = ingrese_numero("primer numero")
    num2 = ingrese_numero("segundo numero")
    rta = suma_lenta(num1, num2)
    print("la suma entre"+str(num1)+" y "+str(num2)+" es igual a: "+str(rta))

if __name__ == "__main__":
    prueba()
