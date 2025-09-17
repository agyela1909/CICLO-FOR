#CICLO7
#CarolAgyelaGonzalezOchoa

contador_positivos = 0
contador_negativos = 0

for i in range(20):
    numero = float(input(f"Ingresa el número {i + 1}: "))

    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")