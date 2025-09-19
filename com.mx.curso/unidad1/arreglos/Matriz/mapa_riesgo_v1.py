# Mapa de riesgo 

# Creaar una matriz de 8x8 

matriz = [
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    ]
    


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print (matriz[i][j], end="")
    print()


area_riesgo =0
area_precaucion =0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] ==2:
            area_riesgo +=1
        if matriz[i][j]==1:
            area_precaucion +=1
    print()

print(f"Area de Riesgo (2): {area_riesgo}")
print(f"Area de precaucion (1): {area_precaucion}")





