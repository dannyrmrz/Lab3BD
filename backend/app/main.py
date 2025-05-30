from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models, crud, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/reservas/", response_model=list[schemas.Reserva])
def read_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reservations(db, skip=skip, limit=limit)

@app.post("/reservas/", response_model=schemas.Reserva)
def create_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.create_reservation(db, reservation=reserva)

@app.get("/reservas/{reserva_id}", response_model=schemas.Reserva)
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = crud.get_reservation(db, reservation_id=reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

@app.put("/reservas/{reserva_id}", response_model=schemas.Reserva)
def update_reserva(reserva_id: int, reserva: schemas.ReservaUpdate, db: Session = Depends(get_db)):
    updated_reserva = crud.update_reservation(db, reservation_id=reserva_id, reservation=reserva)
    if not updated_reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return updated_reserva

@app.delete("/reservas/{reserva_id}", response_model=schemas.Reserva)
def delete_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = crud.delete_reservation(db, reservation_id=reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

@app.get("/")
def root():
    return {"message": "API funcionando"}