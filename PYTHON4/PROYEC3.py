#CICLO3
#CarolAgyelaGonzalezOchoa

productos = []

for i in range(10):
    nombre = input(f"Ingresa el nombre del producto {i + 1}: ")
    calidad = input("Ingresa la calidad del producto: ")
    precio = float(input("Ingresa el precio del producto: "))

    productos.append({"nombre": nombre, "calidad": calidad, "precio": precio})

total_compra = sum(producto["precio"] for producto in productos)

print("\nProductos comprados:")
for producto in productos:
    print(f"Nombre: {producto['nombre']}, Calidad: {producto['calidad']}, Precio: {producto['precio']}")

print(f"\nTotal de la compra: {total_compra}")
