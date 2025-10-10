# Implementación de Timsort en Python

MIN_MERGE = 32

# -------------------------------
# Función para calcular el tamaño mínimo del run
def minRunLength(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

# -------------------------------
# Insertion Sort (para runs pequeños)
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# -------------------------------
# Función merge (para fusionar runs)
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

# -------------------------------
# Función principal: Timsort
def timSort(arr):
    n = len(arr)
    minRun = minRunLength(n)

    # 1. Ordenar bloques pequeños con Insertion Sort
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # 2. Combinar runs con Merge
    size = minRun
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n-1, left + size - 1)
            right = min((left + 2*size - 1), (n-1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# -------------------------------
# Ejemplo de uso
arr = [5, 21, 7, 23, 19, 10, 3, 1, 8, 15]
print("Arreglo original:", arr)
timSort(arr)
print("Arreglo ordenado:", arr)
