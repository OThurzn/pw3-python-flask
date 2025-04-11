# Comentário em Python
# pip install pymysql; pip install mysqlclient; pip install flask-sqlalchemy
# Importando o pacote do Flask
from flask import Flask
# Importando o PyMySQL
import pymysql
# Importando as rotas que estão nos controllers
from controllers import routes
# Importando o model Game
from models.database import db

# Carregamoento da variável app
app = Flask(__name__, template_folder='views')

# Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'
# Configura o FLask com o banco definido
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    # Criando os dados de conexão:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass='pymysql.cursors.DictCursor')
    # Tentando criar o banco
    # Try, trata o sucesso
    try:
        with connection.cursor() as cursor:
            # Cria o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado!")

            # Except, trata a falha
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
        
    # Passando o flasj para SQLAlchemy
    db.init_app(app=app)
    
    #Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
