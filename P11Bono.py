def es_matriz_magica(matriz):
    n = len(matriz)  # tamaño de la matriz (n x n)
    
    # calc la + de la primera fila como referencia
    suma_referencia = 0
    for j in range(n):
        suma_referencia += matriz[0][j]
    
    # verifica si todas las filas tienen la misma +
    for i in range(1, n):
        suma_fila = 0
        for j in range(n):
            suma_fila += matriz[i][j]
        if suma_fila != suma_referencia:
            return False
    
    # verfica si todas las columnas tienen la misma +
    for j in range(n):
        suma_columna = 0
        for i in range(n):
            suma_columna += matriz[i][j]
        if suma_columna != suma_referencia:
            return False
    
    # verifica la + de la diagonal principal
    suma_diagonal_principal = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
    if suma_diagonal_principal != suma_referencia:
        return False
    
    # verfica la + de la diagonal secundaria
    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_secundaria += matriz[i][n - i - 1]
    if suma_diagonal_secundaria != suma_referencia:
        return False
    
    # SI todas las + son =, la matriz es |magica|
    return True

# ejemplo

# definimos una matriz 
matriz = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

# llama a la funcion para verif si la matriz es |magica|
if es_matriz_magica(matriz):
    print("La matriz es mágica.")
else:
    print("La matriz no es mágica.")
