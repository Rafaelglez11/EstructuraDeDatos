
# Limpieza de datos con Numpt:
import numpy as np    

# Simular matriz de 12 x 5:
np.random.seed(42)
datos = np.random.rand(5, 5) * 100

# Simular valores erroneos:
datos[0, 0] = -99
datos[2, 3] = 1000

print("Datos originales:")
print(datos)

indices_erroneos = [0, 2]

datos_limpios = np.delete(datos, indices_erroneos, axis = 0) # Elimina la segunda fila
print("\nDatos limpios:")
print(datos_limpios)