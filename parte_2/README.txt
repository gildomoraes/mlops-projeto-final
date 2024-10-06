Para a criação do container na máquina virtual, foi seguido os seguintes passos:

0. Instalar Docker Engine

# Atualiza lista de pacotes dos repositórios
sudo apt-get update

# Instala o Docker
sudo apt install docker.io

# Inicia o Serviço do Docker
sudo systemctl start Docker

# Verifica a versão do Docker
docker --version

# Automatiza o Início como Serviço
sudo systemctl enable Docker

# Verifique se o Docker está funcionando corretamente
sudo docker run hello-world

1. Criação da Imagem para o Servidor

# Extração da Imagem para a Máquina
git clone https://github.com/gildomoraes/mlops-projeto-final.git

# Seleção da Pasta (Entrar no Diretório)
cd mlops-projeto-final/parte_2

# Construir a Imagem Docker
sudo docker build -t platserver -f Dockerfile .

# Para consultar se sua imagem está “bem criada”, basta digitar:
sudo docker images

2. Colocar o Container Preditor em Execução

# Criar uma rede que será compartilhada entre todos os conteineres
sudo docker network create plat_network

# Para consultar as redes existente
sudo docker network ls

# Rodar o container baseado na imagem
sudo docker run -d --network plat_network -p 10001:8080 --restart always --name serving01 platserver python servingmodel.py model.joblib 8080

# Para consultar a criação do container
sudo docker ps

3. Colocar o Container Gerenciador em Execução

# Gestor JSON para extrair as informações
bash geraconfig.sh

# Rodar o container baseado na imagem
sudo docker run -d --network plat_network -p 443:8080 --restart always -v $(pwd)/config:/myServer/config -v $(pwd)/Log:/myServer/Log --name modelmanager platserver python modelmanager.py

# Para consultar a criação do container
sudo docker ps

# Consultar a rede
sudo docker network inspect plat_network

# Para parar os containers
sudo docker stop <container_id>

# Para visualizar os containers ativos e não
sudo docker ps -a

# para Remover os containers
sudo docker rm <container_id>

# Para remover diretórios
rm -rf <nome repositório>