# models.py
from sqlalchemy import Column, Integer, String, Text, Date, Time, Enum, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
import enum

class TipoUsuarioEnum(enum.Enum):
    visitante = "visitante"
    empleado = "empleado"

class EstadoReservaEnum(enum.Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"
    cancelada = "cancelada"

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    tipo_usuario = Column(Enum(TipoUsuarioEnum, name="tipousuario", create_type=True), nullable=False)

    reservas = relationship("Reserva", back_populates="usuario")

class Atraccion(Base):
    __tablename__ = 'atraccion'

    id_atraccion = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    capacidad = Column(Integer, nullable=False)
    tiempo_promedio = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("capacidad > 0"),
        CheckConstraint("tiempo_promedio > 0"),
    )

    colas = relationship("Cola", back_populates="atraccion")

class Cola(Base):
    __tablename__ = 'cola'

    id_cola = Column(Integer, primary_key=True)
    id_atraccion = Column(Integer, ForeignKey('atraccion.id_atraccion'), nullable=False)
    fecha = Column(Date, nullable=False)
    max_personas = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("max_personas > 0"),
    )

    atraccion = relationship("Atraccion", back_populates="colas")
    reservas = relationship("Reserva", back_populates="cola")

class Reserva(Base):
    __tablename__ = 'reserva'

    id_reserva = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    id_cola = Column(Integer, ForeignKey('cola.id_cola'), nullable=False)
    estado = Column(Enum(EstadoReservaEnum, name="estadoreserva", create_type=True), nullable=False)
    hora_reserva = Column(Time, nullable=False)

    usuario = relationship("Usuario", back_populates="reservas")
    cola = relationship("Cola", back_populates="reservas")
