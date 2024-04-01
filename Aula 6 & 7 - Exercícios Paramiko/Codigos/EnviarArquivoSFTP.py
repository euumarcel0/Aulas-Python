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

# 6 - Criar/abrir objeto/classe para o SFTP:
sftp = ssh.open_sftp()

# 7 - Definir arquivo remoto e diretorio de destino
local_file_path = "teste.txt" # Nome do arquivo local ou diretório no qual o arquivo está.
remote_dir = "/home/admin" # Diretório que você deseja que o arquivo seja enviado

# 8 - Copiar arquivo local para dentro da máquina:
sftp.put(local_file_path, f"{remote_dir}/teste.txt")

print(f"Arquivo '{local_file_path}' copiado para '{remote_dir}'.")

sftp.close()
ssh.close()