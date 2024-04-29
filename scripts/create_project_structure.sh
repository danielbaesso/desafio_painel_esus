#!/bin/bash

# Criar pastas
mkdir -p ../app/endpoints
mkdir -p ../app/services
mkdir -p ../app/models
mkdir -p ../config
mkdir -p ../static
mkdir -p ../templates

# Criar arquivos
touch ../app/__init__.py
touch ../app/endpoints/__init__.py
touch ../app/endpoints/consultas_endpoints.py
touch ../app/endpoints/outros_endpoints.py
touch ../app/services/__init__.py
touch ../app/services/consultas_service.py
touch ../app/services/outro_servico.py
touch ../app/models/__init__.py
touch ../app/models/consultas.py
touch ../config/__init__.py
touch ../config/config.py
touch ../static/.gitkeep
touch ../templates/.gitkeep
touch ../run.py
touch ../requirements.txt

echo "Estrutura de pastas e arquivos criada com sucesso!"
