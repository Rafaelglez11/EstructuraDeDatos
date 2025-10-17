# Ejercicio 5: Sistema de Recomendación de Películas con Matrices

# Paso 1: Crear la matriz de calificaciones (usuarios x películas)
calificaciones = [
    [5, 3, 4, 4],  # Usuario 1
    [3, 1, 2, 3],  # Usuario 2
    [4, 3, 4, 5],  # Usuario 3
    [5, 5, 5, 4],  # Usuario 4
    [2, 3, 3, 1]   # Usuario 5
]

num_usuarios = len(calificaciones)
num_peliculas = len(calificaciones[0])

# Paso 2: Imprimir matriz completa
print("Matriz de calificaciones (usuarios x películas):")
for fila in calificaciones:
    print(fila)

# Paso 3: Calcular promedio de una película específica
pelicula = int(input(f"\nIngrese el número de película (0 a {num_peliculas-1}): "))
suma = 0
for i in range(num_usuarios):
    suma += calificaciones[i][pelicula]
promedio = suma / num_usuarios
print(f"Promedio de calificaciones de la película {pelicula}: {promedio:.2f}")

# Paso 4: Mostrar vector de calificaciones de un usuario específico
usuario = int(input(f"\nIngrese el número de usuario (0 a {num_usuarios-1}): "))
print(f"Calificaciones del usuario {usuario}: {calificaciones[usuario]}")
