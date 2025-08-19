----------------------------------------------------------
/*CONSULTA A TABLA USUARIO*/
----------------------------------------------------------

select *from usuarios

drop table usuarios

SELECT * FROM usuarios WHERE nivel != '1';

ALTER TABLE usuario ALTER COLUMN email TYPE VARCHAR(50);

delete from usuario where id=11;

----------------------------------------------------------
/*CREACION DE TABLA USUARIO*/
----------------------------------------------------------
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave TEXT NOT NULL
);


insert into usuario (ci, nombre, apellido, telefono, direccion, email, usuario, clave, nivel) 
values( '8128602','Melissa','Oviedo','0972676396','Itagua','meloviedo@gmail.com','Mel','123','1');

insert into usuario (ci, nombre, apellido, telefono, direccion, email, usuario, clave) 
values( '6592374','Juan','Orue','0981963246','Capiata','juan@gmail.com','Juan','456');

insert into usuario (ci, nombre, apellido, telefono, direccion, email, usuario, clave) 
values( '4523961','Pedro','Veron','0972305981','J. Agusto','pedrito@gmail.com','Pedro','456');

insert into usuario (ci, nombre, apellido, telefono, direccion, email, usuario, clave, nivel) 
values( '8123640','Carmen','Sanabria','0985962460','Guarambare','carmen@gmail.com','Car','123','1');

----------------------------------------------------------
/*CONSULTA A TABLA USUARIO*/
----------------------------------------------------------

select *from alumnos 

select ci, nombre, apellido, telefono, direccion, email from alumnos 

drop table alumnos

SELECT * FROM alumnos WHERE --- != '1';

ALTER TABLE alumnos ALTER COLUMN --- TYPE VARCHAR(50);

delete from alumnos where id=11;

----------------------------------------------------------
/*CREACION DE TABLA USUARIO*/
----------------------------------------------------------
create table alumnos (
	id serial primary key,
	ci varchar unique not null,
	nombre varchar(20) not null,
	apellido varchar(20) not null,
	telefono varchar(15) not null,
	direccion varchar(20) not null,
	email varchar(20) not null
);


insert into alumnos (ci, nombre, apellido, telefono, direccion, email) 
values( '8128602','Melissa','Oviedo','0972676396','Itagua','meloviedo@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, direccion, email) 
values( '6592374','Juan','Orue','0981963246','Capiata','juan@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, direccion, email) 
values( '4523961','Pedro','Veron','0972305981','J. Agusto','pedrito@gmail.com');

insert into alumnos (ci, nombre, apellido, telefono, direccion, email) 
values( '8123640','Carmen','Sanabria','0985962460','Guarambare','carmen@gmail.com');