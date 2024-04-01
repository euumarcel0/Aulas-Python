# Exemplo 1 - Encontrar o numero que seja par e somando eles
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Variável para armazenar a soma dos números pares
soma_pares = 0

# Loop for para iterar sobre cada número na lista
for numero in numeros:
    # Verifica se o número é par
    if numero % 2 == 0:
        # Se for par, adiciona o número à soma_pares
        soma_pares += numero

# Imprime a soma dos números pares na lista
print("A soma dos números pares na lista é: " + str(soma_pares))


# Exemplo 2 - Define uma lista de números
numeros = [1, 2, 3, 4, 5]

# Itera sobre cada número na lista
for numero in numeros:
    # Verifica se o número é par
    if numero % 2 == 0:
        print("{} é um número par.".format(numero))
    else:
        print("{} é um número ímpar.".format(numero))