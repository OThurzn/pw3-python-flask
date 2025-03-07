# Comentário em Python
# Importando o pacote do Flask
from flask import Flask
from controllers import routes

#Carregamoento da variável app
app = Flask(__name__, template_folder='views')

#Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

if __name__ == '__main__':
    #Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
