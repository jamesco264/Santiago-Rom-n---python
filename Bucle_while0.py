# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 2/6/2025 
# Título de la actividad: bucle while
# ------------------------------------------ 
edad=0
while edad<18:
    print(edad)
    edad=edad+1

print("prueba 2")
nombre = "ale"
while (nombre != "Mateo"):
    print(nombre)
    nombre = input("Ingrese un nombre: ")

print("prueba 3")

num=1
while num != 1:
    entrada=input("ingrese una palabra")
    if entrada == "Finalizar":
        break
    else:
        print(entrada)