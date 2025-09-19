# Importando o Flask
from flask import Flask
# Importando as rotas que estão nos controllers
from controllers import routes

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Chamando as rotas
routes.init_app(app)

# Iniciando o servidor no localhost, porta 5001, modo de depuração ativado
if __name__ == '__main__':
    # Inicializando a aplicação Flask
    app.run(host='0.0.0.0', port=4000, debug=True)
