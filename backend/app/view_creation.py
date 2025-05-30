from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from database import get_db


router = APIRouter()

@router.post("/reservations/", response_model=schemas.Reserva)
def create_reservation(reservation: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.create_reservation(db=db, reservation=reservation)

@router.get("/reservations/", response_model=list[schemas.Reserva])
def read_reservations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservations = crud.get_reservations(db, skip=skip, limit=limit)
    return reservations

@router.get("/reservations/{reservation_id}", response_model=schemas.Reserva)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = crud.get_reservation(db, reservation_id=reservation_id)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.put("/reservations/{reservation_id}", response_model=schemas.Reserva)
def update_reservation(reservation_id: int, reservation: schemas.ReservaUpdate, db: Session = Depends(get_db)):
    updated_reservation = crud.update_reservation(db, reservation_id=reservation_id, reservation=reservation)
    if updated_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation

@router.delete("/reservations/{reservation_id}", response_model=schemas.Reserva)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    deleted_reservation = crud.delete_reservation(db, reservation_id=reservation_id)
    if deleted_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return deleted_reservation