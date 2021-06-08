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
    valor_en_Farenheit = ingrese_numero("ingrese numero para pasarlo de Farenheit a Celcius")
    valor_en_Celcius = ingrese_numero("ingrese numero para pasarlo de Celcius a Farenheit")
    valor_en_Farenheit_convertido_en_Celcius = convertir_a_centigrados(valor_en_Farenheit)
    valor_en_Celcius_convertido_en_Farenheit = convertir_a_fahrenheit(valor_en_Celcius)
    print(f"|    Farenheit: {valor_en_Farenheit} -->  Celcius: {valor_en_Farenheit_convertido_en_Celcius}    |")
    print(f"|    Celcius: {valor_en_Celcius} -->  Farenheit: {valor_en_Celcius_convertido_en_Farenheit}    |")
    
    
    
if __name__ == "__main__":
    prueba()
