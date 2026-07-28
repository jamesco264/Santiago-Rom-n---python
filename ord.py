# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 3/11/2025 
# Título de la actividad: Algortimo de ordenamiento
# ------------------------------------------


def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                alm = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = alm
    return lista


lista_desordenada = [4, 3, 1, 9, 2, 5]

lista_ordenada = ordenamiento_burbuja(lista_desordenada)

print("Lista desordenada: ", lista_desordenada)

print("Lista ordenada: ", lista_ordenada)