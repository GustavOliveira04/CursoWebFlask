import os
from app import app 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class FormularioMusica(FlaskForm):
    nome = StringField('Nome da música', [validators.DataRequired(), validators.length(min = 1, max = 50)])
    banda = StringField('Nome da banda/cantor', [validators.DataRequired(), validators.length(min = 1, max = 50)])
    genero = StringField('Gênero da música', [validators.DataRequired(), validators.length(min = 1, max = 20)])
    cadastrar = SubmitField ('Cadastrar música')

class FormularioUsuario(FlaskForm):
    usuario = StringField('Usuário', [validators.DataRequired(), validators.length(min = 2, max = 30)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.length(min = 1, max = 20)])
    logar = SubmitField('Entrar')
 
class FormularioCadastroUsuario(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.length(min = 1, max = 50)])
    usuario = StringField('Usuário', [validators.DataRequired(), validators.length(min = 1, max = 30)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.length(min = 1, max = 255)])
    cadastrar = SubmitField('Cadastrar usuário')


def recupera_imagem(id):
    for nome_imagem in os.listdir(app.config['UPLOAD_PASTA']):

        nome = str(nome_imagem)

        nome = nome.split('.')

        if f'album{id}' in nome[0]:
            return nome_imagem
        
    return 'default.png'

def deletar_imagem(id):
    imagem = recupera_imagem(id)

    if imagem != 'default.png':
        os.remove(os.path.join(app.config['UPLOAD_PASTA'], imagem))