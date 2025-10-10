

def esta_en_rango(pos, inicio, fin):
    """Devuelve True si pos está en el rango inclusivo [inicio, fin]."""
    return inicio <= pos <= fin

def contar_frutas_en_casa(s, t, a, b, apples, oranges):
    manzanas_en_casa = 0
    naranjas_en_casa = 0

    # posiciones finales de cada manzana y conteo
    for distancia in apples:
        posicion = a + distancia
        if esta_en_rango(posicion, s, t):
            manzanas_en_casa += 1

    # posiciones finales de cada naranja y conteo
    for distancia in oranges:
        posicion = b + distancia
        if esta_en_rango(posicion, s, t):
            naranjas_en_casa += 1

    return manzanas_en_casa, naranjas_en_casa

if __name__ == "__main__":
    # Valores (idénticos a los de tu script original)
    s, t = 7, 10      # límites de la casa
    a, b = 4, 12      # posiciones de los árboles
    apples = [2, 3, -4]
    oranges = [3, -2, -4]

    manzanas, naranjas = contar_frutas_en_casa(s, t, a, b, apples, oranges)
    print("Manzanas: ", manzanas)
    print("Naranjas: ", naranjas)

