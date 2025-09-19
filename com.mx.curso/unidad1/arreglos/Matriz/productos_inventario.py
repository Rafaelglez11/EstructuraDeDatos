

# Matriz del inventario: [ID, Cantidad, Precio]
inventario = [
    [101, 50, 20.5],  # Producto 1
    [102, 30, 15.0],  # Producto 2
    [103, 80, 12.75]  # Producto 3
]

# Mostrar datos del inventario
print("Datos del inventario:")
for fila in inventario:
    print(f"ID: {fila[0]}, Cantidad: {fila[1]}, Precio: ${fila[2]}")

# Elegimos el segundo producto (índice 1) como ejemplo
indice_producto = 1
cantidad = inventario[indice_producto][1]
precio = inventario[indice_producto][2]

# Calcular el valor total
valor_total = cantidad * precio
print(f"\nValor total del producto {inventario[indice_producto][0]}: ${valor_total:.2f}")

# Actualizar el stock después de vender 10 unidades
inventario[indice_producto][1] -= 10

# Mostrar inventario actualizado
print("\nInventario actualizado:")
for fila in inventario:
    print(f"ID: {fila[0]}, Cantidad: {fila[1]}, Precio: ${fila[2]}")
