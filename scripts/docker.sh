# Remove o contêiner dbaesso_container se ele existir
sudo docker rm dbaesso_container

# Constrói a imagem Docker com a tag dbaesso_app usando o Dockerfile presente no diretório atual
sudo docker build -t dbaesso_app -f Dockerfile .

# Executa um novo contêiner Docker com o nome dbaesso_container usando a imagem Docker recém-construída com a tag dbaesso_app
sudo docker run --name dbaesso_container dbaesso_app
