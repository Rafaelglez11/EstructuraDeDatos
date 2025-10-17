# Ejercicio 8: Calificaciones de Estudiantes con Matriz y Vectores

# Paso 1: Número de estudiantes
num_estudiantes = int(input("Ingrese el número de estudiantes: "))

# Paso 2: Crear la matriz
calificaciones = []

# Paso 3: Ingreso de datos
for i in range(num_estudiantes):
    fila = []
    print(f"\nIngrese las calificaciones del estudiante {i}:")
    for j in range(3):  # 3 exámenes
        nota = float(input(f"  Examen {j+1}: "))
        fila.append(nota)
    calificaciones.append(fila)

# Paso 4: Calcular promedio de cada estudiante (vector)
promedios_estudiantes = []
for i in range(num_estudiantes):
    promedio = sum(calificaciones[i]) / 3
    promedios_estudiantes.append(promedio)

# Paso 5: Calcular promedio de cada examen (columna)
promedios_examenes = []
for j in range(3):
    suma = 0
    for i in range(num_estudiantes):
        suma += calificaciones[i][j]
    promedios_examenes.append(suma / num_estudiantes)

# Paso 6: Buscar la calificación más alta y su estudiante
max_nota = -1
estudiante_max = -1
for i in range(num_estudiantes):
    for j in range(3):
        if calificaciones[i][j] > max_nota:
            max_nota = calificaciones[i][j]
            estudiante_max = i

# Paso 7: Mostrar resultados
print("\n📊 Resultados:")
print("Matriz de calificaciones:")
for fila in calificaciones:
    print(fila)

print("\nPromedio de cada estudiante:", promedios_estudiantes)
print("Promedio de cada examen:", promedios_examenes)
print(f"\nLa calificación más alta fue {max_nota}, obtenida por el estudiante {estudiante_max}")
