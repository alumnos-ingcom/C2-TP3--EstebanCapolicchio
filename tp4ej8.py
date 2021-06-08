from tp4ej1 import ingrese_numero

#tp4ej8
def ordenar_mayor_a_menor(uno, dos, tres):
    '''
    devuelve una lista con los tres elementos ordenada de mayor a menor
    '''
    lista_aux = [uno, dos, tres]
    for i in range(0, len(lista_aux)-1):
        if(lista_aux[i] < lista_aux[i+1]):
            #cambia elementos de lugar
            elem_aux = lista_aux[i+1]
            lista_aux[i+1] = lista_aux[i]
            lista_aux[i] = elem_aux
    return lista_aux
    
def ordenar_menor_a_mayor(uno, dos, tres):
    '''
    devuelve una lista con los tres elementos ordenada de menor a mayor
    '''
    lista_aux = [uno, dos, tres]
    for i in range(0, len(lista_aux)-1):
        if(lista_aux[i] > lista_aux[i+1]):
            #cambia elementos de lugar
            elem_aux = lista_aux[i+1]
            lista_aux[i+1] = lista_aux[i]
            lista_aux[i] = elem_aux
    return lista_aux 

def entitular(numero1, mensaje):
    borde = '*' * numero1 + ' '
    print(borde + mensaje + borde)

def prueba():
    num1 = ingrese_numero("ingrese el primer numero")
    num2 = ingrese_numero("ingrese el segundo numero")
    num3 = ingrese_numero("ingrese el tercer numero")
    
    entitular(7, "Ordenada de Menor a Mayor")
    orden_ascendente = ordenar_menor_a_mayor(num1,num2,num3)
    print(f"{orden_ascendente}")
    print('*' * 42) #el sentido de la vida, el universo y todo lo demas es 42
    
    entitular(7, "Ordenada de Mayor a Menor")
    orden_descendente = ordenar_mayor_a_menor(num1,num2,num3)
    print(f"{orden_descendente}")
    print('*' * 42)
    
    
if __name__ == "__main__":
    prueba()
