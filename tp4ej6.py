from tp4ej1 import ingrese_numero
#tp4ej6.py
def minimo(lista):
    '''
    devuelve el minimo de una lista de elementos enteros y/o punto flotante
    '''
    min_aux = list_aux[0]
    for i in range(1, len(lista)):
        if(min_aux > lista[i]):
            min_aux = lista[i]
    return min_aux
    
def maximo(lista):
    '''
    devuelve el maximo de una lista de elementos enteros y/o punto flotante
    '''
    max_aux = lista[0]
    for i in range(1, len(lista)):
        if(max_aux < lista[i]):
            max_aux = lista[i]
    return max_aux    


def prueba():
    lista = []
    for i in range(0,5):#cota superior elegida de forma arbitraria
        lista.append(ingrese_numero(f"ingrese el elemento {i+1} de la lista"))
        
    min = minimo(lista)
    max = maximo(lista)
    
    print(lista)
    print(f"el minimo de la lista es {min}")
    print(f"el minimo de la lista es {max}")
    
    

if __name__ == "__main__":
    prueba()
