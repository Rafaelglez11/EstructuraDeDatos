


def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return f"Elemento encontrado en la posición {i}"
    return "Elemento no encontrado"

# Ejemplo de uso
datos = [7, 12, 5, 9, 20]
print(busqueda_lineal(datos, 9))   #  Elemento encontrado en la posición 3
print(busqueda_lineal(datos, 15))  #  Elemento no encontrado

