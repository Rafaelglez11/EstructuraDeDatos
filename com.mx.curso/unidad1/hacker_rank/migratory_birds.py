

birds = [1, 4, 4, 4, 5, 3]

# Contar ocurrencias con un diccionario
conteo = {}
for b in birds:
    conteo[b] = conteo.get(b, 0) + 1

# Determinar la máxima cantidad de apariciones
max_cant = max(conteo.values())

# Filtrar los tipos que tienen esa cantidad máxima y escoger el menor
tipos_con_max = [tipo for tipo, cantidad in conteo.items() if cantidad == max_cant]
tipo_mas_comun = min(tipos_con_max)

print("Conteo por tipo:", conteo)
print("Tipos con máxima frecuencia:", tipos_con_max)
print("Tipo más pequeño entre los más frecuentes:", tipo_mas_comun)

