# ------------------------------------------
# Autor: Santiago Román
# Fecha: 25/05/2025
# Título de la actividad: Operador in()
# ------------------------------------------
print("Masa", "Fuerza", "Aceleracion")
seleccionado = input("Ingrese lo que quiere calcular: ").lower()

if seleccionado in "masa":
    fuerza = float(input("Ingrese el valor de fuerza: "))
    aceleracion = float(input("Ingrese el valor de aceleracion: "))
    res = fuerza / aceleracion
    print("El valor de masa es: ", res)
elif seleccionado in "fuerza":
    masa = float(input("Ingrese el valor de masa: "))
    aceleracion = float(input("Ingrese el valor de aceleracion: "))
    res = masa * aceleracion
    print("El valor de masa es: ", res)
elif seleccionado in "aceleracion":
    fuerza = float(input("Ingrese el valor de fuerza: "))
    masa = float(input("Ingrese el valor de masa: "))
    res = fuerza / masa
    print("El valor de masa es: ", res)
    


