Para a criação do container na máquina local, foi seguido os seguintes passos:

1. Construir a Imagem Docker
docker build -t modelo-inadimplencia .

2. Rodar o Contêiner
docker run -p 5000:5000 modelo-inadimplencia



