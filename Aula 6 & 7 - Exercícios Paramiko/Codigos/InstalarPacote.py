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

# 6 - Executar comando para instalar o pacote
# stdin, stdout, stderr = ssh.exec_command(f'sudo apt-get install -y <pacote>')
# OBS: Se ocasionar em erro a instalação de qualquer pacote, atualize o sistema primeiro.
package_name = "git"
stdin, stdout, stderr = ssh.exec_command(f'sudo apt-get install {package_name} -y')

# 7 - Validar se o pacote foi instalado corretamente
if stderr.read():
    print(f"Pacote '{package_name}' instalado com sucesso.")
else:
    print(f"Erro ao instalar o pacote '{package_name}'.")

ssh.close()