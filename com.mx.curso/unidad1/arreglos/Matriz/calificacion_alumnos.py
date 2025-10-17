# Análisis de Calificaciones de Estudiantes

# Crear un arreglo (lista) con calificaciones iniciales
calificaciones = [85, 90, 78, 92, 88, 76, 95, 89]

# Función para mostrar todas las calificaciones
def mostrar_calificaciones(lista):
    print("\nCalificaciones de los estudiantes:")
    for i, nota in enumerate(lista):
        print(f"Estudiante {i}: {nota}")

# Función para consultar una calificación específica por índice
def consultar_calificacion(lista):
    indice = int(input("Ingrese el número de estudiante (índice): "))
    if 0 <= indice < len(lista):
        print(f"La calificación del estudiante {indice} es: {lista[indice]}")
    else:
        print("Índice fuera de rango.")

# Función para modificar una calificación
def modificar_calificacion(lista):
    indice = int(input("Ingrese el número de estudiante (índice): "))
    if 0 <= indice < len(lista):
        nueva = float(input("Ingrese la nueva calificación: "))
        lista[indice] = nueva
        print(f"Calificación actualizada del estudiante {indice} a {nueva}")
    else:
        print("Índice fuera de rango.")

# Función para calcular el promedio general
def promedio_calificaciones(lista):
    promedio = sum(lista) / len(lista)
    print(f"\nEl promedio general del grupo es: {promedio:.2f}")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar todas las calificaciones")
    print("2. Consultar una calificación")
    print("3. Modificar una calificación")
    print("4. Calcular promedio general")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        mostrar_calificaciones(calificaciones)
    elif opcion == "2":
        consultar_calificacion(calificaciones)
    elif opcion == "3":
        modificar_calificacion(calificaciones)
    elif opcion == "4":
        promedio_calificaciones(calificaciones)
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
