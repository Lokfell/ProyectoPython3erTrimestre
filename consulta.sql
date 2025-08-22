----------------------------------------------------------
/*CONSULTA A TABLA USUARIOS*/
----------------------------------------------------------
select *from usuarios
drop table usuarios
----------------------------------------------------------
/*CONSULTA A TABLA ROLES*/
----------------------------------------------------------
select *from roles
drop table roles
----------------------------------------------------------
/*CONSULTA A TABLA ALUMNOS*/
----------------------------------------------------------
select *from alumnos 
drop table alumnos
----------------------------------------------------------
/*CONSULTA A TABLA CIUDADES*/
----------------------------------------------------------
drop table ciudades cascade
select *from ciudades 
drop table ciudades
----------------------------------------------------------
/*CONSULTA A TABLA DEPARTAMENTOS*/
----------------------------------------------------------
select *from departamentos 
drop table departamentos
----------------------------------------------------------
/*CONSULTA A TABLA NACIONALIDADES*/
----------------------------------------------------------
select *from nacionalidades 
drop table nacionalidades
----------------------------------------------------------
/*CONSULTA A TABLA CARRERAS*/
----------------------------------------------------------
select *from carreras 
drop table carreras
----------------------------------------------------------
/*CONSULTA A TABLA EXTENSIONES*/
----------------------------------------------------------
select *from extensiones
drop table extensiones

----------------------------------------------------------
/*CREACION DE TABLA USUARIOS*/
----------------------------------------------------------
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
	cod_Alumno varchar(20) not null,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave TEXT NOT NULL,
	rol varchar(20) not null
);

insert into usuarios (cod_Alumno, usuario, clave, rol) 
values('8128602','Mel','123','Alumno/a');

insert into usuarios (cod_Alumno, usuario, clave, rol) 
values('6592374','Juan','123','Alumno/a');

insert into usuarios (cod_Alumno, usuario, clave, rol) 
values('8123640','Car','123','Alumno/a');

insert into usuarios (cod_Alumno, usuario, clave, rol) 
values('4523961','Pedro','123','Alumno/a');

ALTER TABLE usuarios add foreign key (rol) references roles(descripción);
ALTER TABLE usuarios add foreign key (cod_Alumno) references alumnos(ci);

----------------------------------------------------------
/*CREACION DE TABLA ROLES*/
----------------------------------------------------------
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    descripción VARCHAR(50) UNIQUE NOT NULL
);

insert into roles (descripción) 
values('Administrador');

insert into roles (descripción) 
values('Docente');

insert into roles (descripción) 
values('Alumno/a');

insert into roles (descripción) 
values('Secretario/a');

----------------------------------------------------------
/*CREACION DE TABLA ALUMNOS*/
----------------------------------------------------------
create table alumnos (
	id serial primary key,
	ci varchar unique not null,
	nombre varchar(20) not null,
	apellido varchar(20) not null,
	telefono varchar(15) not null,
	nacionalidad varchar(20) not null,
	ciudad varchar(20) not null,
	direccion varchar(20) not null,
	email varchar(20) not null
);

insert into alumnos (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '8128602','Melissa','Oviedo','0972676396','Paraguayo/a','Itagua','Itagua','meloviedo@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '6592374','Juan','Orue','0981963246','Paraguayo/a','Capiatá','Capiatá','juan@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '4523961','Pedro','Veron','0972305981','Argentino/a','J. Augusto Saldivar','J. Agusto','pedrito@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '8123640','Carmen','Sanabria','0985962460','Brasilero/a','Guarambaré','Guarambaré','carmen@gmail.com');

ALTER TABLE alumnos add foreign key (ciudad) references ciudades(nombre);
ALTER TABLE alumnos add foreign key (nacionalidad) references nacionalidades(descripción);

----------------------------------------------------------
/*CREACION DE TABLA CIUDADES*/
----------------------------------------------------------
create table ciudades (
	id serial primary key,
	nombre varchar(20) unique not null,
	departamento varchar(20) not null
);

insert into ciudades (nombre, departamento) 
values('Itá','Central');

insert into ciudades (nombre, departamento) 
values('J. Augusto Saldivar','Central');

insert into ciudades (nombre, departamento) 
values('Guarambaré','Central');

insert into ciudades (nombre, departamento) 
values('Itagua','Central');

insert into ciudades (nombre, departamento) 
values('Capiatá','Central');

insert into ciudades (nombre, departamento) 
values('Yaguarón','Paraguarí');

insert into ciudades (nombre, departamento) 
values('Asunción','Capital');

ALTER TABLE ciudades add foreign key (departamento) references departamentos(nombre);

----------------------------------------------------------
/*CREACION DE TABLA DEPARTAMENTOS*/
----------------------------------------------------------
create table departamentos (
	id serial primary key,
	nombre varchar(20) unique not null
);

insert into departamentos (nombre) 
values('Central');

insert into departamentos (nombre) 
values('Coordillera');

insert into departamentos (nombre) 
values('Paraguarí');

insert into departamentos (nombre) 
values('Capital');

----------------------------------------------------------
/*CREACION DE TABLA NACIONALIDADES*/
----------------------------------------------------------
create table nacionalidades (
	id serial primary key,
	descripción varchar(20) unique not null
);

insert into nacionalidades (descripción) 
values('Paraguayo/a');

insert into nacionalidades (descripción) 
values('Argentino/a');

insert into nacionalidades (descripción) 
values('Brasilero/a');

insert into nacionalidades (descripción) 
values('Uruguayo/a');

----------------------------------------------------------
/*CREACION DE TABLA CARRERAS*/
----------------------------------------------------------
create table carreras (
	id serial primary key,
	descripción varchar(50) unique not null
);

insert into carreras (descripción) 
values('Ingeniería Informática');

insert into carreras (descripción) 
values('Ingeniería Comercial');

insert into carreras (descripción) 
values('Licenciatura en Enfermería');

insert into carreras (descripción) 
values('Licenciatura en Ciencias de la Educación');

----------------------------------------------------------
/*CREACION DE TABLA EXTENSIONES*/
----------------------------------------------------------
create table extensiones (
	id serial primary key,
	descripción varchar(50) unique not null,
	horas int not null,
	cod_Alumno varchar(20) not null,
	cod_Carrera varchar(50) not null
);

insert into extensiones (descripción, horas, cod_Alumno, cod_Carrera) 
values('Seminario', '3', '8128602', 'Ingeniería Informática');

insert into extensiones (descripción, horas, cod_Alumno, cod_Carrera) 
values('Proyecto de extensión', '3', '8128602', 'Ingeniería Informática');

insert into extensiones (descripción, horas, cod_Alumno, cod_Carrera) 
values('Voluntariado', '3', '8128602', 'Ingeniería Informática');

ALTER TABLE extensiones add foreign key (cod_Alumno) references alumnos(ci);
ALTER TABLE extensiones add foreign key (cod_Carrera) references carreras(descripción);

