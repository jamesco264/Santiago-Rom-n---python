# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 15/9/2025 
# Título de la actividad: Calculadora parametros 2
# ------------------------------------------

def resta(a,b):
    return a - b

def suma(a,b):
    return a + b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def menu():
    print("1-Suma")
    print("2-Resta")
    print("3-Multilicacion")
    print("4-Division")
    print("5-Menu")
    print("6-Salir")

ope=0
print("*********************************")
print("***********Calculadora***********")
print("*********************************")
print("1-Suma")
print("2-Resta")
print("3-Multilicacion")
print("4-Division")
print("5-Menu")
print("6-Salir")

while ope != 6:

    ope=input("Ingrese la operacion que desea realizar: ")
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if ope == '1':
        var = suma(num1,num2)
        print(var)
    elif ope == '2':
        var = resta(num1,num2)
        print(var)
    elif ope == '3':
        var = mult(num1,num2)
        print(var)
    elif ope == '4':
        var = div(num1,num2)
        print(var)
    elif ope == '5':
        menu()
    elif ope == '6':
        break
    else:
        print("no esta dentro de las opciones")