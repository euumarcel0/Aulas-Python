#Programa Suporte 0.3
# INSTRUÇÕES:
# 1 - Enviar um arquivo para o servidor remoto
# 2 - Pegar um arquivo do servidor remoto 
# 3 - Reiniciar servidor remoto 
# 4 - Desligar servidor remoto 
# 5 - Criar usuário
# 6 - Exibir informações do sistema operacional
# 7 - Instalar qualquer pacote no servidor remoto
# 0 - Sair

#Instalação do paramiko
#pip install paramiko

# 1 - Importação de Bibliotecas
import paramiko
import os
import time

# 2 - Instanciar a Classe de Conexão do Paramiko
ssh = paramiko.SSHClient()

# 3 - Função - Limpar comandos do sistema
def clear():
    os.system ('cls')

# 4 - Função - Enviar Arquivo - Origem Windows - Destino Linux
def enviar_arquivo():
    # Abrir / Criar - Como trabalhar com os objetos
    scp = ssh.open_sftp()

    # Definir o arquivo local - Ex.: C:\Users\Administrator\Desktop\Curso\Aula 6\arquivoteste.txt
    arquivolocal = input("> arquivo que deseja enviar: ")

    # Definir o diretorio remoto que o usuário tenha direito - Ex.: root ou admin /root 
    diretorio_remoto = input("> caminho de destino: ")

    # Definir nome do arquivo remoto novoaquivo.txt
    nome_arquivo_remoto = input("> nome do arquivo no destino: ")

    #Função Put para enviar arquivos
    scp.put(arquivolocal, f"{diretorio_remoto}/{nome_arquivo_remoto}")

    #Fechar conexão
    scp.close()
    return f"> arquivo '{arquivolocal}' copiado para '{diretorio_remoto}/{nome_arquivo_remoto}'."

# 5 - Função - Pegar Arquivo
def pegar_arquivo():
    # Abrir / Criar - Como trabalhar com os objetos
    scp = ssh.open_sftp()

    # Definir o diretorio remoto com o nome do arquivo
    arquivo_remoto = input("Informe o diretorio remoto, ex.:/home/admin/novoarq.txt: ")
    # Definir o arquivo local
    diretorio_local = input("Informe o diretorio que deseja salvar o arquivo: ")

    # Verificar se o diretório local existe
    if not os.path.exists(diretorio_local):
        return f"O diretório local '{diretorio_local}' não foi encontrado."

    # Variavél do nome do arquivo que será usada no próximo comando de cópia
    # Extraida do caminho e arquivo remoto
    nome_arquivo = os.path.basename(arquivo_remoto)

    # Copiar arquivo remoto para diretorio local
    scp.get(arquivo_remoto, os.path.join(diretorio_local, nome_arquivo))

    # Fechar conexão
    scp.close()
    return f"> Arquivo '{arquivo_remoto}' copiado para '{os.path.join(diretorio_local, nome_arquivo)}'."

# 6 - Função - Reiniciar servidor remoto
def reiniciar_servidor():
    # stdin = Entradas do log do comando
    # stdout = Saidas do log do comando
    # stderr = Erros do log do comando
    # ssh.exec_command - Executa o comando que eu quero
    stdin, stdout, stderr = ssh.exec_command('sudo reboot')
    #Esperar 1 minuto por ser na nuvem AWS
    print ("Contar tempo 1 minuto e 10 segundos.")
    time.sleep(70)#time é definido em segundos
    #Verifica de o comando teve algum erro
    if not stderr.read():# Se não tiver erro - Reiniciar
        #Restabelecer conexão após 1 minuto e 10 segundos
        ssh.connect(instance_ip, username=username, password=senha)
        return "> O Servidor foi reiniciado! A conexão do Programa Suporte foi restabelecida!"
    else: # Se  tiver algum erro - Não vai Reiniciar
        return "> Erro ao reiniciar o servidor!"
    
# 7 - Função - Desligar servidor remoto
def desligar_servidor():
    # stdin = Entradas do log do comando
    # stdout = Saidas do log do comando
    # stderr = Erros do log do comando
    # ssh.exec_command - Executa o comando que eu quero
    stdin, stdout, stderr = ssh.exec_command('sudo init 0')

    #Verifica de o comando teve algum erro
    if not stderr.read():# Se não tiver erro - Desliga Servidor e sai do programa - A mensagem esta dentro do Menu
        return exit(0)
    else:# Se encontrar algum erro - Não vai Desligar
        return "> Erro ao desligar o servidor!"

# 8 - Função - Criar usuário
def criar_usuario():
    usuario = input ("> Digite o nome do novo usuário: ")
    senha = input ("> Digite a senha do novo usuário: ")
    comando = f'sudo useradd -m -p $(openssl passwd -1 {senha}) {usuario}'

    # stdin = Entradas do log do comando
    # stdout = Saidas do log do comando
    # stderr = Erros do log do comando
    # ssh.exec_command - Executa o comando que eu quero 
    stdin, stdout, stderr = ssh.exec_command(comando)

    # Certifique-se de que todos os buffers estejam esvaziados
    stderr.channel.recv_exit_status()

    # Captura a saída de erro e a saída padrão
    error = stderr.read().decode("utf-8")
    output = stdout.read().decode("utf-8")
    
    if error:
        return f"> ERRO ao criar o usuário '{usuario}': {error}"
    # Se houver saída padrão, pode ser uma mensagem informativa
    elif output:
        return f"> Mensagem de criação do usuário '{usuario}': {output}"
    # Se não houver erro nem saída padrão, assume-se que o usuário foi criado com sucesso
    else:
        return f"> Usuário '{usuario}' criado com sucesso."
    
# 9 - Função - Exibir informações do sistema operacional
def exibir_sistema_operacional():
    system_info = {}
    #Busca info Memória
    stdin, stdout, stderr = ssh.exec_command('free -h |grep Gi')
    info_memoria = stdout.read().decode('utf-8')
    system_info["INFO MEMORIA"] = info_memoria

    #Busca info Disco
    stdin, stdout, stderr = ssh.exec_command('sudo fdisk -l |grep "Disk /"')
    info_disco = stdout.read().decode('utf-8')
    system_info["INFO DISCO"] = info_disco

    #Busca info CPU
    stdin, stdout, stderr = ssh.exec_command('cat /proc/cpuinfo |grep -E "processor|model name"')
    info_cpu = stdout.read().decode('utf-8')
    system_info["INFO CPU"] = info_cpu

    #Busca info Sistema Operacional
    stdin, stdout, stderr = ssh.exec_command('cat /etc/issue')
    info_so = stdout.read().decode('utf-8')
    system_info["INFO SO"] = info_so

    return system_info

# 10 - Função - Instalar qualquer pacote no servidor remoto
def instalar_pacote():
    #Variavel com nome do pacote a ser instalado
    nome_pacote = input ("> Informe o nome do pacote: ")
    #Executo a instalação do pacote com root
    verifica_comando = f'apt list --installed | grep -w {nome_pacote}'
    stdin_check, stdout_check, stderr_check = ssh.exec_command(verifica_comando)

    # Captura a saída padrão para verificar se o pacote está instalado
    output_check = stdout_check.read().decode("utf-8")

    # Verifica se o pacote está na lista de pacotes instalados
    if nome_pacote in output_check:
        return f"> O pacote '{nome_pacote}' já está instalado."

    # Caso o pacote não esteja instalado, procede com a instalação
    else:
        # Atualiza a lista de pacotes antes de tentar instalar um novo pacote
        stdin_update, stdout_update, stderr_update = ssh.exec_command('sudo apt update')
        # Aguarda a execução do comando ser concluída
        stdout_update.channel.recv_exit_status()

        # Comando para instalar o pacote com a opção -y para evitar interação
        command_install = f'sudo apt install {nome_pacote} -y'
        stdin_install, stdout_install, stderr_install = ssh.exec_command(command_install)

        # Aguardar até que o comando termine de ser executado
        stdout_install.channel.recv_exit_status()

        # Verifica se ocorreu algum erro durante a instalação
        error_install = stderr_install.read().decode("utf-8")
        if error_install:
            return f"> Erro ao instalar o pacote: '{nome_pacote}', '{erro_install}'"
        else:
            return f"> O pacote '{nome_pacote}' foi instalado com sucesso."

    
# Função Menu do Progrmaa de Suporte
def menu():
    clear() #Limpar a tela
    #exibir o menu de opções
    print("Selecione uma opção digitando o seu respectivo número")
    print("<>=====MENU=====<>")
    print("1 - Enviar um arquivo para o servidor remoto")
    print("2 - Pegar um arquivo do servidor remoto")
    print("3 - Reiniciar servidor")
    print("4 - Desligar servidor")
    print("5 - Criar um usuário")
    print("6 - Exibir informações do sistema operacional")
    print("7 - Instalar qualquer pacote no servidor remoto")
    print("0 - Sair")
    print("<>=====MENU=====<>")
    numero = input("OPÇÃO: ")
    if numero == "0":
        print("Saindo do programa")
        exit(0)
    return numero

#Função do Menu - Programa Suporte
def start_menu():
    while True:
        opcao = menu()
        if opcao == "1":
            print("> Enviar um arquivo")
            print("\n", enviar_arquivo())
            input("\nPressione ENTER para continuar...")
        elif opcao == "2":
            print("> Pegar um arquivo")
            print("\n", pegar_arquivo())
            input("\nPressione ENTER para continuar...")
        elif opcao == "3":
            print("> Reiniciando servidor")
            print("\n", reiniciar_servidor())
            input("\nPressione ENTER para continuar...")
        elif opcao == "4":
            print("> Desligando servidor e Saindo do Programa!")
            print("\n", desligar_servidor())
        elif opcao == "5":
            print("> Criar um usuário")
            print("\n", criar_usuario())
            input("\nPressione ENTER para continuar...")
        elif opcao == "6":
            print("> Informações do Sistema operacional: ")
            print("\n", exibir_sistema_operacional())
            input("\nPressione ENTER para continuar...")
        elif opcao == "7":
            print("> Instalar um pacote no servidor")
            print("\n", instalar_pacote())
            input("\nPressione ENTER para continuar...")