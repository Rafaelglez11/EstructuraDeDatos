import numpy as np

# Cargar data_set
datos = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/practica_numpy_1/iris/iris.data', delimiter=',', dtype='object')
print(datos)

# Cargar solo las primeras cuatro columnas:
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/practica_numpy_1/iris/iris.data', delimiter=',', usecols=(0,1,2,3))
print(datos_numericos)

# Datos a eliminar:
indices_eliminar = [0,1,2,50]

# Eliminar las filas con los indices detectados con error
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)
print("\n----- Datos limpios -----")
print(datos_limpios)

datos_limpios[0,0] = np.nan
datos_limpios[4,0] = np.nan
datos_limpios[2,2] = np.nan
datos_limpios[12,1] = np.nan
datos_limpios[10,2] = np.nan
datos_limpios[3,1] = np.nan
datos_limpios[4,1] = np.nan
datos_limpios[5,0] = np.nan
datos_limpios[25,1] = np.nan
datos_limpios[26,1] = np.nan
datos_limpios[145,1] = np.nan

# Matriz con datos faltantes o NaN:
print("\n--- Datos faltantes ---")
print(datos_limpios)

media_columna = np.nanmean(datos_limpios, axis=0)
print("\n---- Media de cada columna ----")
print(media_columna)

for i in range(datos_limpios.shape[0]):
    for j in range(datos_limpios.shape[1]):
        if np.isnan(datos_limpios[i, j]):
            datos_limpios[i, j] = media_columna[j]

print("\n -- Datos sin errores y con NaN remplazados --")
print(datos_limpios)