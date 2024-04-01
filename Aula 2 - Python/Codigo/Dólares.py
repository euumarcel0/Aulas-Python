def converter_para_dolares(valor_em_reais):
    taxa_de_cambio = 4.96
    valor_em_dolares = valor_em_reais / taxa_de_cambio
    return round(valor_em_dolares, 2)

# Solicita ao usuário que insira o valor em reais
valor_em_reais = float(input("Digite o valor em reais (R$): "))

# Converte o valor para dólares e exibe o resultado
valor_em_dolares = converter_para_dolares(valor_em_reais)
print(f"O valor em dólares é: US$ {valor_em_dolares}")
