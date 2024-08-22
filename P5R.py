def mcd_recursivo(a, b):
    # usamos el algoritmo de Euclides de manera recursiva
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)

def mcm(a, b):
    # se calcula el MCM usando la relacion entre MCM y MCD
    return abs(a * b) // mcd_recursivo(a, b)

# ingresa dos num enteros
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

# calcula el MCM y lo muestra
resultado = mcm(numero1, numero2)
print(f"El minimo comun Multiplo de {numero1} y {numero2} es: {resultado}")
