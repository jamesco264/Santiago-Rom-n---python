# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 9/9/2025 
# Título de la actividad: Calculadora parametros 
# ------------------------------------------

def resta(a,b):
    print(a - b)

def suma(a,b):
    print(a + b)

def mult(a,b):
    print(a * b)

def div(a,b):
    print(a / b)

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
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor"))
    if ope == '1':
        suma(num1,num2)
    elif ope == '2':
        resta(num1,num2)
    elif ope == '3':
        mult(num1,num2)
    elif ope == '4':
        div(num1,num2)
    elif ope == '5':
        menu()
    elif ope == '6':
        break
    else:
        print("no esta dentro de las opciones")