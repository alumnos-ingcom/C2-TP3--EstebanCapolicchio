from tp4ej1 import ingrese_numero
#tp4ej3.py
def convertir_a_fahrenheit(centigrados):
    '''
    convierte °C -> °F
    '''
    return centigrados * 9/5 + 32
    
def convertir_a_centigrados(fahrenheit):
    '''
    convierte °F -> °C
    '''
    return (fahrenheit - 32) * 5/9

def prueba():
    FaC = ingrese_numero("ingrese numero para pasarlo de Farenheit a Celcius")
    CaF = ingrese_numero("ingrese numero para pasarlo de Celcius a Farenheit")
    convertido_FaC = convertir_a_centigrados(FaC)
    convertido_CaF = convertir_a_fahrenheit(CaF)
    print("|    Farenheit: "+str(FaC)" -->  Celcius: "+str(convertido_FaC)+"    |")
    print("|    Celcius: "+str(CaF)" -->  Farenheit: "+str(convertido_CaF)+"    |")
    
    
    
if __name__ == "__main__":
    prueba()
