def ingrese_numero():
    ingresado = input("ingrese numero entero: #")
    try:
        entero = int(ingresado)
        return entero
    except ValueError as err:
        print("El numero ingresado no era entero")
        ##raise IngresoIncorrecto("No era un numero") from err ####<-----------------------------------------------------------------------

def ingrese_entero_reintento(intentos):
    i = 0
    while i < intentos:
        entero = ingrese_numero()
        print(entero)
        i +=1
