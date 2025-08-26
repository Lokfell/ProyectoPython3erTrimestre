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

ALTER TABLE roles RENAME COLUMN descripción TO descripcion;

ALTER TABLE extensiones RENAME COLUMN descripción TO descripcion;

ALTER TABLE carreras RENAME COLUMN descripción TO descripcion;

ALTER TABLE nacionalidades RENAME COLUMN descripción TO descripcion;

ALTER TABLE alumnos RENAME TO personas;

ALTER TABLE extensiones RENAME COLUMN cod_alumno TO cod_persona;

ALTER TABLE usuarios RENAME COLUMN cod_alumno TO cod_persona;


----------------------------------------------------------
/*CONSULTA A TABLA PERSONAS*/
----------------------------------------------------------
select *from personas 
drop table personas
delete from personas where id=6;
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
delete from departamentos where id=1;
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

drop table extensiones cascade
----------------------------------------------------------
/*CREACION DE TABLA ROLES*/
----------------------------------------------------------
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(50) UNIQUE NOT NULL
);

insert into roles (descripcion) 
values('Administrador');

insert into roles (descripcion) 
values('Docente');

insert into roles (descripcion) 
values('Alumno/a');

insert into roles (descripcion) 
values('Secretario/a');

----------------------------------------------------------
/*CREACION DE TABLA NACIONALIDADES*/
----------------------------------------------------------
create table nacionalidades (
	id serial primary key,
	descripcion varchar(20) unique not null
);

insert into nacionalidades (descripcion) 
values('Paraguayo/a');

insert into nacionalidades (descripcion) 
values('Argentino/a');

insert into nacionalidades (descripcion) 
values('Brasilero/a');

insert into nacionalidades (descripcion) 
values('Uruguayo/a');

----------------------------------------------------------
/*CREACION DE TABLA DEPARTAMENTOS*/
----------------------------------------------------------
create table departamentos (
	id serial primary key,
	nombre varchar(20) unique not null
);

insert into departamentos (nombre) 
values('Alto Paraguay');

insert into departamentos (nombre) 
values('Alto Paraná');

insert into departamentos (nombre) 
values('Amambay');

insert into departamentos (nombre) 
values('Boquerón');

insert into departamentos (nombre) 
values('Caaguazú');

insert into departamentos (nombre) 
values('Caazapá');

insert into departamentos (nombre) 
values('Canindeyú');

insert into departamentos (nombre) 
values('Capital');

insert into departamentos (nombre) 
values('Central');

insert into departamentos (nombre) 
values('Concepción');

insert into departamentos (nombre) 
values('Coordillera');

insert into departamentos (nombre) 
values('Guairá');

insert into departamentos (nombre) 
values('Itapúa');

insert into departamentos (nombre) 
values('Misiones');

insert into departamentos (nombre) 
values('Ñeembucú');

insert into departamentos (nombre) 
values('Paraguarí');

insert into departamentos (nombre) 
values('Presidente Hayes');

insert into departamentos (nombre) 
values('San Pedro');

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
/*CREACION DE TABLA PERSONAS*/
----------------------------------------------------------
create table personas (
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

insert into personas (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '8128602','Melissa','Oviedo','0972676396','Paraguayo/a','Itagua','Itagua','meloviedo@gmail.com');

insert into personas (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '6592374','Juan','Orue','0981963246','Paraguayo/a','Capiatá','Capiatá','juan@gmail.com');

insert into personas (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '4523961','Pedro','Veron','0972305981','Argentino/a','J. Augusto Saldivar','J. Agusto','pedrito@gmail.com');

insert into personas (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '8123640','Carmen','Sanabria','0985962460','Brasilero/a','Guarambaré','Guarambaré','carmen@gmail.com');

insert into personas (ci, nombre, apellido, telefono, nacionalidad, ciudad, direccion, email) 
values( '123456','Hechicero','Supremo','0972676396','Paraguayo/a','Itagua','Itagua','lucascuak@gmail.com');

ALTER TABLE personas add foreign key (ciudad) references ciudades(nombre);
ALTER TABLE personas add foreign key (nacionalidad) references nacionalidades(descripcion);

----------------------------------------------------------
/*CREACION DE TABLA USUARIOS*/
----------------------------------------------------------
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
	cod_persona varchar(20) not null,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave TEXT NOT NULL,
	rol varchar(20) not null
);

insert into usuarios (cod_persona, usuario, clave, rol) 
values('8128602','Mel','123','Alumno/a');

insert into usuarios (cod_persona, usuario, clave, rol) 
values('6592374','Juan','123','Alumno/a');

insert into usuarios (cod_persona, usuario, clave, rol) 
values('8123640','Car','123','Alumno/a');

insert into usuarios (cod_persona, usuario, clave, rol) 
values('4523961','Pedro','123','Alumno/a');

ALTER TABLE usuarios add foreign key (rol) references roles(descripcion);
ALTER TABLE usuarios add foreign key (cod_persona) references personas(ci);

----------------------------------------------------------
/*CREACION DE TABLA CARRERAS*/
----------------------------------------------------------
create table carreras (
	id serial primary key,
	descripcion varchar(50) unique not null
);

insert into carreras (descripcion) 
values('Ingeniería Informática');

insert into carreras (descripcion) 
values('Ingeniería Comercial');

insert into carreras (descripcion) 
values('Licenciatura en Enfermería');

insert into carreras (descripcion) 
values('Licenciatura en Ciencias de la Educación');

----------------------------------------------------------
/*CREACION DE TABLA EXTENSIONES*/
----------------------------------------------------------


create table extensiones (
	id serial primary key,
	descripcion varchar(50) not null,
	horas int not null,
	cod_persona varchar(20) not null,
	cod_Carrera varchar(50) not null
);

insert into extensiones (descripcion, horas, cod_persona, cod_Carrera) 
values('Seminario', '3', '8128602', 'Ingeniería Informática');

insert into extensiones (descripcion, horas, cod_persona, cod_Carrera) 
values('Proyecto de extensión', '3', '8128602', 'Ingeniería Informática');

insert into extensiones (descripcion, horas, cod_persona, cod_Carrera) 
values('Voluntariado', '3', '8128602', 'Ingeniería Informática');

ALTER TABLE extensiones add foreign key (cod_persona) references personas(ci);
ALTER TABLE extensiones add foreign key (cod_Carrera) references carreras(descripcion);

