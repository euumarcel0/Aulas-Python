import webbrowser
import time
import pyautogui
import pyperclip

# Definir destinatário e assunto
email = "eumarcelomesquita@gmail.com"
assunto = "Configuração de Rede"

# Abrir uma nova guia no navegador padrão
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)  # Aguardar um pouco para a página carregar

# Clicar no botão escrever (você pode ajustar as coordenadas conforme necessário)
pyautogui.click(x=151, y=254)
pyautogui.press("tab")

# Preencher informações do email
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Carregar conteúdo do arquivo de configuração de rede
with open("configuracao_rede.txt", "r", encoding="utf-8") as arquivo:
    conteudo_arquivo = arquivo.read()

# Formatar mensagem
texto = f"""
Prezados,

Segue as configurações do sistema:

## Conteúdo do arquivo:

{conteudo_arquivo}

Qualquer dúvida estou à disposição.

Atenciosamente,
Seu Nome
"""

# Enviar email
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")