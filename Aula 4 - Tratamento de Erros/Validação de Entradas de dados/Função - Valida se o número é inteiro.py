def validar_faixa(numero, inicio, fim):
    """Valida se um número está dentro de uma faixa específica."""
    if numero.isdigit():  # Verifica se a entrada é um número inteiro
        if int(inicio) <= int(numero) <= int(fim):
            return True  # Retorna True se o número estiver dentro da faixa
        else:
            # Se o número estiver fora da faixa, imprime uma mensagem de erro
            print(f"Valor inválido! Informe um número inteiro entre {inicio} e {fim}.")
    else:
        # Se a entrada não for um número inteiro, imprime uma mensagem de erro
        print(f"Número inválido! '{numero}' não é um número inteiro. Informe um número inteiro entre {inicio} e {fim}.")

# Loop para solicitar um número válido ao usuário
while True:
    resposta = input("Informe um número inteiro entre 1 e 100: ")
    # Chama a função validar_faixa para verificar se o número está entre 1 e 100
    if validar_faixa(resposta, 1, 100):
        break  # Sai do loop se o número for válido
    else:
        print("Por favor, insira um número inteiro válido.")

print("Número válido inserido com sucesso!")