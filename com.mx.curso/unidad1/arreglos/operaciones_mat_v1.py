

import numpy as np 

datos = np.array([[10,10,10],
                 [20,20,20],
                 [30,30,30]])

print("datos originlaes:\n",datos)


datos_limpios = np.delete(datos, 1, axis=0)
print("datos con errores introducidos:\n", datos_limpios)

datos[0] =[-1, -2, -2]
print("datos con errores introducidos:\n", datos)

valor_negativo = []
for i in range(datos.shape[0]):
    for j in range(datos.range[1]):
        if datos[i][j]< 0:
            valor_negativo.append((i,j))

datos_limpios = np.delete(datos, valor_negativo, axis=0)
print("datos limpios despues de eliminar valores negativos", datos_limpios)

