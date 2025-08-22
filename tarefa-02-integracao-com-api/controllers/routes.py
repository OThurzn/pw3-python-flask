from flask import render_template, request, url_for, redirect
import urllib.request
import json

def init_app(app):
    # Rota principal para listar todas as frutas
    @app.route('/')
    @app.route('/fruits', methods=['GET'])
    def fruits():
        try:
            # URL da API do One Piece
            url = 'https://api.api-onepiece.com/v2/fruits/en'
            response = urllib.request.urlopen(url)
            apiData = response.read()
            fruitsList = json.loads(apiData)
            
            return render_template('fruits.html', fruitsList=fruitsList)
        except Exception as e:
            return render_template('error.html', error=str(e))

    # Rota para mostrar detalhes de uma fruta específica
    @app.route('/fruits/<int:id>', methods=['GET'])
    def fruit_detail(id):
        try:
            # URL da API do One Piece
            url = 'https://api.api-onepiece.com/v2/fruits/en'
            response = urllib.request.urlopen(url)
            apiData = response.read()
            fruitsList = json.loads(apiData)
            
            # Procurar a fruta pelo ID
            fruit_info = None
            for fruit in fruitsList:
                if fruit['id'] == id:
                    fruit_info = fruit
                    break
            
            if fruit_info:
                return render_template('fruit_detail.html', fruit=fruit_info)
            else:
                return f'A fruta com a ID {id} não foi encontrado.'
        except Exception as e:
            return render_template('error.html', error=str(e))




