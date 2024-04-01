# 1 - Importar biblioteca do paramiko
import paramiko

# 2 - Instanciar a classe paramiko
ssh = paramiko.SSHClient()

# 3 - Configurar chave SSH, substituir "path_da_key" pelo caminho da chave SSH
# ssh_key = paramiko.RSAKey.from_private_key_file(path_da_key)
ssh_key = paramiko.RSAKey.from_private_key_file("suachave.pem")

# 4 - Politica de aceitação de chaves (não recomendado em produção)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 5 - Conectar-se ao servidor
# ssh.connect(server_ip, username=usuario_do_server, pkey=<variavel_que_contem_a_chave_ssh_configurada>)
ssh.connect("seuIP", username="admin", pkey=ssh_key)


# 6 - Definir usuario e senha
new_password = "senhasegura123"
new_username = "user"

# 7 - Definir comando
command = f'sudo useradd -m -p $(openssl passwd -1 {new_password}) {new_username}'

# 8 - Executar comando
stdin, stdout, stderr = ssh.exec_command(command)

# 9 - Verificar se o comando foi executado com sucesso
if not stderr.read():
    print(f"Usuário '{new_username}' criado com sucesso.")
else:
    print("Erro ao criar usuário.")

ssh.close()