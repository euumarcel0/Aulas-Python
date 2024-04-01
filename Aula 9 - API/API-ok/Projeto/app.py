# Programa Equipamentos 0.1
# 1 - Rodar Script no equipamento
# 2 - Fazer backup
# 3 - Reiniciar equipamento
# 4 - Executar um comando no equipamento
# 5 - Criar um usuário no equipamento
# 6 - Exibir as configurações do equipamento
# 7 - Configurar Banner
# 8 - Voltar ao Menu anterior
# 0 - Sair

# Importar Bibliotecas
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import time
from netmiko import ConnectHandler

# import API
app = Flask(__name__)
api = Api(app)
CORS(app)

# Função para limpar a tela do console
def clear():
    os.system('cls')

# Função para conectar-se ao equipamento Cisco
def Conectar(ip, username, password):
    try:
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
        }
        connection = ConnectHandler(**device)
        print(f"> Conexão com o equipamento {ip} estabelecida com sucesso!")
        return connection
    except Exception as e:
        print(f"> Erro ao conectar-se ao equipamento {ip}: {e}")
        return None

# Função para exibir o menu principal
def iniciar_menu():
    while True:
        print("Selecione uma opção digitando o seu respectivo número")
        print("<>=====MENU=====<>")
        print("1 - Rodar script no equipamento")
        print("2 - Fazer Backup")
        print("3 - Executar um comando no equipamento")
        print("4 - Criar um usuário no equipamento")
        print("5 - Exibir configurações atuais do equipamento")
        print("6 - Configurar Banner")
        print("7 - Voltar ao Menu anterior")
        print("0 - Sair")
        print("<>=====MENU=====<>")
        opcao = input("OPÇÃO: ")
        if opcao == "0":
            print("Saindo do programa")
            exit(0)
        elif opcao == "1":
            print("> Rodar um script no equipamento")
            equipamento = selecionar_equipamento()
            if equipamento == "Switch":
                print("\n", rodar_script(switch_connection))  # Chama a função para rodar um script no switch
            elif equipamento == "Roteador":
                print("\n", rodar_script(router_connection))  # Chama a função para rodar um script no roteador
            voltar_ao_menu_principal()
        elif opcao == "2":
            print("> Fazer backup do equipamento Cisco")
            equipamento = selecionar_equipamento()
            if equipamento == "Switch":
                print("\n", fazer_backup(switch_connection))  # Chama a função para fazer backup no switch
            elif equipamento == "Roteador":
                print("\n", fazer_backup(router_connection))  # Chama a função para fazer backup no roteador
            voltar_ao_menu_principal()
        elif opcao == "3":
            print("> Executar um comando e exibir últimas configurações")
            equipamento = selecionar_equipamento()
            comando = input("> Digite o comando que deseja executar: ")
            if equipamento == "Switch":
                resultado = enviar_comando(switch_connection, comando)  # Chama a função para enviar um comando para o switch
            elif equipamento == "Roteador":
                resultado = enviar_comando(router_connection, comando)  # Chama a função para enviar um comando para o roteador
            print("\n", resultado)
            voltar_ao_menu_principal()
        elif opcao == "4":
            print("> Criar um usuário no equipamento")
            equipamento = selecionar_equipamento()
            if equipamento == "Switch":
                print("\n", criar_usuario(switch_connection))  # Chama a função para criar um usuário no switch
            elif equipamento == "Roteador":
                print("\n", criar_usuario(router_connection))  # Chama a função para criar um usuário no roteador
            voltar_ao_menu_principal()
        elif opcao == "5":
            print("> Exibir últimas configurações do equipamento Cisco: ")
            equipamento = selecionar_equipamento()
            if equipamento == "Switch":
                print("\n", exibir_ultimas_configuracoes(switch_connection))  # Chama a função para exibir as últimas configurações do switch
            elif equipamento == "Roteador":
                print("\n", exibir_ultimas_configuracoes(router_connection))  # Chama a função para exibir as últimas configurações do roteador
            voltar_ao_menu_principal()
        elif opcao == "6":
            print("> Configurar banner de mensagem no equipamento Cisco")
            equipamento = selecionar_equipamento()
            if equipamento == "Switch":
                print("\n", configurar_banner_cisco(switch_connection))  # Chama a função para configurar o banner no switch
            elif equipamento == "Roteador":
                print("\n", configurar_banner_cisco(router_connection))  # Chama a função para configurar o banner no roteador
            voltar_ao_menu_principal()
        elif opcao == "7":
            print("Selecionar outro equipamento...")
            voltar_para_selecao_equipamento()
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

# Função 1 para rodar script - Envia um arquivo de script local para o equipamento Cisco
def rodar_script(connection, script_path=None, comandos=None):
    try:
        if script_path:
            # Verifica se o arquivo existe
            if not os.path.isfile(script_path):
                return {"error": f"Erro: Arquivo '{script_path}' não encontrado."}

            # Lendo o conteúdo do arquivo de script local linha por linha
            with open(script_path, 'r') as f:
                script_content = f.readlines()

            # Enviando cada linha do arquivo de script para o equipamento via SSH
            response_formatted = []
            for line in script_content:
                output = connection.send_config_set(line.strip(), exit_config_mode=False)
                response_formatted.extend(output.splitlines()) # Adicionando a saída formatada

            time.sleep(2) # Aguarda um pouco após o envio do script

            return {
                "resultado": {
                    "Mensagem": f"Script '{script_path}' enviado para o equipamento.",
                    "Resposta": response_formatted
                }
            }
        
        elif comandos:
            # Enviando os comandos para o equipamento via SSH
            output = connection.send_config_set(comandos.split(';'))
            time.sleep(2)

            # Formatando a saída em uma lista de comandos e respostas
            response_formatted = output.splitlines() # Dividindo a saída em linhas
            return {
                "Resultado": {
                    "Mensagem": "Comandos enviados para o equipamento.",
                    "Resposta": response_formatted
                }
            }
        
        else:
            return {"error": "Nenhum script ou comando fornecido."}
    
    except Exception as e:
        return {"error": f"Erro ao rodar o script: {e}"}

# Função 2 para fazer backup - Faz um backup do equipamento Cisco e salva localmente no computador Windows
def fazer_backup(connection):
    try:
        output = connection.send_command("show running-config")
        nome_arquivo = input("> Nome do arquivo de backup: ")
        with open(nome_arquivo, "w") as output_file:
            output_file.write(output)
        return { "Mensagem": f"Backup do equipamento salvo em '{nome_arquivo}' com sucesso"}
    except Exception as e:
        return {"Erro": f"Erro ao fazer backup: {e}"}

# Função 3 para enviar comando - Executa um comando e retorna o resultado
def enviar_comando(connection, comando):
    try:
        output = connection.send_command(comando, expect_string=r"#")  # Definindo o padrão esperado como o prompt de execução do comando
        output_lines = output.splitlines()[-4:]  # Pegando as últimas três linhas da saída
        result = "\n" .join(output_lines) if output_lines else "Nenhuma saída disponível."
        
        # Dividindo a saída em linhas e retornando como uma lista no JSON
        output_lines = result.splitlines()
        return {
            "Mensagem": f"Comando '{comando}' executado com sucesso.",
            "Resultado": output_lines
        }
    except Exception as e:
        return {"Erro": f"Erro ao executar o comando '{comando}': {e}"}

# Função 4 para criar usuário no equipamento Cisco
def criar_usuario(connection):
    try:
        usuario = input("> Digite o nome do novo usuário: ")
        senha = input("> Digite a senha do novo usuário: ")
        connection.send_config_set([f"username {usuario} privilege 15 password {senha}", "write memory"])

        # Adicionando a listagem de usuários existentes
        usuarios_existentes = connection.send_command("show running-config | include username")
        usuarios_existentes_lines = usuarios_existentes.splitlines()  # Dividindo a saída em linhas
        return {
            "Mensagem": f"Usuário '{usuario}' criado com sucesso.",
            "Usuários existentes": usuarios_existentes_lines  # Retornando as linhas individualmente
        }
    except Exception as e:
        return {"Erro": f"Erro ao criar usuário: {e}"}

# Função 5 para exibir configurações atuais do equipamento Cisco
def exibir_ultimas_configuracoes(connection):
    try:
        output = connection.send_command("show running-config")
        output_lines = output.splitlines()  # Dividindo a saída em linhas
        return {
            "Mensagem": "Últimas configurações do equipamento Cisco:",
            "Configurações Atual": output_lines
        }
    except Exception as e:
        return {"Erro": f"Erro ao exibir configurações: {e}"}

# Função 6 para configurar banner de mensagem no equipamento Cisco
def configurar_banner_cisco(connection):
    try:
        tipo_banner = input("Selecione o tipo de banner:\n1 - MOTD (Message of the Day)\n2 - Login\n3 - Exec\nOpção: ")
        if tipo_banner == "1":
            tipo_banner_texto = "motd"
        elif tipo_banner == "2":
            tipo_banner_texto = "login"
        elif tipo_banner == "3":
            tipo_banner_texto = "exec"
        else:
            return {"error": "Opção inválida. Por favor, selecione 1, 2 ou 3."}

        mensagem = input("> Digite a mensagem do banner: ")
        output = connection.send_config_set([f"banner {tipo_banner_texto} #{mensagem}#", "write memory"])
        return {
            "Mensagem": f"Banner {tipo_banner_texto.upper()} configurado com sucesso com a mensagem:",
            "Banner": mensagem.splitlines()  # Dividindo a mensagem em linhas
        }
    except Exception as e:
        return {"Erro": f"Erro ao configurar banner: {e}"}

# Função para voltar ao menu principal
def voltar_ao_menu_principal():
    input("\nPressione ENTER para voltar ao menu principal...")
    os.system('cls')

# Função Menu Postman
def Menu_postman():
    return {
        "menu": { 
            "Defina o equipamento em seguida a opção desejada: ": "Switch ou Roteador",
            "1": "rodar_script",
            "2": "fazer_backup",
            "3": "enviar_comando",
            "4": "criar_usuario",
            "5": "exibir_ultimas_configuracoes",
            "6": "configurar_banner_cisco"
        }
    }
    
# Função para o menu de seleção de equipamento
def selecionar_equipamento():
    while True:
        clear()
        print("<>=====MENU DE SELEÇÃO=====<>")
        print("Selecione o equipamento para configurar:")
        print("1 - Switch")
        print("2 - Roteador")
        print("0 - Sair")
        print("<>=====MENU DE SELEÇÃO=====<>")
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

# Função para voltar para seleção de equipamento
def voltar_para_selecao_equipamento():
    input("\nPressione ENTER para selecionar outro equipamento...")
    return

if __name__ == "__main__":
    # Definindo informações de conexão
    ip_switch = "10.1.1.230"
    username_switch = "admin"
    password_switch = "Its00"
    ip_router = "10.1.1.191"
    username_router = "admin"
    password_router = "Its00"

    # Conectar-se aos dispositivos
    switch_connection = Conectar(ip_switch, username_switch, password_switch)
    router_connection = Conectar(ip_router, username_router, password_router)
    os.system('cls')

# Dicionário que mapeia opções do menu para funções correspondentes
menu_options = {
    "1": rodar_script,
    "2": fazer_backup,
    "3": enviar_comando,
    "4": criar_usuario,
    "5": exibir_ultimas_configuracoes,
    "6": configurar_banner_cisco,
    "menu": Menu_postman
}

# Função para executar a opção selecionada do menu
def executar_opcao(opcao, connection, comando=None):
    if opcao == "menu":
        return Menu_postman()
    if opcao == "1":
        return rodar_script(connection)
    elif opcao == "2":
        return fazer_backup(connection)  
    elif opcao == "3":
        comando = input("> Digite o comando desejado: ")
        return enviar_comando(connection, comando)
    elif opcao == "4":
        return criar_usuario(connection)
    elif opcao == "5":
        return exibir_ultimas_configuracoes(connection)
    elif opcao == "6":
        return configurar_banner_cisco(connection)
    else:
        return {"error": "Opção inválida. Por favor, selecione uma opção existente."}    

# Função principal para lidar com requisições da API
class RodarScript(Resource):
    def post(self):
        data = request.get_json()
        opcao = data['opcao']
        connection = None
        if opcao == "menu":
            return {'result': executar_opcao(opcao, connection)}
        else:
            equipamento = data.get('equipamento')
            connection = None
            if equipamento == "Switch":
                connection = switch_connection
            elif equipamento == "Roteador":
                connection = router_connection

            if connection:
                return {'result': executar_opcao(opcao, connection)}
            else:
                return {'error': 'Equipamento não reconhecido'}, 400

# Adicionando a rota para rodar o script
api.add_resource(RodarScript, '/executar')

# Adicione suas rotas de API aqui...
@app.route('/roteador')
def roteador():
    return render_template('Roteador.html')

@app.route('/switch')
def switch():
    return render_template('Switch.html')


if __name__ == '__main__':
    app.run(debug=True)
