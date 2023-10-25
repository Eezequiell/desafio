import masa
import temperatura
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen =="celsius" and unidad_destino =="fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    else:
        return None
    
def convertir_masa