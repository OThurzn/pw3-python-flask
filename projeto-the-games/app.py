# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando função no Python
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores = ['iruah', 'davi_lambari', 'edsongf', 'kioto', 'black.butterfly', 'jujudopix']
    jogos = ['Fortnite', 'PUBG', 'The last of us', 'God of War', 'Ghost of Tsushima', 'Spider Man', 'Cuphead']
    return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores,
                           jogos=jogos)


if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
