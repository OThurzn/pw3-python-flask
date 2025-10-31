from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os
import uuid
from database import db, Imagem


app = Flask(__name__)
app.secret_key = 'troque-essa-chave'  # necessário para flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

feedbacks = []

@app.route("/oque")
def oque():
    return render_template("oque.html")

@app.route("/colete")
def colete():
    return render_template("colete.html")

@app.route("/telas")
def telas():
    return render_template("telas.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        feedbacks.append({
            'nome': nome,
            'email': email,
            'assunto': assunto,
            'mensagem': mensagem
        })

        return redirect(url_for('index'))

    return render_template('index.html', feedbacks=feedbacks)

# Define pasta que receberá arquivos de upload
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# Define o tamanho máximo de um arquivo de upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Definindo tipos de arquivos permitidos
FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
def arquivos_permitidos(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

# UPLOAD DE IMAGENS
@app.route('/galeria', methods=['GET', 'POST'])
def galeria():
    # Seleciona os nomes dos arquivos de imagens no banco
    imagens = Imagem.query.all()

    if request.method == 'POST':
        # Captura o arquivo vindo do formulário
        file = request.files['file']
        # Verifica se a extensão do arquivo é permitida
        if not arquivos_permitidos(file.filename):

            flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
            return redirect(request.url)

        # Define um nome aleatório para o arquivo
        filename = str(uuid.uuid4())

        # Gravando o nome do arquivo no banco
        img = Imagem(filename)
        db.session.add(img)
        db.session.commit()


        # Salva o arquivo na pasta de uploads
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("Imagem enviada com sucesso!", 'success')

        return redirect(url_for('galeria'))
    return render_template('galeria.html', imagens=imagens)


if __name__ == '__main__':
    
    if sys.platform.startswith('win'):
        import msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
        msvcrt.setmode(sys.stderr.fileno(), os.O_BINARY)
    
    app.run(host="127.0.0.1", port=5000, debug=True)
