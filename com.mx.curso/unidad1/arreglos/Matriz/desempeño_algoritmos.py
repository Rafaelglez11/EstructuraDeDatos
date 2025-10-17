# -*- coding: utf-8 -*-
import time
import random

# Función para medir tiempos de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    final = time.time()
    return resultado, final - inicio

# ---------- ALGORITMOS DE ORDENAMIENTO ---------- #

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def particion(lista, inicio, fin):
    pivote = lista[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

def quicksort(lista, inicio, fin):
    if inicio < fin:
        indice_pivote = particion(lista, inicio, fin)
        quicksort(lista, inicio, indice_pivote - 1)
        quicksort(lista, indice_pivote + 1, fin)
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def select_sort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

# ---------- ALGORITMOS DE BÚSQUEDA ---------- #

def busqueda_binaria(lista, objetivo):
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(A, p, r, x):
    if p > r:
        return -1
    mid = (p + r) // 2
    if A[mid] == x:
        return mid
    elif A[mid] < x:
        return binary_search_recursive(A, mid + 1, r, x)
    else:
        return binary_search_recursive(A, p, mid - 1, x)

# ---------- PRUEBAS DE LOS ALGORITMOS ---------- #

# Ordenamiento
print("\n=== PRUEBA DE ORDENAMIENTO ===")
arr = [29, 10, 14, 37, 13]
print("Original:", arr)
print("Selection Sort:", select_sort(arr.copy()))
print("Merge Sort:", mergeSort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("QuickSort:", quicksort(arr.copy(), 0, len(arr) - 1))

# Búsqueda
print("\n=== PRUEBA DE BÚSQUEDA ===")
nums = [2, 4, 7, 10, 15, 20, 35]
x = 15
pos_iter, _ = medir_tiempo(busqueda_binaria, nums, x)
pos_rec, _ = medir_tiempo(binary_search_recursive, nums, 0, len(nums) - 1, x)
print(f"Búsqueda binaria iterativa → {x} encontrado en posición {pos_iter}")
print(f"Búsqueda binaria recursiva → {x} encontrado en posición {pos_rec}")

# ---------- MEDICIÓN DE DESEMPEÑO ---------- #

print("\n=== MEDICIÓN DE DESEMPEÑO ===")
sizes = [5000, 10000, 50000, 100000]
algoritmos = {
    "Selection Sort": select_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": mergeSort,
    "QuickSort": lambda arr: quicksort(arr, 0, len(arr) - 1)
}

for size in sizes:
    print(f"\nTamaño de lista: {size}")
    valores = [random.randint(0, 100000) for _ in range(size)]

    for nombre, algoritmo in algoritmos.items():
        arr_copia = valores.copy()
        _, tiempo = medir_tiempo(algoritmo, arr_copia)
        print(f"{nombre:15s} → {tiempo:.5f} segundos")

# Búsqueda en lista grande
print("\n=== DESEMPEÑO DE BÚSQUEDA ===")
lista_grande = sorted([random.randint(0, 1000000) for _ in range(500000)])
objetivo = random.choice(lista_grande)

_, tiempo_bin = medir_tiempo(busqueda_binaria, lista_grande, objetivo)
_, tiempo_rec = medir_tiempo(binary_search_recursive, lista_grande, 0, len(lista_grande)-1, objetivo)
print(f"Búsqueda binaria iterativa: {tiempo_bin:.6f} segundos")
print(f"Búsqueda binaria recursiva: {tiempo_rec:.6f} segundos")
