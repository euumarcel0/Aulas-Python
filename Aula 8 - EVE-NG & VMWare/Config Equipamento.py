import telnetlib
import os
import time

# Função - Limpar comandos do sistema
def clear():
    os.system('cls')

# Função - Conectar-se ao equipamento Cisco
def connect_to_device(ip, username, password):
    try:
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.read_until(b"#").decode('utf-8')  # Aguarda o prompt de comando
        print(f"> Conexão com o equipamento {ip} estabelecida com sucesso!")
        return tn
    except Exception as e:
        print(f"> Erro ao conectar-se ao equipamento {ip}: {e}")
        return None

# Função - Menu Principal
def start_menu(tn):
    while True:
        clear()
        print("Selecione uma opção digitando o seu respectivo número")
        print("<>=====MENU=====<>")
        print("1 - Rodar script no equipamento")
        print("2 - Fazer Backup")
        print("3 - Reiniciar equipamento")
        print("4 - Executar um comando no equipamento")
        print("5 - Criar um usuário no equipamento")
        print("6 - Exibir últimas configurações do equipamento")
        print("7 - Configurar Banner")
        print("9 - Selecionar outro equipamento")
        print("0 - Sair")
        print("<>=====MENU=====<>")
        opcao = input("OPÇÃO: ")
        if opcao == "0":
            print("Saindo do programa")
            tn.write(b"exit\n")
            exit(0)
        elif opcao == "1":
            print("> Rodar um script no equipamento")
            print("\n", rodar_script(tn))
            voltar_ao_menu_principal()
        elif opcao == "2":
            print("> Fazer backup do equipamento Cisco")
            print("\n", fazer_backup(tn))
            voltar_ao_menu_principal()
        elif opcao == "3":
            print("> Reiniciando equipamento Cisco")
            print("\n", reiniciar_equipamento_cisco(tn))
            voltar_ao_menu_principal()
        elif opcao == "4":
            print("> Executar um comando e exibir últimas configurações")
            comando = input("> Digite o comando que deseja executar: ")
            resultado = enviar_comando(tn, comando)
            print("\n", resultado)
            print("\n", exibir_ultimas_configuracoes(tn, comando))
            voltar_ao_menu_principal()
        elif opcao == "5":
            print("> Criar um usuário")
            print("\n", criar_usuario(tn))
            voltar_ao_menu_principal()
        elif opcao == "6":
            print("> Exibir últimas configurações do equipamento Cisco: ")
            print("\n", exibir_ultimas_configuracoes(tn, "Último comando não disponível"))
            voltar_ao_menu_principal()
        elif opcao == "7":
            print("> Configurar banner de mensagem no equipamento Cisco")
            print("\n", configurar_banner_cisco(tn))
            voltar_ao_menu_principal()
        elif opcao == "9":
            print("Selecionar outro equipamento...")
            return
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

# Função - Rodar Script - Enviar arquivo de script local para o equipamento Cisco
def rodar_script(tn):
    print("Selecione uma opção:")
    print("1 - Enviar conteúdo de um arquivo TXT")
    print("2 - Digitar os comandos manualmente")
    opcao = input("Opção: ")

    if opcao == "1":
        diretorio_local = input("> Caminho local do arquivo de script: ")

        # Lendo o conteúdo do arquivo de script local
        with open(diretorio_local, 'r') as f:
            script_content = f.read()

        # Enviando o conteúdo do arquivo de script para o equipamento via Telnet
        tn.write(script_content.encode() + b"\n")

        return f"> Script '{diretorio_local}' enviado para o equipamento."
    elif opcao == "2":
        comandos = input("> Digite os comandos que deseja enviar (separados por ';' se mais de um): ")

        # Enviando os comandos para o equipamento via Telnet
        for comando in comandos.split(';'):
            tn.write(comando.strip().encode() + b"\n")

        return f"> Comandos digitados enviados para o equipamento."
    else:
        return "Opção inválida. Por favor, selecione '1' ou '2'."

# Função - Fazer Backup - Faz um backup do equipamento Cisco e salva localmente no computador Windows
def fazer_backup(tn):
    nome_arquivo = input("> Nome do arquivo de backup: ")
    tn.write(b"show running-config\n")
    backup_content = tn.read_until(b"#").decode('utf-8')
    with open(f"{nome_arquivo}.txt", 'w') as f:
        f.write(backup_content)
    return f"> Backup do equipamento Cisco feito com sucesso. Arquivo salvo como '{nome_arquivo}.txt'."

# Função - Reiniciar Equipamento Cisco
def reiniciar_equipamento_cisco(tn):
    tn.write(b"reload\n")
    tn.read_until(b"confirm").decode('utf-8')
    tn.write(b"\n")
    time.sleep(120)  # Espera 2 minutos após o reinício
    tn.read_until(b"System configuration has been modified. Save? [yes/no]: ").decode('utf-8')
    tn.write(b"no\n")
    time.sleep(10)  # Espera 10 segundos após não salvar a configuração
    tn.read_until(b"Press RETURN to get started!").decode('utf-8')
    return "> O equipamento Cisco foi reiniciado com sucesso."

# Função - Enviar Comando - Executa um comando e retorna o resultado
def enviar_comando(tn, comando):
    tn.write(comando.encode() + b"\n")
    resultado = tn.read_until(b"#").decode('utf-8')
    return f"> Comando '{comando}' executado com sucesso.\n\n{resultado}"

# Função - Criar usuário no equipamento Cisco
def criar_usuario(tn):
    usuario = input("> Digite o nome do novo usuário: ")
    senha = input("> Digite a senha do novo usuário: ")
    # Criar o usuário
    tn.write(f"username {usuario} privilege 15 password {senha}\n".encode())
    return f"> Usuário '{usuario}' criado com sucesso."

# Função - Exibir últimas configurações do equipamento Cisco
def exibir_ultimas_configuracoes(tn, ultimo_comando):
    try:
        # Envia o comando para mostrar as últimas configurações
        tn.write(b"show running-config\n")

        # Aguarda até obter a resposta completa
        time.sleep(5)  # Aumenta o tempo de espera para 5 segundos
        time.sleep(2)  # Aguarda mais 2 segundos para garantir que as informações estejam disponíveis
        resultado = tn.read_very_eager().decode('utf-8')

        # Dividindo o resultado em linhas
        linhas = resultado.split('\n')

        # Verifica se há mais linhas disponíveis além das já exibidas
        if len(linhas) > 5:
            # Pede ao usuário para pressionar ENTER para exibir mais linhas
            input("\nPressione ENTER para exibir mais 4 linhas das configurações...")

            # Exibe as próximas 4 linhas se houverem
            ultimas_configuracoes = '\n'.join(linhas[1:5])

            # Retorna as configurações e o último comando executado
            return f"> Último comando executado: {ultimo_comando}\n\nÚltimas configurações do equipamento Cisco:\n\n{ultimas_configuracoes}"
        else:
            # Se não houver mais linhas, retorna todas as linhas disponíveis
            ultimas_configuracoes = '\n'.join(linhas[1:])

            # Retorna as configurações e o último comando executado
            return f"> Último comando executado: {ultimo_comando}\n\nÚltimas configurações do equipamento Cisco:\n\n{ultimas_configuracoes}"
    except Exception as e:
        return f"Erro ao obter as últimas configurações do equipamento: {e}. Verifique a conexão e tente novamente."

# Função - Configurar banner de mensagem no equipamento Cisco
def configurar_banner_cisco(tn):
    mensagem = input("> Digite a mensagem do banner: ")

    # Configurar banner de mensagem
    tn.write(b"banner motd #\n")
    tn.write(mensagem.encode() + b"\n")
    tn.write(b"#\n")

    return f"> Banner configurado com sucesso com a mensagem:\n{mensagem}"

# Função - Voltar ao menu principal
def voltar_ao_menu_principal():
    input("\nPressione ENTER para voltar ao menu principal...")

# Função - Menu de seleção de equipamento
def selecionar_equipamento():
    while True:
        clear()
        print("<>=====MENU INICIAL=====<>")
        print("Selecione o equipamento para configurar:")
        print("1 - Switch")
        print("2 - Roteador")
        print("0 - Sair")
        print("<>=====MENU INICIAL=====<>")
        escolha = input("Escolha: ")
        if escolha == "0":
            print("Saindo do programa")
            exit(0)
        elif escolha == "1":
            return "Switch"
        elif escolha == "2":
            return "Roteador"
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

# Função - Voltar para seleção de equipamento
def voltar_para_selecao_equipamento():
    input("\nPressione ENTER para selecionar outro equipamento...")
    return

if __name__ == "__main__":
    # Definindo informações de conexão
    ip_switch = "10.1.1.59"
    username_switch = "admin"
    password_switch = "Its00"
    ip_router = "10.1.1.182"
    username_router = "admin"
    password_router = "Its00"

    # Conectar-se aos dispositivos
    switch_connection = connect_to_device(ip_switch, username_switch, password_switch)
    router_connection = connect_to_device(ip_router, username_router, password_router)

    # Iniciar menu para seleção de equipamento
    while True:
        equipamento = selecionar_equipamento()
        if equipamento == "Switch":
            start_menu(switch_connection)
        elif equipamento == "Roteador":
            start_menu(router_connection)
        voltar_para_selecao_equipamento()