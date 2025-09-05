# creamos un arreglo (lista en Python) con características: altura, edad, peso
vector = [1.75, 20, 70]  # altura (m), edad (años), peso (kg)

# mostrar el vector inicial
print("Vector inicial:", vector)

# acceder a un elemento por índice
indice = int(input("Ingresa el índice del elemento que quieres ver (0=altura, 1=edad, 2=peso): "))
print("Elemento en índice", indice, ":", vector[indice])

# modificar un valor
nuevo_valor = float(input("Ingresa el nuevo valor para ese índice: "))
vector[indice] = nuevo_valor
print("Vector actualizado:", vector)

# calcular la media
media = sum(vector) / len(vector)
print("La media de los elementos es:", media)
