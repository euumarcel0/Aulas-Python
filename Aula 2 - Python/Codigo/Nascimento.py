# Definição da função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = 2024  # Considerando que o ano atual seja 2024
    return ano_atual - ano_nascimento

# Entrada do ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = calcular_idade(ano_nascimento)

# Exibição da idade calculada
print(f"A idade é: {idade} anos.")