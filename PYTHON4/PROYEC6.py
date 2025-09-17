#CICLO6
#CarolAgyelaGonzalezOchoa

contador_adultos = 0

for i in range(20):
    edad = int(input(f"Ingresa la edad de la persona {i + 1}: "))

    if edad >= 18:
        contador_adultos += 1

print(f"Número de adultos que asisten al evento: {contador_adultos}")
