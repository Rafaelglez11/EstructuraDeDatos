import time 

def tiene_duplicados_lineal(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True 
    return False

# pruebas con diferentes tamaños de arreglos 

sizes = [100,1000,10000]

for n in sizes:
    arr = list(range(n)) # Arreglo sin duplicados para forzar el peor caso 

    start_time = time.time()
    tiene_duplicados_lineal(arr)
    end_time = time.time()

    print(f"Busqueda de duplicados en un arreglo de {n} elementos: {end_time - start_time: .6f} segudnos.")

    