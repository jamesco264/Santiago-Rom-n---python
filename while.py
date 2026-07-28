# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 21/7/2025 
# Título de la actividad: bucle while
# ------------------------------------------ 
print ("Ejercicio 1")
pal = str(input("Ingrese una frase: "))
cont = 0 
while cont < 10 :
    print(pal)
    cont = cont + 1

print("Ejercicio 2")
cont = 1
while cont < 101 :
    print(cont)
    cont = cont + 1

print("Ejercicio 3")
num = int (input("Ingrese un numero: "))
while num > 0 :
    print(num)
    num = num - 1

print("Ejercicio 4")
cont = 5
while cont!=105:
    print(cont)
    cont = cont + 5

print("Ejercicio 5")
cont = 0
num = 0
while cont < 51:
    num = num + cont
    cont = cont + 1 
print(num)

print("Ejercicio 6")
numI = int(input("Ingrese el valor inical : "))
numF = int(input("ingrese un valor final : "))
numF = numF + 2
while numI != numF:
    if numI > numF:
        res = numI % 2
        print(numI)
        numI = numI - 2
    else:
        res = numI % 2
        print(numI)
        numI = numI + 2

print("Ejercicio 7")
cont = 1
print("Para finalizar ingrese un 0")
while cont == 1:
    sum=int(input("ingrese los valores que quiere sumar: "))

print("Ejercicio 8)")
num3=str("hin")
s=str(input("ingrese la contraseña: "))
while num3!=s:
    s=str(input("la contraseña es incorrecta, intente nuevamente: "))
print("La contraseña es correcta")

print("Ejercicio 9)")
p=str(input("Ingrese una palabra: "))
v=0
while p:
    print(p[v])
    v=v+1
    if v==len(p):
        break

print("Ejercicio 10)")
num4=0
s1=int(input("ingrese un numero: "))
while num4<s1*10:
    num4=s1+num4
    print (num4)