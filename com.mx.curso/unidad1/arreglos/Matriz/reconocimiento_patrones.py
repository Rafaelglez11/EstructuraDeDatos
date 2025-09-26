
# Ejercicio 1: Vector de características para reconocimiento de patrones

# Paso 1: Declarar el vector de características (ejemplo: flor)
vector = [3.5, 1.4, 0.2]  # Longitud de sépalo, longitud de pétalo, anchura de pétalo

# Paso 2: Calcular la suma total del vector
suma_total = sum(vector)

# Paso 3: Crear un nuevo vector normalizado
vector_normalizado = []  # Aquí guardaremos los valores normalizados

# Iterar sobre cada valor y dividirlo entre la suma total
for valor in vector:
    normalizado = valor / suma_total
    vector_normalizado.append(normalizado)

# Paso 4: Mostrar resultados
print("Vector original:", vector)
print("Suma total:", suma_total)
print("Vector normalizado:", vector_normalizado)
