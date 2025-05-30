from sqlalchemy.orm import Session
from models import Reserva
from schemas import ReservaCreate, ReservaUpdate


def create_reservation(db: Session, reservation: ReservaCreate):
    db_reservation = Reserva(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservation(db: Session, reservation_id: int):
    return db.query(Reserva).filter(Reserva.id_reserva == reservation_id).first()

def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reserva).offset(skip).limit(limit).all()

def update_reservation(db: Session, reservation_id: int, reservation: ReservaUpdate):
    db_reservation = db.query(Reserva).filter(Reserva.id_reserva == reservation_id).first()
    if db_reservation:
        for key, value in reservation.dict(exclude_unset=True).items():
            setattr(db_reservation, key, value)
        db.commit()
        db.refresh(db_reservation)
    return db_reservation

def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(Reserva).filter(Reserva.id_reserva == reservation_id).first()
    if db_reservation:
        db.delete(db_reservation)
        db.commit()
    return db_reservation