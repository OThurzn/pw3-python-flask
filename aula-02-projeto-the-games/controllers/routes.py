from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edsongf',
             'kioto', 'black.butterfly', 'jujudopix']

# Array de objetos
gamelist = [{'Titulo': 'CS-GO',
             'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
# Criando função no Python
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # acessando o primeiro
        game = gamelist[0]

        if request.method == 'POST':
            if request.form.get('jogador'):  # nome do input
                jogadores.append(request.form.get('jogador'))

        jogos = ['Fortnite', 'PUBG', 'The last of us', 'God of War',
                 'Ghost of Tsushima', 'Spider Man', 'Cuphead']

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'): gamelist.append({'Titulo': request.form.get('titulo'),
                                                                                                                          'Ano': request.form.get('ano'),
                                                                                                                          'Categoria': request.form.get('categoria')})

        return render_template('cadgames.html', gamelist=gamelist)
