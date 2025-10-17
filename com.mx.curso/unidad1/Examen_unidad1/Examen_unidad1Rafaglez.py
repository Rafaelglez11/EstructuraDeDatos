
# Rafael Gonzalez Reyes                         Examen 1 

import numpy as np

def diagonalDiferencia(arreglo):
    #arreglo de numpy
    matriz = np.array(arreglo)
    
    #suma de la diagonal principal 
    principal = np.trace(matriz)
    
    #suma de la diagonal secundaria 
    secondaria = np.trace(np.fliplr(matriz))
    
    return abs(principal - secondaria)

arreglo = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDiferencia(arreglo)) 

