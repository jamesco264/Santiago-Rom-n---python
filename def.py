# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 18/8/2025 
# Título de la actividad: def 
# ------------------------------------------
def suma(): 
    print("Ingrese dos valores")
    a = int(input("Ingrese el 1er valor: "))
    b = int(input("Ingres el 2do valor: "))
    resultado = a + b
    print(f'{a} + {b} = {resultado}')
    print(a, '+', b, '=', resultado)

def resta():
    print("Ingrese dos valores")
    a = int(input("Ingrese el 1er valor: "))
    b = int(input("Ingres el 2do valor: "))
    resultado = a - b 
    print("El resultado es: ", resultado)


def mult():
    print("Ingrese dos valores")
    a = int(input("Ingrese el 1er valor: "))
    b = int(input("Ingres el 2do valor: "))
    resultado = a * b 
    print("El resultado es: ", resultado)

print("Suma")
suma()

print("Resta")
resta()

print("Multiplicaion")
mult()

