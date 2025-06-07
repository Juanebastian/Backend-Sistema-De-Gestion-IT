from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.schemas.ticket import TicketCreate, TicketOut, TicketUpdate, TicketCerrar
from app.services.ticket_service import (
    obtener_tickets,
    obtener_ticket_por_id,
    crear_ticket,
    actualizar_ticket,
    eliminar_ticket, cerrar_ticket, obtener_tickets_por_tecnico
)

router = APIRouter(prefix="/tickets", tags=["tickets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TicketOut])
def listar_tickets(db: Session = Depends(get_db)):
    return obtener_tickets(db)

@router.get("/{ticket_id}", response_model=TicketOut)
def obtener_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return obtener_ticket_por_id(db, ticket_id)

@router.post("/", response_model=TicketOut)
def crear_nuevo_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return crear_ticket(db, ticket)

@router.put("/{ticket_id}", response_model=TicketOut)
def actualizar_ticket_existente(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    return actualizar_ticket(db, ticket_id, ticket)

@router.delete("/{ticket_id}")
def eliminar_ticket_por_id(ticket_id: int, db: Session = Depends(get_db)):
    return eliminar_ticket(db, ticket_id)



@router.put("/{ticket_id}/cerrar", response_model=TicketOut)
def cerrar_ticket_endpoint(ticket_id: int, datos_cierre: TicketCerrar, db: Session = Depends(get_db)):
    return cerrar_ticket(db, ticket_id, datos_cierre)

@router.get("/tecnico/{id_tecnico}", response_model=List[TicketOut])
def obtener_tickets_de_tecnico(id_tecnico: int, db: Session = Depends(get_db)):
    return obtener_tickets_por_tecnico(db, id_tecnico)