create database elitehoopers;

use elitehoopers

create table contatos(
	nome varchar(60) not null unique,
    email varchar(60) not null unique,
    tel varchar(20),
    mensagem varchar(255)
);

select * from contatos
