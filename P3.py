def invertir_numero(n):
    # inicio de la variable que almacenara el numero invertido
    invertido = 0
    
    # mientras queden dig en n
    while n > 0:
        # obtenemos el ult dig de n
        ultimo_digito = n % 10
        # dezplamaos los dig ya invertidos a la izquierda (X por 10) y + el ult dig
        invertido = invertido * 10 + ultimo_digito
        # quitamos el ult dig de n
        n = n // 10
    
    # retornamos el num invertido
    return invertido

def son_espejos(a, b):
    # invertimos el num a
    a_invertido = invertir_numero(a)
    
    # comparar el num invertido de a con b
    if a_invertido == b:
        return True
    else:
        return False

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

# verifica si son nums espejos
if son_espejos(numero1, numero2):
    print("Los numeros son espejos.")
else:
    print("Los numeros no son espejos.")
