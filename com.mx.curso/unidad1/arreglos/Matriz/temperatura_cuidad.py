# Mapa de Temperaturas en una Ciudad

# Crear una matriz 3x3 con temperaturas iniciales (por ejemplo, valores aleatorios entre 15 y 35)
import random

temperaturas = [[random.randint(15, 35) for _ in range(3)] for _ in range(3)]

# Función para imprimir toda la matriz
def mostrar_mapa(m):
    print("\nMapa de temperaturas (3x3):")
    for fila in m:
        print(fila)

# Función para acceder a una celda específica (por ejemplo, la central)
def consultar_temperatura(m):
    fila = int(input("Ingrese el número de fila (0-2): "))
    columna = int(input("Ingrese el número de columna (0-2): "))
    print(f"La temperatura en la zona [{fila}][{columna}] es: {m[fila][columna]} °C")

# Función para modificar una temperatura en una celda
def modificar_temperatura(m):
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    nueva_temp = float(input("Ingrese la nueva temperatura: "))
    m[fila][columna] = nueva_temp
    print(f"Temperatura actualizada en la zona [{fila}][{columna}] a {nueva_temp} °C")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar mapa de temperaturas")
    print("2. Consultar temperatura en una zona")
    print("3. Modificar temperatura de una zona")
    print("4. Mostrar temperatura central")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        mostrar_mapa(temperaturas)
    eli
