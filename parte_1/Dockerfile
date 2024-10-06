# Usar a imagem base do Python
FROM python:3.9

LABEL maintainer="gildofmneto@gmail.com"
LABEL version="1.0"

# Instala aplicações básicas para caso precise vasculhar um contêiner da imagem
RUN apt-get update
RUN apt-get install nano

# Cria um diretório Base na imagem
RUN mkdir -p /myServer
RUN mkdir -p /Log

# Copia todo o conteúdo para o diretório Base
COPY . /myServer

# Determina qual o diretório "padrão" do contêiner quando o mesmo iniciar
WORKDIR /myServer

# Instala pacotes Python
RUN pip install --upgrade pip
RUN pip install -r /myServer/requirements.txt

# Expõe alguns diretórios para o HOST
VOLUME /myServer/config
VOLUME /Log

# Expõe para o HOST algumas portas, por padrão
EXPOSE 80
EXPOSE 8080
EXPOSE 5000

# Comando para rodar o servidor Flask
# CMD ["python", "serving.py"]
CMD ["sh", "-c", "python serving.py & sleep 5 && python client.py"]
# http://192.168.15.128:5000