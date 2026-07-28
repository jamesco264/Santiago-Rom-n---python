# ------------------------------------------ 
# Autor: Santiago Román
# Fecha: 3/11/2025 
# Título de la actividad: Algortimo de ordenamiento 2
# ------------------------------------------

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        valmin = i
        for j in range(i + 1, n):
            if arr[j] < arr[valmin]:
                valmin = j
        if valmin != i:
            arr[i], arr[valmin] = arr[valmin], arr[i]
    print(arr) 

# Ejemplo:
datos = [88, 33, 11, 44, 22]
selection_sort(datos)
# print(datos) # Imprime: [11, 22, 33, 44, 88]
