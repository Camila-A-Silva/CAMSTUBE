CREATE DATABASE IF NOT EXISTS CamsTube;

USE CamsTube;


CREATE TABLE IF NOT EXISTS genero (
 nome_genero VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);



CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME(6),
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT FK_musica_0 FOREIGN KEY (nome_genero) REFERENCES genero (nome_genero)
);



