# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 21/7/2025 
# Título de la actividad: for in 
# ------------------------------------------

print("Ejercicio 1")
mat=str(input("Ingrese una materia: "))
cant = 0
for i in mat:
    print(mat[cant])
    cant = cant + 1
print("tiene", cant) 

print("Ejercicio 2")
contiene_digito = False
cad=input("Ingrese una cadena de caracteres: ")
for i in cad:
    if "0" <= i <= "9":
        contiene_digito = True
if contiene_digito: 
    print("Contiene digito")
else:
    print("No contiene digito")

print("Ejercicio 3")
nom=str(input("Ingrese su nombre: "))
cont = 0 
for cant in range(14):
    print(nom)