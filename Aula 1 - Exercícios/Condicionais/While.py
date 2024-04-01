# Número a ser adivinhado
numero_secreto = 42

# Loop para adivinhar o número
while True:
    # Solicita ao usuário um palpite
    palpite = int(input("Adivinhe o número secreto (entre 1 e 100): "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns, você acertou o número secreto!")
        break  # Sai do loop se o palpite estiver correto
    else:
        print("Tente novamente!")  # Mensagem de tentativa incorreta