# Definição da função para calcular as notas necessárias para um saque
def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for nota in notas:
        qtd_notas = valor // nota
        if qtd_notas > 0:
            resultado[nota] = qtd_notas
            valor -= qtd_notas * nota

    return resultado

# Entrada do valor a ser sacado
valor_saque = int(input("Valor do saque: R$ "))
notas = calcular_notas(valor_saque)

# Exibição das notas necessárias para o saque
for nota, qtd in notas.items():
    print(f"Notas de R$ {nota}: {qtd}")