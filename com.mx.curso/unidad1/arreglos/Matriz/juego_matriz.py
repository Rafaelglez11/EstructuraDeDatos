# Ejercicio 7: Tablero de Juego con Matriz

# Paso 1: Crear la matriz vacía 5x5
tablero = []

# Paso 2: Llenar la matriz con datos del usuario
print("Ingrese los valores del tablero (0 = vacío, 1 = obstáculo):")
for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Celda [{i}][{j}]: "))
        while valor not in [0, 1]:  # Validación
            print("Solo se permiten 0 (vacío) o 1 (obstáculo).")
            valor = int(input(f"Celda [{i}][{j}]: "))
        fila.append(valor)
    tablero.append(fila)

# Paso 3: Mostrar tablero
print("\n🟦 Tablero del juego:")
for fila in tablero:
    print(fila)

# Paso 4: Contar obstáculos en todo el tablero
total_obstaculos = 0
for i in range(5):
    for j in range(5):
        if tablero[i][j] == 1:
            total_obstaculos += 1

# Paso 5: Contar obstáculos en una fila específica
fila_usuario = int(input("\nIngrese el número de fila (0 a 4) para analizar: "))
obstaculos_fila = tablero[fila_usuario].count(1)

# Paso 6: Mostrar resultados
print("\n📊 Resultados:")
print("Total de obstáculos en el tablero:", total_obstaculos)
print(f"Obstáculos en la fila {fila_usuario}:", obstaculos_fila)
