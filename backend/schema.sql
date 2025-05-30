-- filepath: c:\Users\BRUTE\Documents\GitHub\Lab3BD\backend\schema.sql

CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    tipo_usuario VARCHAR(20) NOT NULL CHECK (tipo_usuario IN ('visitante', 'empleado'))
);

CREATE TABLE Atraccion (
    id_atraccion SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    capacidad INT NOT NULL,
    tiempo_promedio INT NOT NULL
);

CREATE TABLE Cola (
    id_cola SERIAL PRIMARY KEY,
    id_atraccion INT REFERENCES Atraccion(id_atraccion),
    fecha DATE NOT NULL,
    max_personas INT NOT NULL
);

CREATE TABLE Reserva (
    id_reserva SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario),
    id_cola INT REFERENCES Cola(id_cola),
    estado VARCHAR(20) NOT NULL CHECK (estado IN ('pendiente', 'confirmada', 'cancelada')),
    hora_reserva TIME NOT NULL
);