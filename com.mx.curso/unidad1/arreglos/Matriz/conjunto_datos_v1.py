# Limpieza de conjunto de datos para la IA:
import numpy as np
data = np.array(
    [[10.9,9.1,20.1,30.1],
    [5.9,2.1,20.1,30.1],
    [10.9,3.1,20.1,30.1],
    [10.9,4.1,20.1,30.1],
    [7.9,5.1,20.1,30.1],
    [10.9,6.1,20.1,30.1],
    [10.9,7.1,20.1,30.1],
    [10.9,8.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,10.1,20.1,30.1]])

print("Datos originales: ")
print(data)

# Simular una fila con error:
data[5] = [99.99,99.99,99.99,99.99]
data[0,1] = np.nan
data[5,2] = np.nan
data[9,3] = np.nan

print("\n---- Datos con errores ----")
print(data)

# Eliminar filas con NaN
data_sin_errores = np.delete(data, 5, axis= 0)

print("\n---- Datos sin errores ----")
print(data_sin_errores)

media_columna = np.nanmean(data_sin_errores, axis=0)
print("---- Media de cada columna ----")
print(media_columna)

# Llenar los valores en dónde hay Nan:
for i in range(data.shape[0]): # Filas
    for j in range(data.shape[1]): # Columnas
        if np.isnan(data[i, j]):
            data[i, j] = media_columna[j]

print("\n----- Valores sin NaN -----")
print(data)