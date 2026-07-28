# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 2/6/2025 
# Título de la actividad: bucle while
# ------------------------------------------ 
print("Ejercicio 1")
nom = input("Ingrese un nombre: ")
res = 0
while res < 15:
    print(nom)
    res = res + 1

print("Ejercicio 2")
mul = 0
while mul < 150:
    mul = mul + 6
    print(mul)

print("Ejercicio 3") 
ini = int ( input ("Ingrese un valor incial: "))
fin = int ( input ("Ingrese un valor final: "))
while ini < fin:
    print(ini)
    ini = ini + 1
    print(ini)

print("Ejercicio 4")
num=0
num_sum=0
while num != 5050:
    num_sum= num_sum+1
    num = num+num_sum
    print(num)

print("Ejercicio 5")
num=0
con=0
while num < 50:
    num= num +2
    con = con+1
    print(num)
print("Hay ", con, "numeros par")