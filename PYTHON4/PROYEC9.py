#CICLO9
#CarolAgyelaGonzalezOchoa

nombres = []
telefonos = []
correos = []

# Capturar 15 elementos
for i in range(15):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo: ")

    # Agregar a las listas
    nombres.append(nombre)
    telefonos.append(telefono)
    correos.append(correo)

# Imprimir el directorio
print("\nDirectorio:")
for i in range(15):
    print(f"{nombres[i]} - Teléfono: {telefonos[i]}, Correo: {correos[i]}")