# Importa as funções necessárias do módulo pyinputplus
from pyinputplus import inputNum, inputURL, inputEmail, inputMenu, inputChoice, RetryLimitException

# Aceita somente um Email válido
email = inputEmail(prompt='Digite seu Email: ')

# Aceita somente um número inteiro
numero = inputNum(prompt='Digite um número: ')

# Aceita somente um URL válida
url = inputURL(prompt='Digite uma URL: ')

# Lista de opções para o menu
opcoes = ['Roteador', 'Switch', 'Linux', 'Sair']

# Cria um menu numerado
item_menu = inputMenu(opcoes, numbered=True, prompt='Escolha uma opção: \n')

# Cria um menu com limite de tentativas
try:
    numeros = ['1', '2', '3', '4']
    escolha = inputChoice(numeros, limit=2, prompt='Escolha um número entre 1 a 4: \n')
except RetryLimitException:
    # Se o usuário não escolher nenhuma das opções dentro do limite de tentativas
    print('Acabou suas chances')
else:
    print('Você escolheu: ', escolha)