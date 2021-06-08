from tp4ej1 import ingrese_numero
from tp4ej9 import es_impar

#tp4ej10.py
def factores_primos(numero):
    '''
    devuelve un tuple con los factores de un numero entero positivo y cuantas veces aparecen
    '''
    #verifica que aunque ingrese un numero flotante o negativo se convertirá en un entero positivo
    numero = int(numero)
    if(numero < 0):
        numero = -numero
    
    #creo un tuple vacio y lo convierto en una lista para poder agregarle elementos
    tuple_de_factores = ("")
    lista_auxiliar = list(tuple_de_factores)
    
    #si ingresé el 0 ó el 1, devuelvo un tuple notificando que no fue considerado el numero
    if(numero == 0 or numero == 1):
        lista_auxiliar.append("ingresaste el numero "+str(numero)+" no lo puedo considerar para este programa.")
        return tuple(lista_auxiliar)
    
    #creo una copia del numero para el bucle y un indice para la lista de factores
    tope = numero
    j=0
    for i in range(tope,1,-1):
        #siempre reseteo el indice "k" a 1, el cual indica la cantidad del mismo factor presentes en el numero
        k=1
        #solo si lo divide y ademas es primo se lo considera un factor
        while(numero%i == 0 and es_primo(i)):
            numero = numero//i
            #solo si es la primera vez que aparece lo agrego a la lista, sino solo le modifico el valor de "k"
            if(k==1):
                lista_auxiliar.append(str(i)+" aparece "+str(k)+" veces.")
                j+=1
            lista_auxiliar[j-1] = str(i)+" aparece "+str(k)+" veces."
            k+=1
    #vuelvo la lista un tuple y lo retorno
    tuple_de_factores=tuple(lista_auxiliar)
    return  tuple_de_factores



def prueba():
    numero = ingrese_numero()
    resultados = factores_primos(numero)
    print(resultados)
    
    

if __name__ == "__main__":
    prueba()


