from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Musica
from app import db, app
from definicoes import recupera_imagem, deletar_imagem, FormularioMusica
import time

@app.route('/')
def listarMusicas():

    if session.get('usuario_logado') is None:
        return redirect(url_for('fazer_Login'))
    
    lista = Musica.query.order_by(Musica.id_musica)

    return render_template('musiclist.html',
                            titulo = 'Músicas Cadastradas', 
                            musicas = lista)

@app.route('/cadastrar')
def cadastrar_Musicas():

    if session.get('usuario_logado') is None:
        return redirect (url_for('fazer_Login'))

    form = FormularioMusica()

    return render_template('cadastra_musica.html',
                           titulo = 'Cadastre uma Música', form = form)

@app.route('/adicionar', methods = ['POST',])
def adicionar_Musicas():

    formRecebido = FormularioMusica(request.form)

    if not formRecebido.validate_on_submit():
        return redirect(url_for('cadastrar_Musicas'))

    nome = formRecebido.nome.data
    cantorBandaGrupo = formRecebido.banda.data
    genero = formRecebido.genero.data

    musica = Musica.query.filter_by(nome_musica = nome).first()

    if musica:
        flash("Essa música já foi cadastrada!")
        return redirect(url_for('listarMusicas'))

    nova_musica = Musica(nome_musica = nome, cantor_banda = cantorBandaGrupo, genero_musica = genero)

    db.session.add(nova_musica)
    db.session.commit()

    arquivo = request.files['arquivo']

    if arquivo:

        pasta_arquivos = app.config['UPLOAD_PASTA']

        nome_arquivo = arquivo.filename

        nome_arquivo = nome_arquivo.split('.')

        extensao = nome_arquivo[len(nome_arquivo)-1]

        momento = time.time()

        nome_completo = f'album{nova_musica.id_musica}_{momento}.{extensao}'

        arquivo.save(f'{pasta_arquivos}/{nome_completo}')
    

    return redirect(url_for('listarMusicas'))

@app.route('/editar/<int:id>')
def editar(id):
 
    if session.get('usuario_logado') is None:
        return redirect(url_for('fazer_Login'))
    
    musicaBuscada = Musica.query.filter_by(id_musica = id).first()

    form = FormularioMusica()

    form.nome.data = musicaBuscada.nome_musica
    form.banda.data = musicaBuscada.cantor_banda
    form.genero.data = musicaBuscada.genero_musica

    album = recupera_imagem(id)

    return render_template('editar_musica.html',
                           titulo = 'Editar música',
                           musica = form,
                           album_musica = album,
                           id = id)

@app.route('/atualizar', methods = ['POST'])
def atualizar():
    
    formRecebido = FormularioMusica(request.form)

    if formRecebido.validate_on_submit():

        musica = Musica.query.filter_by(id_musica = request.form['txtId']).first()

        musica.nome_musica = formRecebido.nome.data
        musica.cantor_banda = formRecebido.banda.data
        musica.genero_musica = formRecebido.genero.data

        db.session.add(musica)
        db.session.commit()

        arquivo = request.files['arquivo']

        if arquivo:

            pasta_upload = app.config['UPLOAD_PASTA']

            nome_arquivo = arquivo.filename

            nome_arquivo = nome_arquivo.split('.')

            extensao = nome_arquivo[len(nome_arquivo)-1]

            momento = time.time()

            nome_completo = f'album{musica.id_musica}_{momento}.{extensao}'

            deletar_imagem(musica.id_musica)

            arquivo.save(f'{pasta_upload}/{nome_completo}')

        flash("Música editada com sucesso!")

    return redirect(url_for('listarMusicas'))

@app.route('/excluir/<int:id>')
def excluir(id):

    if session.get('usuario_logado') is None:
        return redirect(url_for('fazer_Login'))
    
    Musica.query.filter_by(id_musica = id).delete()

    deletar_imagem(id)

    db.session.commit()

    flash("Música excluida com sucesso!")

    return redirect(url_for('listarMusicas'))

@app.route('/uploads/<nome_imagem>')
def imagem(nome_imagem):
    return send_from_directory('uploads', nome_imagem)
    