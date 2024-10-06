Para a criação do container na máquina virtual, foi seguido os seguintes passos:

1. Criação da Imagem para o Servidor

# Extração da Imagem para a Máquina
#git clone https://github.com/elthonf/plataformas-cognitivas-docker.git
git clone https://github.com/gildomoraes/mlops-projeto-final.git

# Seleção da Pasta (Entrar no Diretório)
#cd plataformas-cognitivas-docker/
cd mlops-projeto-final/parte_2

# Construir a Imagem Docker
#sudo docker build -t platserver -f dockerbuilds/DockerServer.txt .
sudo docker build -t platserver -f DockerFile .

# Para consultar se sua imagem está “bem criada”, basta digitar:
sudo docker images

2. Colocar o Container Preditor em Execução

# Criar uma rede que será compartilhada entre todos os conteineres
sudo docker network create plat_network

# Para consultar as redes existente
sudo docker network ls

# Rodar a Imagem
# sudo docker run -d --network plat_network -p 10001:8080 --restart always --name serving01 platserver python servingmodel.py models/modelo.joblib 8080
sudo docker run -d --network plat_network -p 10001:8080 --restart always --name serving01 platserver python serving.py model.joblib 8080

# Para consultar a criação do container
sudo docker ps


3. Colocar o Container Gerenciador em Execução

# Gestor JSON para extrair as informações
bash geraconfig.sh

# Rodar a Imagem
sudo docker run -d --network plat_network -p 443:8080 --restart always -v $(pwd)/config:/myServer/config -v $(pwd)/Log:/myServer/Log --name modelmanager platserver python modelmanager.py

# Para consultar a criação do container
sudo docker ps

# Consultar a rede
sudo docker network inspect plat_network