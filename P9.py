import numpy as np

# Ingreso de números
numeros = [float(input(f"Por favor ingrese el número {i+1}: ")) for i in range(5)]

# Cálculo de operaciones
promedio = np.mean(numeros)
mediana = np.median(numeros)
promedio = np.prod(numeros) ** (1/len(numeros))
ascendente = np.sort(numeros)
descendente = np.sort(numeros)[::-1]
potencia = max(numeros) ** min(numeros)
raiz_cubica = np.cbrt(min(numeros))

# Impresión de resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Promedio: {promedio}")
print(f"Números en orden ascendente: {ascendente}")
print(f"Números en orden descendente: {descendente}")
print(f"La potencia del mayor número elevado al menor número: {potencia}")
print(f"La raíz cúbica del menor número: {raiz_cubica}")
