# Ejercicio 6: Análisis de Ventas Diarias con Arreglos

# Paso 1: Crear arreglo para almacenar ventas de lunes a domingo
ventas = []

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Paso 2: Pedir al usuario las ventas de cada día
print("Ingrese las ventas de cada día de la semana:")
for i in range(7):
    valor = float(input(f"Ventas del {dias[i]}: "))
    ventas.append(valor)

# Paso 3: Calcular total de ventas de la semana
total_ventas = sum(ventas)

# Paso 4: Buscar día con más ventas y día con menos ventas
maximo = max(ventas)
minimo = min(ventas)
dia_max = dias[ventas.index(maximo)]
dia_min = dias[ventas.index(minimo)]

# Paso 5: Mostrar resultados
print("\n📊 Resultados del análisis de ventas:")
print("Ventas registradas:", ventas)
print("Total de ventas de la semana:", total_ventas)
print(f"Día con más ventas: {dia_max} ({maximo})")
print(f"Día con menos ventas: {dia_min} ({minimo})")
