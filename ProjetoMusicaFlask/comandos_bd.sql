create database playMusica;

use playmusica;

-- Criando as tabelas do banco
create table musica(
	id_musica int primary key auto_increment not null,
    nome_musica varchar(50) not null,
	cantor_banda varchar(50) not null,
    genero_musica varchar(20) not null
    );
    
-- Primeiras consultas
select * from musica;
select nome_musica, genero_musica from musica;

-- Inserindo dados com INSERT
insert into musica(nome_musica, cantor_banda, genero_musica)
values('Am i dreaming', 'Metro Boomin', 'Pop');

insert into musica(nome_musica, cantor_banda, genero_musica)
values('The pretender', 'Foo fighters', 'Rock');

-- Inserindo mais de um dado de uma vez
insert into musica(nome_musica, cantor_banda, genero_musica)
values('Ainda gosto dela', 'Skank', 'Mpb'),
('Mente má', 'Nakama, Mc Staff', 'Funk'),
('Like you do', 'Joji', 'Pop'),
('End of begining', 'Djo', 'Pop'),
('Annihilate', 'Metro Boomin', 'Pop');

-- Consultas com WHERE
select * from musica where genero_musica = 'Pop';
select * from musica where cantor_banda = 'Metro Boomin';

-- SEMPRE Q STARTAR USAR 'use playmusica' PARA INICIAR O BANCO!

-- Fazendo consultas com o comando LIKE
select * from musica where cantor_banda like 'M%';
select * from musica where cantor_banda like '%n';

-- Fazendo consultas com o sinal de diferente '<>'
select * from musica where genero_musica <> 'Mpb';
select * from musica where cantor_banda like '%o%';

-- Fazendo consultas com numeros 'menor igual <=' e 'maior igual >='
select * from musica where id_musica <= 5;
select * from musica where id_musica >= 5;

-- Fazendo atualizações com UPDATE
update musica set nome_musica = 'End of beginning' where id_musica = 6;
update musica set genero_musica = 'Indie' where id_musica = 5;

-- Fazendo exclusão de registros com DELETE
delete from musica where id_musica = 7;


-- Criando tabela de usuários
create table usuario(
id_usuario int primary key auto_increment not null,
nome_usuario varchar(50) not null,
login_usuario varchar(30) not null,
senha_usuario varchar(20) not null);

select * from usuario;

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Gustavo Freitas', 'gufreitas04', 'admin');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Gabriel Oliveira', 'gabfelipe', 'admin123');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Gustavo Felipe', 'gufreitas04', 'felipe04');

-- Limpando uma tabela com o comando TRUNCATE
truncate table usuario;

-- Fazendo o campo de login ser unico com o comando UNIQUE
-- Usando 'add' e 'alter table' para alterar uma tabela e adicionar algo
alter table usuario add unique(login_usuario);

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Gustavo Freitas', 'gufreitas04', 'admin'),
('Gabriel Oliveira', 'gabfelipe04', 'admin123');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Gustavo Felipe', 'gufelipe04', 'felipe04');

-- Fazendo exclusão de usuarios com DELETE
delete from usuario where id_usuario = 5;