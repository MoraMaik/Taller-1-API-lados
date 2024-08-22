def mcd_iterativo(a, b):
    # usamos el algoritmo de Euclides de manera iterativa
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    # se calcula el MCM usando la relacion entre MCM y MCD
    return abs(a * b) // mcd_iterativo(a, b)

# ingresa dos num enteros
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

# calcula el MCM y lo muestra
resultado = mcm(numero1, numero2)
print(f"El minimo comun Multiplo de {numero1} y {numero2} es: {resultado}")
