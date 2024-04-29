# COMO RODAR
## Linux - Docker
A partir da raiz do projeto:
`sudo bash scripts/docker.sh`

## Linux - Docker Compose
A partir da raiz do projeto:
`sudo bash scripts/compose.sh`

## Windows - Docker Compose
A partir da raiz do projeto:
`docker compose build`
`docker compose up`

# ESTRUTURA DO PROJETO
Este projeto é baseado em uma arquitetura controller-service-repository, chamado também de endpoint.
Embora este projeto seja muito pequeno, decidiu-se usar esta estrutura para permitir que este projeto cresça e se expanda.
Todos os endpoints estão na pasta endpoints.
Toda a lógica de negócios está na pasta de serviço.
Todas as operações de dados estão no repositório.

Estamos usando dados fornecidos por um arquivo CSV. Mudar isso para alguma outra tecnologia (como banco de dados) deve ser fácil. Basta alterar os métodos necessários no arquivo do repositório.

# STACK
Utilizou-se:
- Python3
- Docker
- Flask
- Pandas

# PRÓXIMOS PASSOS
- Utilizar pandas ou pyspark para fazer limpeza mais padronizada das colunas.
- Criar teste unitário e de integração.
