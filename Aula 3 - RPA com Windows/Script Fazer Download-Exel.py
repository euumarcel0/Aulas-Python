import pyautogui # Manipular Mouse, Teclado e Tela
import pyperclip # Copiar e Colar Texto
import time


#Entre um comando e outro ele aguarda 1 segundo
pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto

# Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#Esperar 5 segundos
time.sleep(5)

# Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
pyautogui.click(x=201, y=354, clicks=2)
time.sleep(2)

# Passo 3: Fazer o download da base de vendas
pyautogui.click(x=201, y=354) # clicar no arquivo
time.sleep(2)
#pyautogui.click(x=3288, y=411) # clicar nos 3 pontinhos
pyautogui.click(x=1601, y=154) # clicar no fazer download
time.sleep(5) # esperar o download acabar

# Passo 4: Importar a base de vendas pro Python
import pandas as pd

tabela = pd.read_excel(r"C:\Users\administrator\Downloads\Vendas - Dez.xlsx")
display(tabela)

# Passo 5: Calcular os indicadores da empresa
faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)

# Passo 6: Enviar um e-mail para a diretoria com os indicadores de venda

# abrir aba
pyautogui.hotkey("ctrl", "t")

# entrar no link do email - https://mail.google.com/mail/u/0/#inbox
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=151, y=254)

# preencher as informações do e-mail
pyautogui.write("danilo.sibov@gmail.com")
pyautogui.press("tab") # selecionar o email

pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: locale.currency(faturamento, grouping=True)}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Danilo Sibov
"""

# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")