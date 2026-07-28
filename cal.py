# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 13/10/2025 
# Título de la actividad: Calculadora geometrica
# ------------------------------------------

import math as m # Importamos la biblioteca matemática

# Función para el área del círculo
def area_circulo(radio):
    # COMPLETAR: verificar si el radio es positivo y calcular el área
    if r > 0:
        return m.pi * radio ** 2
        # Fórmula: π * radio^2
    else:
        return print("error")
    

# Función para el área del rectángulo
def area_rectangulo(base, altura):
    # COMPLETAR: verificar que base y altura sean positivas y calcular el área
    b = base
    a = altura
    if b > 0 and a > 0:
        return b * a
    else:
        return print("error")



# Función para el área del triángulo rectángulo
def area_triangulo_rectangulo(cateto1, cateto2):
    # COMPLETAR: verificar que los catetos sean positivos y calcular el área
    c1 = cateto1
    c2 = cateto2
    if c1 > 0 and c2 > 0:
        return (c1 * c2)/2
    else:
        return print("error")

# Función para calcular la hipotenusa
def hipotenusa_triangulo(cateto1, cateto2):
    # COMPLETAR: verificar que los catetos sean positivos y calcular la hipotenusa
    if c1 > 0 and c2 > 0:
        return m.sqrt(c1**2+c2**2)
    else:
        return print("error")
    # Fórmula: sqrt(cateto1^2 + cateto2^2)


# Programa principal
print("--- Calculadora de Geometría Plana ---")

# --- Círculo ---
try:
    r = float(input("\n[Círculo] Ingresa el radio: "))
    resultado_circulo = area_circulo(r)
    if isinstance(resultado_circulo, float):
        print(f"-> Área del círculo: {resultado_circulo:.2f}")
    else:
        print(f"-> {resultado_circulo}")
except ValueError:
    print("Error: Ingresa un valor numérico válido para el radio.")

# --- Rectángulo ---
try:
    b = float(input("\n[Rectángulo] Ingresa la base: "))
    a = float(input("[Rectángulo] Ingresa la altura: "))
    resultado_rectangulo = area_rectangulo(b, a)
    if isinstance(resultado_rectangulo, float):
        print(f"-> Área del rectángulo: {resultado_rectangulo:.2f}")
    else:
        print(f"-> {resultado_rectangulo}")
except ValueError:
    print("Error: Ingresa valores numéricos válidos para base y altura.")

# --- Triángulo Rectángulo ---
try:
    c1 = float(input("\n[Triángulo Rectángulo] Ingresa el Cateto 1: "))
    c2 = float(input("[Triángulo Rectángulo] Ingresa el Cateto 2: "))
    
    # Área
    resultado_area_triangulo = area_triangulo_rectangulo(c1, c2)
    if isinstance(resultado_area_triangulo, float):
        print(f"-> Área del triángulo: {resultado_area_triangulo:.2f}")
    else:
        print(f"-> {resultado_area_triangulo}")
    
    # Hipotenusa
    resultado_hipotenusa = hipotenusa_triangulo(c1, c2)
    if isinstance(resultado_hipotenusa, float):
        print(f"-> Hipotenusa: {resultado_hipotenusa:.2f}")
    else:
        # Esto solo ocurrirá si el chequeo de error se activa en la función
        print(f"-> Error al calcular hipotenusa: {resultado_hipotenusa}") 
except ValueError:
    print("Error: Ingresa valores numéricos válidos para los catetos.")