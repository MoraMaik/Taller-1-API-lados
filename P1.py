# Prog para separar los digitos de un numero entero

numero = int(input("Ingresa un número entero: "))

#Lista para almacenar los dig
digitos = []

# verificar si el número es -
if numero < 0:
    numero = -numero  # Convertir a +

# usar ciclo while 
while numero > 0:
    digito = numero % 10 
    digitos.append(digito) 
    numero = numero // 10  # quitar ultimo dig del num

# invertir la lista de dig pq se agregaron al rev

digitos.reverse()


print("Los digitos separados son:", digitos)
