from flask import Flask
from app.endpoints.atendimentos_endpoints import consultas_bp
from config import config

def create_app():
    # Criação de uma instância do aplicativo Flask
    app = Flask(__name__)

    # Registrar Blueprint 'consultas_bp'
    app.register_blueprint(consultas_bp)

    # Configurações do aplicativo Flask
    app.config.from_object(config)

    return app

if __name__ == '__main__':
    # Execução do aplicativo Flask
    app = create_app()
    app.run(host='localhost', port='8001', debug=True)
