from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate
from datetime import datetime

def obtener_tickets(db: Session):
    return db.query(Ticket).all()

def obtener_ticket_por_id(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    return ticket

def crear_ticket(db: Session, datos: TicketCreate):
    nuevo = Ticket(
        asunto=datos.asunto,
        descripcion=datos.descripcion,
        estado_id=datos.estado_id,
        prioridad_id=datos.prioridad_id,
        id_creador=datos.id_creador,
        id_tecnico=datos.id_tecnico
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def actualizar_ticket(db: Session, ticket_id: int, datos: TicketUpdate):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    ticket.asunto = datos.asunto
    ticket.descripcion = datos.descripcion
    ticket.estado_id = datos.estado_id
    ticket.prioridad_id = datos.prioridad_id
    ticket.id_creador = datos.id_creador
    ticket.id_tecnico = datos.id_tecnico
    ticket.fecha_cierre = datos.fecha_cierre
    ticket.fecha_actualizacion = datetime.utcnow()

    db.commit()
    db.refresh(ticket)
    return ticket

def eliminar_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    db.delete(ticket)
    db.commit()
    return {"mensaje": "Ticket eliminado correctamente"}
