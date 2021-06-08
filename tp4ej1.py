#tp4ej1.py
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

class FueraDeLimite(Exception):
    """Esta es la Excepcion para el ingreso incorrecto por salirse de los limites"""
    pass

def ingrese_numero(mensaje):
    '''
    -mensaje es un string el cual se concatenara con ": "
    para luego pedir un numero al usuario.
    -en caso de no ingresar un numero se levanta la siguiente excepcion:
        IngresoIncorrecto(Exception)
    '''
    ingresado = input(mensaje+":")
    try:
        entero = int(ingresado)
        return entero
    except ValueError as err:
        raise IngresoIncorrecto("el input no era un numero")

def ingrese_entero_reintento(mensaje, intentos=3):#por defecto son 3 intentos
    '''
    -mensaje es un string el cual se utiliza en la funcion:
        ingrese_numero(mensaje)
    -intentos es un integer con valor por defecto igual a 3 el cual
    al llegar a 0 sin haber ingresado correctamente un numero
    levanta la siguiente excepcion:
        IngresoIncorrecto(Exception)
    '''
    i = intentos
    while i > 0:
        try:
            entero = ingrese_numero(mensaje)
            return entero
        except IngresoIncorrecto:
            i -=1
            print(f"quedan {i} intentos")
            
    raise IngresoIncorrecto("el input no era un numero")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    '''
    -mensaje es un string el cual se utiliza en la funcion:
        ingrese_numero(mensaje)
    -valor_minimo es un integer con valor por defecto igual a 0
    -valor_minimo es un integer con valor por defecto igual a 10
    - si el input no es un numero levanta la siguiente excepcion:
        IngresoIncorrecto(Exception)
    - si el input es un numero pero esta fuera de las cotas asignadas levanta la siguiente excepcion:
        FueraDeLimite(Exception)
    '''
    try:
        entero = ingrese_numero(mensaje)
        if(valor_minimo < entero and entero < valor_maximo):
            return entero
        else:
            raise FueraDeLimite("el input esta fuera de los limites establecidos")
    except IngresoIncorrecto:
        raise IngresoIncorrecto("el input no era un numero")
        
        
def prueba():
    mensaje="Ingrese un numero por favor"
    print("***************ingreso de numero entero*****************")
    num1 = ingrese_numero(mensaje)
    print(num1)
    print("********************************************************")
    print("*********ingreso de numero entero con intentos**********")
        respuesta = input("quiere elegir usted cuantos intentos tiene? (Si | No) : ").lower()
        if(respuesta == "si"):
            intentos=ingrese_numero(mensaje)
            num2a = ingrese_entero_reintento(mensaje,intentos)
            print(num2a)
        elif(respuesta == "no"):
            num2b = ingrese_entero_reintento(mensaje)#por defecto serán 3 intentos
            print(num2b)
        else:
            print("a ver... solo tenias que responder 'si' o 'no'...")
            print("por ende asumiré que no te importa... pasemos a la siguiente prueba")
    print("********************************************************")
    print("****ingreso de numero entero entre ciertos valores******")
    num3 = ingreso_entero_restringido(mensaje)#por defecto será entre 0 y 10
    print(num3)
    print("********************************************************")

if __name__ == "__main__":
    prueba()
