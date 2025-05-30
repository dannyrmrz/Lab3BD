
CREATE TABLE atraccion (
	id_atraccion SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	descripcion TEXT, 
	capacidad INTEGER NOT NULL, 
	tiempo_promedio INTEGER NOT NULL, 
	PRIMARY KEY (id_atraccion), 
	CHECK (capacidad > 0), 
	CHECK (tiempo_promedio > 0)
)

;


CREATE TABLE usuario (
	id_usuario SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	tipo_usuario tipousuario NOT NULL, 
	PRIMARY KEY (id_usuario), 
	UNIQUE (email)
)

;


CREATE TABLE cola (
	id_cola SERIAL NOT NULL, 
	id_atraccion INTEGER NOT NULL, 
	fecha DATE NOT NULL, 
	max_personas INTEGER NOT NULL, 
	PRIMARY KEY (id_cola), 
	CHECK (max_personas > 0), 
	FOREIGN KEY(id_atraccion) REFERENCES atraccion (id_atraccion)
)

;


CREATE TABLE reserva (
	id_reserva SERIAL NOT NULL, 
	id_usuario INTEGER NOT NULL, 
	id_cola INTEGER NOT NULL, 
	estado estadoreserva NOT NULL, 
	hora_reserva TIME WITHOUT TIME ZONE NOT NULL, 
	PRIMARY KEY (id_reserva), 
	FOREIGN KEY(id_usuario) REFERENCES usuario (id_usuario), 
	FOREIGN KEY(id_cola) REFERENCES cola (id_cola)
)

;

