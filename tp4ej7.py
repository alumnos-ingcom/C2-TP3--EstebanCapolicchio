from tp4ej1 import ingrese_numero
#tp4ej7.py    
def division_lenta(dividendo, divisor):
    '''
    realiza una division entre dos numeros enteros (tambien acepta numeros punto flotante) sean positivos o negativos
    devuelve una lista que contiene el Cociente y el Resto de la division
    si se trata de dividir por 0 alza error ZeroDivisionError
    '''
    #nunca se puede dividir por 0...
    if(divisor == 0):
        raise ZeroDivisionError
    
    cociente = 0
    resto = 0
    # cualquier numero entero se puede escribir como:
    # A = B * C + R
    # donde:
    # dividendo == A
    # divisor   == B
    # cociente  == C
    # resto     == R
    
    flag_A_negativo = 0
    flag_B_negativo = 0
    #esto nos servirá para hacer mas facil la "division" y para asignar los signos al final
    if(dividendo < 0):
        dividendo = -dividendo
        flag_A_negativo = 1
    if(divisor < 0):
        divisor = -divisor
        flag_B_negativo = 1

    while (dividendo - divisor) >= 0:
        dividendo -= divisor
        cociente += 1
        resto = dividendo
    #¿quien se lleva los signos?
    # si A (+) y B (+) --> C (+) y R (+) {ejemplo: 11 = 5 * 2 + 1}
    # si A (+) y B (-) --> C (-) y R (+) {ejemplo: 11 = -5 * -2 + 1}
    # si A (-) y B (+) --> C (-) y R (-) {ejemplo: -11 = 5 * -2 - 1}
    # si A (-) y B (-) --> C (+) y R (-) {ejemplo: -11 = -5 * 2 - 1}
    resto = dividendo * (-1)**flag_A_negativo
    cociente = cociente * (-1)**flag_A_negativo * (-1)**flag_B_negativo
    resultados = (cociente, resto)
    return resultados


def prueba():
    dividendo = ingrese_numero()
    divisor = ingrese_numero()
    resultados = division_lenta(dividendo, divisor)
    print(f"[Cociente, Resto] = {resultados}")
    

if __name__ == "__main__":
    prueba()



