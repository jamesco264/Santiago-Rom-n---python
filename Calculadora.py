# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 25/8/2025 
# Título de la actividad: Calculadora
# ------------------------------------------

def suma(): 
    print("Ingrese dos valores")
    a = int(input())
    b = int(input())
    resultado = a + b
    print("El resultado es: ", resultado)

def resta():
    print("Ingrese dos valores")
    a = int(input())
    b = int(input())
    resultado = a - b 
    print("El resultado es: ", resultado)

def mult():
    print("Ingrese dos valores")
    a = int(input())
    b = int(input())
    resultado = a * b 
    print("El resultado es: ", resultado)

def div():
    print("Ingrese dos valores")
    a = int(input())
    b = int(input())
    resultado = a / b 
    if resultado == 0:
        print("No se puede dividir entre cero")
    else:
     print("El resultado es: ", resultado)

def menu():
    print("1-Suma")
    print("2-Resta")
    print("3-Multilicacion")
    print("4-Division")
    print("5-Salir")

ope=0
print("***********************************")
print("***********Calculadora*************")
print("***********************************")
print("1-Suma")
print("2-Resta")
print("3-Multilicacion")
print("4-Division")
print("5-Menu")
print("6-Salir")

while ope != 6:

    ope=input("Ingrese la operacion que desea realizar: ")
    if ope == '1':
        suma()
    elif ope == '2':
        resta()
    elif ope == '3':
        mult()
    elif ope == '4':
        div()
    elif ope == '5':
        menu()
    elif ope == '6':
        break
    else:
        print("no esta dentro de las opciones")