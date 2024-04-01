#Envio de Arquivos via SCP
#Instalar o paramiko - pip install paramiko

# 1 - Importa biblioteca
import paramiko

#CONEXÃO DO SSH

# 2 - Instanciar a Classe de Conexão do Paramiko
ssh = paramiko.SSHClient()

# 3 - Configuração do SSH, chave ou par de chave - o arquivo tem que estar na mesma pasta
ssh_key = paramiko.RSAKey.from_private_key_file(r"suachave.pem")

# 4 - Politica de CAceitação da Cheve
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 5 - Conexão do SSH com o Servidor Debian
ssh.connect("seuIP", username="admin", pkey=ssh_key)

#ACESSO ARQUIVOS
# 6 - Desligar o servidor remotamente:
stdin, stdout, stderr = ssh.exec_command('sudo init 0')

# 7 - Verificar se o comando foi executado com sucesso
if not stderr.read():
    print("Desligando servidor...")
else:
    print("Erro ao criar usuário.")

#Fechar conexões
ssh.close()
