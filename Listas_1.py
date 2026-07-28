print("Ejercicio 1")
lista=[]
for i in range(5):
    usuario=input("Ingrese un nombre: ")
    lista.append(usuario)
print(lista)
print("Ejercicio 2")
lista=[]
for i in range(5):
    num=int(input())
    lista.append(num)
res=sum(lista)
print(lista)
print(res)
print("Ejercicio 3")
lista=[]
tupla=("banana,manzana,pera,kiwi,granada")
frut=input("Ingrese una fruta: ")
if frut in tupla:
    print("Esta dentro de la lista")
else:
    print("No esta en la lista")
print("Ejercicio 4")
lista=[]
tupla=input("Ingrese un productoy su valor: ")
tupla1=input("Ingrese un productoy su valor: ")
tupla2=input("Ingrese un productoy su valor: ")
lista=tupla+tupla1+tupla2
print(lista)

