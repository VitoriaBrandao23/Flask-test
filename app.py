from flask import Flask

app = Flask(__name__)

@app.route('/')
def initial():
    return 'Olá, mundo!'

@app.route('/<idioma>')
def helloWorld(idioma):
    if idioma == 'portugues':
        mensagem = 'Olá, mundo!'
    elif idioma == 'ingles':
        mensagem = 'Hello, world!'
    elif idioma == 'frances':
        mensagem = 'Salut, monde!'
    else:
        mensagem = 'Não tenho conhecimento!'
    
    return f'<h1>{mensagem}</h1>'
