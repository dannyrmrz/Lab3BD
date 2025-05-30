-- Usuarios
INSERT INTO Usuario (nombre, email, tipo_usuario) VALUES
('Carlos Pérez', 'carlos@example.com', 'visitante'),
('Ana Gómez', 'ana@example.com', 'visitante'),
('Luis Torres', 'luis@example.com', 'visitante'),
('Marta Ruiz', 'marta@example.com', 'visitante'),
('Pedro López', 'pedro@example.com', 'empleado');

-- Atracciones
INSERT INTO Atraccion (nombre, descripcion, capacidad, tiempo_promedio) VALUES
('Montaña Rusa', 'Atracción de alta velocidad', 20, 5),
('Casa del Terror', 'Atracción de miedo', 15, 7),
('Rueda de la Fortuna', 'Rueda panorámica gigante', 30, 10);

-- Colas
INSERT INTO Cola (id_atraccion, fecha, max_personas) VALUES
(1, '2025-06-01', 100),
(1, '2025-06-02', 80),
(2, '2025-06-01', 70),
(3, '2025-06-01', 120);

-- Reservas (más de 30 combinaciones)
INSERT INTO Reserva (id_usuario, id_cola, estado, hora_reserva) VALUES
(1, 1, 'confirmada', '10:00'),
(1, 2, 'pendiente', '11:00'),
(2, 1, 'confirmada', '10:15'),
(2, 3, 'confirmada', '12:00'),
(3, 1, 'pendiente', '10:30'),
(3, 4, 'cancelada', '13:00'),
(4, 3, 'confirmada', '11:30'),
(4, 2, 'confirmada', '11:45'),
(4, 4, 'pendiente', '13:15'),
(1, 3, 'confirmada', '12:30'),
(2, 4, 'pendiente', '13:00'),
(3, 2, 'confirmada', '11:00'),
(1, 4, 'confirmada', '14:00'),
(3, 3, 'pendiente', '12:45'),
(2, 2, 'confirmada', '11:30'),
(4, 1, 'cancelada', '10:45'),
(2, 3, 'pendiente', '12:15'),
(1, 1, 'confirmada', '09:30'),
(3, 2, 'confirmada', '11:20'),
(1, 3, 'confirmada', '12:10'),
(4, 4, 'confirmada', '13:30'),
(2, 1, 'confirmada', '10:50'),
(3, 4, 'pendiente', '14:15'),
(2, 4, 'cancelada', '14:45'),
(3, 1, 'confirmada', '10:10'),
(4, 3, 'confirmada', '12:50'),
(1, 2, 'confirmada', '10:40'),
(2, 2, 'pendiente', '11:10'),
(3, 3, 'cancelada', '12:35'),
(1, 4, 'confirmada', '13:50');
