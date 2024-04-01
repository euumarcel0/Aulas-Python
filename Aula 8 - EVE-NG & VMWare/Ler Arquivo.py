import telnetlib

# Função para ler os comandos do arquivo de configuração e armazená-los em uma lista
def ler_arquivo_configuracao(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        comandos = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista
    return comandos

# Função para conectar ao switch via Telnet e executar os comandos
def executar_comandos_telnet(hostname, username, password, comandos):
    # Inicia uma nova conexão Telnet
    tn = telnetlib.Telnet(hostname)
    
    # Aguarda a solicitação do nome de usuário
    tn.read_until(b"Username: ")
    # Envia o nome de usuário
    tn.write(username.encode('ascii') + b"\n")
    
    # Aguarda a solicitação da senha
    tn.read_until(b"Password: ")
    # Envia a senha
    tn.write(password.encode('ascii') + b"\n")
    
    # Itera sobre os comandos e os envia um por um
    for comando in comandos:
        tn.write(comando.encode('ascii') + b"\n")
    
    # Adiciona o comando para sair da sessão Telnet
    tn.write(b"exit\n")
    
    # Exibe a saída do switch após a execução dos comandos
    print(tn.read_all().decode('ascii'))

# Configurações de conexão Telnet
hostname = "endereco_do_switch"  # Endereço IP do switch Cisco
username = "seu_usuario"  # Nome de usuário para autenticação Telnet
password = "sua_senha"  # Senha para autenticação Telnet

# Nome do arquivo contendo os comandos de configuração
arquivo_configuracao = "configuracao_switch.txt"

# Chama a função para ler os comandos do arquivo de configuração
comandos = ler_arquivo_configuracao(arquivo_configuracao)

# Chama a função para executar os comandos via Telnet
executar_comandos_telnet(hostname, username, password, comandos)
