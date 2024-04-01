# Importa as funções necessárias do módulo pyinputplus
from pyinputplus import inputEmail, inputNum, inputURL, inputChoice, RetryLimitException

# Aceita somente um Email válido
email = inputEmail(prompt='Digite seu Email: ')

# Aceita somente um número inteiro
numero = inputNum(prompt='Digite um número: ')

# Aceita somente um URL válida
url = inputURL(prompt='Digite uma URL: ')

# Input para escolher uma opção da lista
print("Escolha uma opção:")
print("1. Cachorro")
print("2. Gato")
print("3. Boi")
opcao_escolhida = input("Digite o número correspondente à sua escolha: ")

# Input para escolher um número entre 1 e 4
numero_escolhido = input("Escolha um número entre 1 a 4: ")

# Cria um menu com limite de tentativas
try:
    numeros = ['1', '2', '3', '4']
    escolha = inputChoice(numeros, limit=2, prompt='Escolha um número entre 1 a 4: \n')
except RetryLimitException:
    # Se o usuário não escolher nenhuma das opções dentro do limite de tentativas
    print('Acabou suas chances')
else:
    print('Você escolheu: ', escolha)