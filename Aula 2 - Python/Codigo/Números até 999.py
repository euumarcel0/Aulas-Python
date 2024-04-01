# Definição da função para separar os dígitos de um número
def separar_digitos(numero):
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    return milhar, centena, dezena, unidade

# Entrada de um número entre 0 e 9999
numero = int(input("Digite um número entre 0 e 9999: "))

# Chamada da função para separar os dígitos e exibição dos resultados
milhar, centena, dezena, unidade = separar_digitos(numero)
print(f"Milhar: {milhar}, Centena: {centena}, Dezena: {dezena}, Unidade: {unidade}")