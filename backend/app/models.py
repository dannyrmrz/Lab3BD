from sqlalchemy import Column, Integer, String, ForeignKey, Time, Enum as SQLEnum
from sqlalchemy.orm import relationship
from .custom_types import TipoUsuario, EstadoReserva
from .database import Base

class Usuario(Base):
    __tablename__ = 'Usuario'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    tipo_usuario = Column(SQLEnum(TipoUsuario), nullable=False)

    reservas = relationship("Reserva", back_populates="usuario")

class Atraccion(Base):
    __tablename__ = 'Atraccion'

    id_atraccion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    capacidad = Column(Integer, nullable=False)
    tiempo_promedio = Column(Integer, nullable=False)

    colas = relationship("Cola", back_populates="atraccion")

class Cola(Base):
    __tablename__ = 'Cola'

    id_cola = Column(Integer, primary_key=True, index=True)
    id_atraccion = Column(Integer, ForeignKey('Atraccion.id_atraccion'))
    fecha = Column(String, nullable=False)
    max_personas = Column(Integer, nullable=False)

    atraccion = relationship("Atraccion", back_populates="colas")
    reservas = relationship("Reserva", back_populates="cola")

class Reserva(Base):
    __tablename__ = 'Reserva'

    id_reserva = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    id_cola = Column(Integer, ForeignKey('Cola.id_cola'))
    estado = Column(SQLEnum(EstadoReserva), nullable=False)
    hora_reserva = Column(Time, nullable=False)

    usuario = relationship("Usuario", back_populates="reservas")
    cola = relationship("Cola", back_populates="reservas")