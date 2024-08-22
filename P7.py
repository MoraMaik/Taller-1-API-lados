def contar_vocales(cadena):
    vocales = 0
    for char in cadena:
        if char in 'aeiouAEIOU':
            vocales += 1
        if vocales >= 2:
            return vocales
    return vocales

def buscar_cadena_con_vocales(cadena1, cadena2, cadena3, cadena4, cadena5):
    if contar_vocales(cadena1) >= 2:
        print(cadena1)
        return
    if contar_vocales(cadena2) >= 2:
        print(cadena2)
        return
    if contar_vocales(cadena3) >= 2:
        print(cadena3)
        return
    if contar_vocales(cadena4) >= 2:
        print(cadena4)
        return
    if contar_vocales(cadena5) >= 2:
        print(cadena5)
        return
    
    print("No existe")
