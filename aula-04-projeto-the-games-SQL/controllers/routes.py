from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edsongf',
             'kioto', 'black.butterfly', 'jujudopix']

# Array de objetos
gamelist = [{'Titulo': 'CS-GO',
             'Ano': 2012,
             'Categoria': 'FPS Online'}]

consolelist = [{'Nome': 'Playstation 5',
                'Preco': 4300,
                'Pais': 'Estados Unidos'}]


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

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Titulo': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')})

        return render_template('cadgames.html', gamelist=gamelist)

    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():

        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('preco') and request.form.get('pais'):
                consolelist.append({'Nome': request.form.get('nome'),
                                    'Preco': request.form.get('preco'),
                                    'Pais': request.form.get('pais')})

        return render_template('cadconsoles.html', consolelist=consolelist)
