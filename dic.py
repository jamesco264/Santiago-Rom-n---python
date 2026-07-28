# Estructura de datos global para simular el inventario
# {
#     'LECHE': {'precio': 1.50, 'stock': 100},
#     'PAN': {'precio': 2.00, 'stock': 50}
# }
inventario_global = { "LECHE": {'precio': 1.50, 'stock': 100}, "PAN": {'precio': 2.00, 'stock': 50} }

# Función para agregar o actualizar un producto
def agregar_o_actualizar_producto(nombre, precio, stock):
    # COMPLETAR:
    # 1. Verificar que el precio y el stock sean positivos (> 0). Si no, devolver un error.
    # 2. Convertir el nombre a mayúsculas para evitar duplicados.
    # 3. Si el producto ya existe, ACTUALIZAR su precio y AÑADIR el stock al existente.
    # 4. Si el producto no existe, crearlo.
    if precio > 0 and stock > 0:
        if nombre in inventario_global:
            inventario_global[nombre]['precio'] = precio
            inventario_global[nombre]['stock'] = inventario_global[nombre]['stock'] + stock
            return ("Producto actualizado")
        else:
            inventario_global[nombre] = {'precio' : precio, 'stock' : stock}
            return ("Producto agregado")
    else:
        return ("No se agrego porque no hay stock")

# Función para registrar una venta
def registrar_venta(nombre, cantidad):
    # COMPLETAR:
    # 1. Convertir el nombre a mayúsculas.
    # 2. Verificar que la cantidad sea positiva (> 0). Si no, devolver un error.
    # 3. Verificar si el producto existe. Si no, devolver un error.
    # 4. Verificar si hay suficiente stock. Si no, devolver un error con el stock actual.
    # 5. Si todo es correcto, restar la cantidad del stock y calcular el ingreso total.
    gan = 0
    if cantidad > 0 :
        nombre = nombre.upper()
        if nombre in inventario_global and cantidad:
            if inventario_global[nombre]['stock'] >= cantidad:
                inventario_global[nombre]['stock'] = inventario_global[nombre]['stock'] - cantidad
                gan = cantidad * inventario_global[nombre]['precio']
                return gan 
            else:
                return("No hay suficiente stock")
        else:
            return("El producto no se encuentra en el inventario o no hay suficiente stock")

# Función para mostrar el inventario actual
def mostrar_inventario():
    if not inventario_global:
        return "El inventario está vacío."
    salida = "\n--- INVENTARIO ACTUAL ---\n"
    for nombre, datos in inventario_global.items():
        salida += f"Producto: {nombre:<10} | Precio: ${datos['precio']:.2f} | Stock: {datos['stock']} unidades\n"
    return salida


# -----------------------------------------------------
# Programa Principal de Prueba
# -----------------------------------------------------

print("--- Sistema Básico de Gestión de Inventario ---")

# --- 1. AGREGAR / ACTUALIZAR PRODUCTOS ---
print("\n--- AGREGANDO PRODUCTOS ---")

# Agregar producto nuevo (ACEITE)
print(agregar_o_actualizar_producto("Aceite", 4.50, 20))

# Agregar otro producto nuevo (ATÚN)
print(agregar_o_actualizar_producto("Atún", 1.20, 100))

# Intentar agregar un producto con datos inválidos (Stock <= 0)
print(agregar_o_actualizar_producto("Fideos", 1.00, 0))

# Actualizar producto existente (ACEITE)
# Se actualiza el precio a 5.00 y se añaden 5 unidades al stock
print(agregar_o_actualizar_producto("Aceite", 5.00, 5))

# Mostrar inventario después de las adiciones/actualizaciones
print(mostrar_inventario())


# --- 2. REGISTRAR VENTAS ---
print("\n--- REGISTRANDO VENTAS ---")

# Venta exitosa (ATÚN)
print(registrar_venta("Atún", 10))

# Venta exitosa (ACEITE)
print(registrar_venta("Aceite", 3))

# Intento de venta de producto inexistente
print(registrar_venta("Papas", 10))

# Intento de venta con stock insuficiente (ACEITE tiene 25 unidades: 20 iniciales + 5 añadidas)
print(registrar_venta("Aceite", 30))

# Mostrar inventario después de las ventas
print(mostrar_inventario())