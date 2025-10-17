# Ejercicio 4: Historial de Entrenamiento de un Modelo

# Paso 1: Crear una lista vacía para guardar las precisiones
precisiones = []

print("Ingrese la precisión de cada época (escriba -1 para finalizar):")

# Paso 2: Bucle para leer valores
while True:
    valor = float(input("Precisión: "))
    if valor == -1:  # Condición de salida
        break
    precisiones.append(valor)  # Agregar a la lista

# Paso 3: Verificar que la lista no esté vacía
if len(precisiones) > 0:
    precision_final = precisiones[-1]   # Último valor
    precision_maxima = max(precisiones) # Mayor valor registrado
    
    # Paso 4: Mostrar resultados
    print("\nHistorial de precisiones:", precisiones)
    print("Precisión final:", precision_final)
    print("Precisión más alta:", precision_maxima)
else:
    print("\nNo se ingresaron valores de precisión.")
