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
# 6 - Abrir / Criar - Como trabalhar com os objetos
scp = ssh.open_sftp()

# 7 - Defini o arquivo remoto
arquivolocal = r"C:...\teste.txt"
diretorio_remoto = "/home/admin"

# 8 - Copiar arquivo local para diretorio remoto do Debian
scp.put(arquivolocal, f"{diretorio_remoto}/teste.txt")

print (f"Arquivo '{arquivolocal}' copiado para '{diretorio_remoto}'.")

#Fechar conexões
scp.close()
ssh.close()