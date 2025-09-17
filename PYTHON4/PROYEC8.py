#CICLO8
#CarolAgyelaGonzalezOchoa

descripciones = []
cantidades = []
precios = []

for i in range(10):
    descripcion = input(f"Ingrese la descripción del producto {i + 1}: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    descripciones.append(descripcion)
    cantidades.append(cantidad)
    precios.append(precio)

print("\nProductos en la ferretería:")
for i in range(10):
    print(f"{cantidades[i]} {descripciones[i]} ${precios[i]}")