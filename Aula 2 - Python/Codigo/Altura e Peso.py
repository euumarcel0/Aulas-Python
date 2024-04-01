# Definição da função para calcular o IMC
def calcular_imc(altura, peso):
    return peso / (altura ** 2)

# Entrada da altura e peso do usuário
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

# Cálculo do IMC e exibição do resultado
imc = calcular_imc(altura, peso)
print(f"Seu IMC é: {imc:.2f}")