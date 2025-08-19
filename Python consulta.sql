CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave TEXT NOT NULL
);


---------------------------------------------------------
/*CONSULTA A TABLA USUARIO*/
----------------------------------------------------------

select *from usuarios

drop table usuarios

SELECT * FROM usuarios WHERE nivel != '1';

ALTER TABLE usuarios ALTER COLUMN email TYPE VARCHAR(50);

delete from usuarios where id=11;

----------------------------------------------------------
/*CREACION DE TABLA USUARIO*/
----------------------------------------------------------
create table usuarios (
	id serial primary key,
	ci varchar unique not null,
	nombre varchar(20) not null,
	apellido varchar(20) not null,
	telefono varchar(15) not null,
	direccion varchar(20) not null,
	email varchar(20) not null,
	usuario varchar(15) not null,
	clave varchar(15) not null,
	nivel varchar(10) 
)

insert into usuarios (ci, nombre, apellido, telefono, direccion, email, usuario, clave, nivel) 
values( '8128602','Melissa','Oviedo','0972676396','Itagua','meloviedo@gmail.com','Mel','123','1');

insert into usuarios (ci, nombre, apellido, telefono, direccion, email, usuario, clave) 
values( '6592374','Juan','Orue','0981963246','Capiata','juan@gmail.com','Juan','456');

insert into usuarios (ci, nombre, apellido, telefono, direccion, email, usuario, clave) 
values( '4523961','Pedro','Veron','0972305981','J. Agusto','pedrito@gmail.com','Pedro','456');

insert into usuarios (ci, nombre, apellido, telefono, direccion, email, usuario, clave, nivel) 
values( '8123640','Carmen','Sanabria','0985962460','Guarambare','carmen@gmail.com','Car','123','1');
