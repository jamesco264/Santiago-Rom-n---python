# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 6/10/2025 
# Título de la actividad: Calculadora estadisticas
# ------------------------------------------


def calcular_suma(lista):
    resultado = 0 
    for i in numeros:
        resultado += i
    return resultado

def calcular_promedio(lista):
    cont = 0 
    res = 0 
    for i in numeros:
        cont = cont + 1
        res += i
    res = res / cont
    return res
    
def calcular_maximo(lista):
    a = 0
    for i in numeros: 
        if i == 0 or i > a:
            a = i
    return a

def calcular_minimo(lista):
    a = 0
    for i in numeros: 
        if a is 0 or i < a:
            a = i
    return a  
   

entrada = input("Ingresá números separados por espacio: ")
numeros = [int(x) for x in entrada.split()]  # Convierte a lista de enteros


print(calcular_suma(numeros))
print(calcular_promedio(numeros))
print(calcular_maximo(numeros))
print(calcular_minimo(numeros))