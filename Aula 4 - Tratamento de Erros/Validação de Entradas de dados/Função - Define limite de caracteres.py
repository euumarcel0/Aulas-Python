def validar_tamanho(texto, maximo):
    """Valida se o tamanho do texto não excede o máximo permitido."""
    if len(texto) > maximo:
        print(f"O texto deve conter no máximo {maximo} caracteres!")
    else:
        return True

while True:
    texto = input("Informe um texto de no máximo 20 caracteres: ")
    # Chama a função validar_tamanho para verificar se o texto não excede 20 caracteres
    if validar_tamanho(texto, 20):
        break  # Sai do loop se o texto for válido