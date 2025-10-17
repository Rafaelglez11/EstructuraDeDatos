
# Registro de Intensidades de Luz

# Crear la matriz 4x4 con valores iniciales (por ejemplo, intensidades aleatorias)
import random

matriz = [[random.randint(0, 100) for _ in range(4)] for _ in range(4)]

# Función para imprimir la matriz completa
def mostrar_matriz(m):
    print("\nMatriz de intensidades de luz (4x4):")
    for fila in m:
        print(fila)

# Función para consultar la intensidad en una posición específica
def consultar_intensidad(m):
    fila = int(input("Ingrese el número de fila (0-3): "))
    columna = int(input("Ingrese el número de columna (0-3): "))
    print(f"La intensidad en la posición [{fila}][{columna}] es: {m[fila][columna]}")

# Función para modificar la intensidad en una posición específica
def modificar_intensidad(m):
    fila = int(input("Ingrese la fila (0-3): "))
    columna = int(input("Ingrese la columna (0-3): "))
    nuevo_valor = int(input("Ingrese el nuevo valor de intensidad (0-100): "))
    m[fila][columna] = nuevo_valor
    print(f"Valor actualizado en la posición [{fila}][{columna}] a {nuevo_valor}")

# Función para calcular el promedio general de la matriz
def promedio_intensidad(m):
    suma = sum(sum(fila) for fila in m)
    total = len(m) * len(m[0])
    promedio = suma / total
    print(f"El promedio general de intensidades es: {promedio:.2f}")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar matriz completa")
    print("2. Consultar intensidad en una posición")
    print("3. Modificar intensidad")
    print("4. Calcular promedio general")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        mostrar_matriz(matriz)
    elif opcion == "2":
        consultar_intensidad(matriz)
    elif opcion == "3":
        modificar_intensidad(matriz)
    elif opcion == "4":
        promedio_intensidad(matriz)
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
