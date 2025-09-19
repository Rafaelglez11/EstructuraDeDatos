
# Crear la matriz del cine (4 filas x 5 columnas) inicializada en 0
cine = [[0 for _ in range(5)] for _ in range(4)]

# Función para imprimir el mapa de asientos
def imprimir_mapa(matriz):
    print("\nMapa de asientos (0 = libre, 1 = ocupado):")
    for fila in matriz:
        print(" ".join(str(asiento) for asiento in fila))

# Mostrar mapa inicial
imprimir_mapa(cine)

# Pedir fila y asiento al usuario
fila = int(input("\nIngrese el número de fila (1-4): ")) - 1
asiento = int(input("Ingrese el número de asiento (1-5): ")) - 1

# Marcar el asiento como ocupado
cine[fila][asiento] = 1

# Mostrar mapa actualizado
imprimir_mapa(cine)

# Contar asientos libres
libres = sum(asiento == 0 for fila in cine for asiento in fila)
print(f"\nNúmero total de asientos libres: {libres}")
