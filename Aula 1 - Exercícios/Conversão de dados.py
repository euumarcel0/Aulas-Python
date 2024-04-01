# Conversão de Dados
# Convertendo uma string para um número inteiro
numero_texto = "10"
print (type (numero_texto))
numero_inteiro = int(numero_texto)
print (numero_inteiro)

#Converter Numero Inteiro em Ponto Flutuante
numero_inteiro = 10
numero_ponto_flutuante = float(numero_inteiro)
print (numero_ponto_flutuante)

# Convertendo um número inteiro para uma string
numero_inteiro = 10
numero_texto = str(numero_inteiro)
print (numero_texto)

# Convertendo um valor para um booleano (0 se torna False, qualquer outro valor se torna True)
valor = 0
valor_booleano = bool(valor)
print (valor_booleano)

# Convertendo uma string para uma lista de caracteres
texto = "Python"
lista_caracteres = list(texto)
print (lista_caracteres)

# Convertendo uma lista de strings para uma única string
lista_palavras = ["Olá", "mundo"]
texto = " ".join(lista_palavras)
print (texto)

# Convertendo uma lista de números para uma única string
numeros = [1, 2, 3, 4, 5]
texto = " ".join(map(str, numeros))
print (texto)

# Convertendo uma string para um número hexadecimal
numero_hex = int("A1", 16)
print(numero_hex)

# Convertendo um número para uma string binária
numero_binario = bin(10)
print(numero_binario)