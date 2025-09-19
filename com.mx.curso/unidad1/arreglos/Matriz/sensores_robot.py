

# Lecturas de los sensores en cm
lecturas = [120, 85, 210, 150]

# Umbral crítico
umbral = 100

# Recorremos cada lectura
for i in range(len(lecturas)):
    valor = lecturas[i]
    print(f"Sensor {i+1}: {valor} cm")

    # Si la lectura es menor al umbral, mostramos advertencia
    if valor < umbral:
        print("  ⚠ ADVERTENCIA: Distancia crítica detectada.")


