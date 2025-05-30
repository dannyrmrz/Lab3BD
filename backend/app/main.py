from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas
from .models import Reserva
from .schemas import ReservaCreate
from . import crud

models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to read all reservations
@app.get("/reservas/", response_model=list[schemas.Reserva])
def read_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Reserva).offset(skip).limit(limit).all()

# Route to create a reservation
@app.post("/reservas/", response_model=schemas.Reserva)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    db_reserva = Reserva(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

# Route to read a specific reservation
@app.get("/reservas/{reserva_id}", response_model=schemas.Reserva)
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = crud.get_reserva(db, reserva_id=reserva_id)
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

# Route to update a reservation
@app.put("/reservas/{reserva_id}", response_model=schemas.Reserva)
def update_reserva(reserva_id: int, reserva: schemas.ReservaUpdate, db: Session = Depends(get_db)):
    updated_reserva = crud.update_reserva(db=db, reserva_id=reserva_id, reserva=reserva)
    if updated_reserva is None:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return updated_reserva

# Route to delete a reservation
@app.delete("/reservas/{reserva_id}", response_model=schemas.Reserva)
def delete_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = crud.delete_reserva(db=db, reserva_id=reserva_id)
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

@app.get("/")
def root():
    return {"message": "API funcionando"}